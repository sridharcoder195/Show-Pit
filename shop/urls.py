from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('<slug:c_slug>/',views.home_page,name='product'),
    path('<slug:c_slug>/<slug:product_slug>/',views.pd,name='product'),
    path('search',views.search,name='searching')
]
