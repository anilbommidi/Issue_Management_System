from django.urls import path
from .views import *

urlpatterns = [
    path('client_register/', Client_Views.as_view()),
    path('client_login/', Client_Login_Views.as_view()),
    path('client_password_change/<int:Client_Id>', Client_Password_Change.as_view()),
    path('clients_get_all/', Client_Get_Views.as_view()),
    path('clients_get_by_id/<int:Client_Id>', Client_Get_By_Id_Views.as_view()),
    path('clients_update/<int:Client_Id>', Client_Update_Views.as_view()),
    path('clients_delete/<int:Client_Id>', Client_Delete_Views.as_view()),
    path('projects/', Project_Views.as_view()),
    path('projects_get_all/', Project_Get_Views.as_view()),
    path('projects_get_by_project_id/<int:Project_Id>', Project_Get_By_Project_Id.as_view()),
    path('projects_get_by_client_id/<int:Client_Id>', Project_Get_By_Client_Id.as_view()),
    path('projects_update/<int:Project_Id>', Project_Update_Views.as_view()),
    path('tasks/', Task_Views.as_view()),
    path('tasks_get_all/', Task_Get_Views.as_view()),
    path('tasks_get_by_id/<int:Task_Id>', Task_Get_Task_Id.as_view()),
    path('tasks_get_by_project_id/<int:Project_Id>', Task_Get_Project_Id.as_view()),
    path('tasks_update/<int:Task_Id>', Task_Update_Views.as_view()),
    path('issues/', Issue_Views.as_view()),
    path('issues_get_all/', Issue_Get_Views.as_view()),
    path('issues_get_by_id/<int:Issue_Id>', Issue_Get_By_Id.as_view()),
    path('issues_get_by_task_id/<int:Task_Id>', Issue_Get_By_Task_Id.as_view()),
    path('issues_filter_by_status/<str:Issue_Status>', Issue_Filter_By_Status.as_view()),
    path('issues_filter_by_priority/<str:Issue_Priority>', Issue_Filter_By_Priority.as_view()),
    path('issues_update/<int:Issue_Id>', Issue_Update_Views.as_view()),
]
