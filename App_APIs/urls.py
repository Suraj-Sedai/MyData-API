from django.urls import path, include
from App_APIs.views import MyModelList, MyModelDetail
from .views import api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('mymodels/', MyModelList.as_view(), name='mymodel-list'),
    path('mymodels/<int:pk>/', MyModelDetail.as_view(), name='mymodel-detail'),
    # Add more URL patterns here as needed
]
