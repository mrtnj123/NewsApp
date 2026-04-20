from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('general',views.gen, name='general'),
    path('news',views.news, name='news')

]
