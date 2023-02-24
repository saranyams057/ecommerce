from . import views
from django.contrib import admin
from django.urls import path, include
app_name='shopapp'
urlpatterns = [
    #path('',views.index,name="index"),
    path('',views.Allprodcat,name='Allprodcat'),
    path('<slug:c_slug>/',views.Allprodcat,name='Products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodCatdetail')
]