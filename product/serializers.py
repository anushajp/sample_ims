import datetime

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # name = serializers.SerializerMethodField()
    # start_date = serializers.SerializerMethodField()
    # start_date_in_format1 = serializers.SerializerMethodField()
    # duration_days = serializers.SerializerMethodField()
    # duration_nights = serializers.SerializerMethodField()
    # # travel_quote = serializers.CharField(source='travel_quote')
    # trip_code = serializers.SerializerMethodField()
    # image = serializers.SerializerMethodField()
    # amount = serializers.SerializerMethodField()
    # rating = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()
    # # is_invited = serializers.SerializerMethodField()
    # # invited_by = serializers.SerializerMethodField()
    # # invited_on = serializers.SerializerMethodField()
    # # has_enquired = serializers.SerializerMethodField()
    # # has_favourited = serializers.SerializerMethodField()
    # # has_joined = serializers.SerializerMethodField()
    # #  user_images = serializers.SerializerMethodField()
    # # has_rejected = serializers.SerializerMethodField()
    # # has_paid = serializers.SerializerMethodField()
    # short_description = serializers.CharField(source='short_desc')
    # detailed_description = serializers., given the validated data.CharField(source='detailed_desc')
    # # respond_by = serializers.SerializerMethodField()
    # inclusions = serializers.SerializerMethodField()
    # highlights = serializers.SerializerMethodField()
    # has_booked = serializers.SerializerMethodField()
    # hotels = serializers.SerializerMethodField()
    # trip_type = serializers.SerializerMethodField()
    # is_confirmed = serializers.SerializerMethodField()
    # countries = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'description', 'quantity', 'price',
            'created_on', 'updated_on',
        )

    # def __init__(self, *args, **kwargs):
    #     remove_fields = kwargs.pop('exclude', None)
    #     current_user = kwargs.pop('current_user', None)
    #     self.view = kwargs.pop('view', None)
    #     super(TourSerializer, self).__init__(*args, **kwargs)
    #
    #     if remove_fields:
    #         # for multiple fields in a list/tuple
    #         for field_name in remove_fields:
    #             self.fields.pop(field_name)
    #     self.current_user = current_user

    # def get_duration_days(self, obj):
    #     count = PitstopItinerary.objects.filter(
    #         pitstop__package_pitstop__tour_city__tour_country__tour=obj
    #     ).count()
    #     return count
    #
    # def get_duration_nights(self, obj):
    #     count = self.get_duration_days(obj)
    #     return count-1
    #
    # def get_countries(self, obj):
    #     countries = list(obj.package_countries.values_list('country__name', flat=True))
    #     return countries
    #
    # def get_is_confirmed(self, obj):
    #     return False
    #
    # def get_name(self, obj):
    #     return obj.title
    #
    # def get_trip_type(self, obj):
    #     return 'tour'
    #
    # def get_trip_code(self, obj):
    #     return obj.tour_code
    #
    #
    # def get_highlights(self, obj):
    #     highlights = obj.highlights.split('\r\n') if obj.highlights else []
    #     return highlights
    #
    #
    # def get_inclusions(self, obj):
    #     inclusions = obj.inclusions.split(',') if obj.inclusions else []
    #     return inclusions
    #
    # def get_start_date_in_format1(self, obj):
    #         return ""
    #
    # def get_start_date(self, obj):
    #     if self.view == "all":
    #         return ""
    #     else:
    #         return ""
    #
    # def get_image(self, obj):
    #     return '/media/' + str(obj.image)
    #
    # def get_amount(self, obj):
    #     try:
    #         amount = min(list(obj.price_list.values_list(
    #             'thirty_five_plus_premier', flat=True
    #         )))
    #         formatted_amount = trip_utils.format_amount(amount)
    #     except Exception as e:
    #         formatted_amount = "To be decided"
    #     return formatted_amount
    #
    # def get_rating(self, obj):
    #     return obj.user_rating
    #
    # def get_tags(self, obj):
    #     tags = list(obj.tags.all().values_list('name', flat=True))
    #     result_tags = [item.upper() for item in tags]
    #     return result_tags
    #
    # def get_has_booked(self, obj):
    #     return False
    #
    # def get_hotels(self, obj):
    #     hotel_data = []
    #     hotels = TourHotel.objects.filter(
    #         tour_pitstop__tour_city__tour_country__tour=obj
    #     ).distinct('hotel')
    #     for hotel in hotels:
    #         data = {
    #             'place': hotel.hotel.name,
    #             'city': hotel.hotel.city.name,
    #             'type_of_room': hotel.hotel_type,
    #             'address': hotel.hotel.address,
    #             'latitude': hotel.hotel.location_latitude
    #             if hotel.hotel.location_latitude else '',
    #             'logitude': hotel.hotel.location_logitude
    #             if hotel.hotel.location_logitude else '',
    #             'image': str(
    #                 hotel.hotel.image) if hotel.hotel.image
    #             else '/static/common/images/jrnyon_common_default.jpg',
    #             'description': hotel.hotel.description,
    #             'details': ''
    #         }
    #         hotel_data.append(data)
    #     return hotel_data

    def create(self, validated_data):
        """
        Create and return a new Product instance.
        """
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update the product instance
        """
        instance.title = validated_data.get('name', instance.name)
        instance.code = validated_data.get('quantity', instance.code)
        instance.linenos = validated_data.get('price', instance.linenos)
        instance.language = validated_data.get('description', instance.language)
        instance.save()
        return instance
