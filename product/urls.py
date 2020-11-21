from django.contrib import admin
from django.urls import path, include, re_path


from . import api_views

urlpatterns = [
    path(r'list/', api_views.ProductList.as_view()),
    path(r'', api_views.ProductView.as_view()),
    path(r'<int:pk>/', api_views.ProductView.as_view()),
    path(r'<int:pk>/request/', api_views.ProductRequestView.as_view()),
    path(r'request/<int:pk>/approve/', api_views.ApproveProductRequestView.as_view()),
]