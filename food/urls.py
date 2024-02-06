from . import views
from django.urls import path

app_name = 'food'   #important line these can give you error
urlpatterns = [ 
    path('', views.index,name='index'),
    #dyanamin url pattern defined for the details
    path('<int:item_id>/',views.details,name='details'),
    path('item/', views.item,name='item'),
    # add item urls
    path('add/',views.create_item,name='create_item'),
    #update or edit the currrent img and name
    path('update/<int:id>/',views.update_item,name='update_item'),
    #Delete the file
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    
    
    
]