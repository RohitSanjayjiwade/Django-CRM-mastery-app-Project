from django.urls import path

from . import views

# app_name = 'webapp'

urlpatterns = [
	path('', views.index, name=''),
	path('register/', views.register, name='register'),
	path('login/', views.my_login, name='my_login'),

	# CRUD

	path('dashboard', views.dashboard, name='dashboard'),
	path('create-record', views.create_record, name='create_record'),
	path('update-record/<int:id>', views.update_record, name='update_record'),
	path('view-record/<int:id>', views.view_record, name='view_record'),
	path('delete-record/<int:id>', views.delete_record, name='delete_record'),


	path('logout/', views.user_logout, name='user_logout'),

]