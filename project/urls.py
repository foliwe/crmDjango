from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_record/', views.create_record, name='create_record'),
    path('record/<int:pk>', views.view_record, name='view_record'),
    path('update_record/<int:pk>', views.update_record, name='update'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),



]
