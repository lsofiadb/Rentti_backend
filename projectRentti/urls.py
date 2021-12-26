"""projectRentti URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from renttiApp import views
from renttiApp.views.reservationDetailView import ReservationDetailView, ReservationApi, ReservationUpdateApi,ReservationDeleteApi
from renttiApp.views.vehicleDetailView import VehicleDetailView, VehicleApi, VehicleUpdateApi, VehicleDeleteApi
from renttiApp.views.leaseholderDetailView import LeaseholderDetailView, LeaseholderApi, LeaseholderUpdateApi, LeaseholderDeleteApi
from renttiApp.views.supplierDetailView import SupplierDetailView, SupplierApi, SupplierUpdateApi, SupplierDeleteApi


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('api/',ReservationApi.as_view()),
    path('api/create', ReservationDetailView.as_view()),
    path('api/<int:pk>',ReservationUpdateApi.as_view()),
    path('api/<int:pk>/delete',ReservationDeleteApi.as_view()),
    path('vehicle/',VehicleApi.as_view()),
    path('vehicle/create',VehicleDetailView.as_view()),
    path('vehicle/<int:pk>',VehicleUpdateApi.as_view()),
    path('vehicle/<int:pk>/delete',VehicleDeleteApi.as_view()),
    path('leaseholder/',LeaseholderApi.as_view()),
    path('leaseholder/<int:pk>',LeaseholderUpdateApi.as_view()),
    path('supplier/',SupplierApi.as_view()),
    path('supplier/<int:pk>',SupplierUpdateApi.as_view()),
]