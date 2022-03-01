from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('base', views.base, name='base'),
    path('add_customer/',  views.add_customer, name='add_customer'),
    path('create_account/', views.create_account, name = 'create_account'),
    path('view_customer/', views.view_customer, name="view_customer"),
    path('update_customer/<int:pk>', views.update_customer, name="update_customer"),
    
   # path('manage_account', views.manage_account, name="manage_account"),
   # path('delete_account', views.delete_account, name="delete_account"),
]