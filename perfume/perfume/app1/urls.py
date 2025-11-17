from django.contrib import admin
from django.urls import path,include
from.views import*
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from app1 import views
urlpatterns = [
    
    path('',index),
    path('index',index),
    path('about',about),
    path('buy_perfume',buy_perfume),
    path('contact',contact),
    path('men',men),
    path('women',women),
    path('exclusive',exclusive),
    path('exclusive1',exclusive1),
    path('product_details/<int:id>',product_details),
    path('cart',cart),
    path('delt/<int:id>',delt),
    path('checkouts',checkout),
    path('thankyou',thankyou),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),

]