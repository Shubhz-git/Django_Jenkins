"""CarWashSystem URL Configuration

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
from django.contrib import admin
from django.urls import path
from carwash.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', adminlogin, name='login'),
    path('contact', contact, name='contact'),
    path('admin_home', admin_home,name='admin_home'),
    path('addCarWashpoint', addCarWashpoint,name='addCarWashpoint'),
    path('manageCarWashpoint', manageCarWashpoint,name='manageCarWashpoint'),
    path('editCarWashPoint/<int:pid>', editCarWashPoint,name='editCarWashPoint'),
    path('delete_CarWash/<int:pid>', delete_CarWash,name='delete_CarWash'),
    path('addBooking', addBooking,name='addBooking'),
    path('customerBook', customerBook,name='customerBook'),
    path('view_BookingDtls/<int:pid>', view_BookingDtls,name='view_BookingDtls'),
    path('newBooking', newBooking,name='newBooking'),
    path('completeBooking', completeBooking,name='completeBooking'),
    path('delete_booking/<int:pid>', delete_booking, name='delete_booking'),
    path('allBooking', allBooking,name='allBooking'),
    path('ChangePassword', ChangePassword,name='ChangePassword'),
    path('logout', Logout, name='logout'),
    path('unread_queries', unread_queries, name='unread_queries'),
    path('read_queries', read_queries, name='read_queries'),
    path('view_queries/<int:pid>', view_queries, name='view_queries'),
]
