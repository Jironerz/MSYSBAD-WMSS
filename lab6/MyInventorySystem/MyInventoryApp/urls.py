from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('main', views.main, name="main"),
    path('add_bottle/', views.add_bottle, name='add_bottle'),
    path('signup/', views.signup, name='signup'),
    path('view_supplier/<int:pk>', views.view_supplier, name='view_supplier'),
    path('view_bottles/<int:pk>', views.view_bottles, name='view_bottles'),
    path('manage_account/<int:pk>/', views.manage_account, name="manage_account"),
    path('logout', views.logout, name="logout"),
    path('delete_user/<int:pk>/', views.delete_user, name="delete_user"),
    path('view_bottle_details/<str:pk>', views.view_bottle_details, name='view_bottle_details'),
    path('change_password/<int:pk>/', views.change_password, name="change_password"),
    path('delete_bottle/<str:pk>/', views.delete_bottle, name="delete_bottle"),
]

