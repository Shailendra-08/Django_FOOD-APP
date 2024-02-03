
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    #dyanamin url pattern defined for the details
    path('<int:item_id>/',views.details,name='details'),
    path('item/', views.item,name='item'),
    

]