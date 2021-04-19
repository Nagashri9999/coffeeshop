from django.urls import path
from coffeeapp import views


urlpatterns=[
    path('',views.index,name='index') ,
    path('about',views.about,name='about'),
    path('gallery',views.gallery,name='gallery'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('order',views.order,name='order'),
    path('orderplaced',views.orderplaced,name='orderplaced') ,   
]


