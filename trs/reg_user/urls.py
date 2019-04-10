from django.urls import path
from . import views,trs
urlpatterns = [
    path('', views.index, name='index'),
    path('form',views.load_form,name='form'),
    path('result',views.disp_res,name='rec'),
]