import uuid
import hashlib
import datetime
import math

from django.conf import settings
from django.core.paginator import Paginator

from rest_framework.views import APIView

from . import constants


class BaseAPIListView(APIView):
    base_fields = []
    renderer_classes = []
    order_fields = {}

    default_order_key = '_created_on'

    def _paginate(self, queryset, request_page_num=1, page_size=constants.DEFAULT_PAGE_SIZE):
        paginator = Paginator(queryset, page_size)
        if request_page_num <= paginator.num_pages:
            return paginator.page(request_page_num).object_list
        return queryset
