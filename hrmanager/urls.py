from django.urls import path

from hrmanager import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.create_employee_record, name='create_employee'),
    path('update/<int:id>', views.update_employee_record, name='update_employee'),
    path('delete/<int:id>', views.delete_employee_record, name='delete_employee'),

]