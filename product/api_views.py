import logging

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from .models import Product, ProductRequest
from .serializers import ProductSerializer
from . import constants
from . import utils
from common import exceptions as common_exceptions

logger = logging.getLogger('application_log')


class ProductList(generics.ListAPIView):
    queryset = Product.objects
    # ToDo Override get_queryset method to change the result/fields for different roles like
    #  admin, staff and customer

    @method_decorator(permission_required('product.view_product', raise_exception=True))
    def get(self, request, *args, **kwargs):
        serializer = ProductSerializer(self.queryset, many=True)
        page = self.paginate_queryset(serializer.data)
        return self.get_paginated_response(page)


class ProductView(APIView):
    """
    Add, retrieve, update or delete a product instance.
    """
    def get_object(self, pk):
        return Product.objects.get(pk=pk)
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    @method_decorator(permission_required('product.view_product', raise_exception=True))
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @method_decorator(permission_required('product.add_product', raise_exception=True))
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(permission_required('product.change_product', raise_exception=True))
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @method_decorator(permission_required('product.delete_product', raise_exception=True))
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductRequestView(APIView):

    MANDATORY_FIELDS = ['quantity', ]
    message = ''

    def is_valid(self, request):
        is_request_valid = True
        message = ''
        for field in self.MANDATORY_FIELDS:
            field_value = request.data.get(field, None)
            if not field_value:
                is_request_valid = False
                message = constants.ERR_MSG_MANDATORY_FIELDS
                break
        if message != '':
            self.message = message
        return is_request_valid

    @method_decorator(permission_required('product.add_product_request', raise_exception=True))
    def post(self, request, pk):
        logger.debug('New Product Request -> %s by %s' % (request.data, request.user))
        # validate request
        if not self.is_valid(request):
            logger.error('New Product Request - Invalid request -> %s' % self.message)
            return Response(
                {'message': self.message},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:

            product = Product.objects.get(id=pk)
            quantity = request.data.get('quantity')

            amount = utils.calculate_amount(product, int(quantity))

            # The request can be created even if the units required is more than units available
            product_request = ProductRequest.objects.create(
                product=product, quantity=quantity, created_by=request.user,
                price_per_unit=product.price, amount=amount
            )

            data = dict(message=constants.SUCC_MSG_REQUEST_CREATED)
            _status = status.HTTP_200_OK
            logger.debug('Created new product request -  %s' % product_request.id)
        except Product.DoesNotExist as error:
            print(error)
            data = dict(message=constants.ERR_MSG_PRODUCT_DOES_NOT_EXIST)
            _status = status.HTTP_500_INTERNAL_SERVER_ERROR
            logger.error('Create new product request Failed -  %s' % error)
        except Exception as error:
            print(error)
            data = dict(message=constants.ERR_MSG_COMMON)
            _status = status.HTTP_500_INTERNAL_SERVER_ERROR
            logger.error('Create new product request Failed -  %s' % error)
        return Response(data, status=_status)


# class ProductRequestList(generics.ListAPIView):
#     queryset = ProductRequest.objects.filter(is_approved=False)
#     ordering_fields = ['updated_on', 'price']
#
#     @method_decorator(permission_required('product.view_product_request', raise_exception=True))
#     def get(self, request, *args, **kwargs):
#         serializer = ProductSerializer(self.queryset, many=True)
#         page = self.paginate_queryset(serializer.data)
#         return self.get_paginated_response(page)


class ApproveProductRequestView(APIView):
    @method_decorator(permission_required('product.approve_product_request', raise_exception=True))
    def get(self, request, pk):
        logger.debug('Approve Product Request -> %s' % pk)
        try:
            # ToDo - Implement rollback if any db query fails
            product_request = ProductRequest.objects.get(id=pk)
            product = product_request.product

            if product_request.quantity > product.quantity:
                raise common_exceptions.CustomError('The requested units are more than the available units.')

            product_request.is_approved=True
            product_request.save()

            product.quantity -= product_request.quantity
            product.save()

            data = dict(message=constants.SUCC_MSG_REQUEST_APPROVED)
            _status = status.HTTP_200_OK
            logger.debug('Approved Request -  %s' % product_request.id)

        except common_exceptions.CustomError as error:
            data = dict(message=str(error))
            _status = status.HTTP_500_INTERNAL_SERVER_ERROR
            logger.error('Approve product request Failed -  %s' % error)

        except Exception as error:
            data = dict(message=constants.ERR_MSG_COMMON)
            _status = status.HTTP_500_INTERNAL_SERVER_ERROR
            logger.error('Approve product request Failed -  %s' % error)
        return Response(data, status=_status)
