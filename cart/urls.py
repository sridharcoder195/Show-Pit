from django.urls import path
from . import views

urlpatterns = [
    path('cart_details', views.cart_page, name='cart'),
    path('add/<int:prod_id>/',views.add_to_cart,name='addcart'),
    path('decrement/<int:prod_id>/', views.miin_cart, name='decrement'),
    path('del/<int:prod_id>/', views.delete, name='delitem'),

]