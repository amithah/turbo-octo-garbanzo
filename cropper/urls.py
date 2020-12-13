
from django.urls import path,include
from django.views.generic import TemplateView
from .views import photo_list
app_name ="cropper"
urlpatterns = [

    path('', photo_list,name= 'photo_list'),

]
