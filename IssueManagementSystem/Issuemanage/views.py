from .Issues_Crud.client_register import Client_Views
from .Issues_Crud.client_login import Client_Login_Views
from .Issues_Crud.client_get_all import Client_Get_Views
from .Issues_Crud.project_register import Project_Views
from .Issues_Crud.project_get_all import Project_Get_Views
from .Issues_Crud.task_register import Task_Views
from .Issues_Crud.task_get_all import Task_Get_Views
from .Issues_Crud.issue_register import Issue_Views
from .Issues_Crud.issue_get_all import Issue_Get_Views
from .Issues_Crud.change_password import Client_Password_Change
from .Issues_Crud.client_get_by_id import Client_Get_By_Id_Views
from .Issues_Crud.projects_get_by_id import Project_Get_By_Project_Id
from .Issues_Crud.projects_get_by_client_id import Project_Get_By_Client_Id
from .Issues_Crud.task_get_by_id import Task_Get_Task_Id
from .Issues_Crud.task_get_by_project_id import Task_Get_Project_Id
from .Issues_Crud.issue_get_by_id import Issue_Get_By_Id
from .Issues_Crud.issue_get_by_task_id import Issue_Get_By_Task_Id
from .Issues_Crud.issue_filter_by_status import Issue_Filter_By_Status
from .Issues_Crud.issue_filter_by_priority import Issue_Filter_By_Priority
from .Issues_Crud.client_update import Client_Update_Views
from .Issues_Crud.project_update import Project_Update_Views
from .Issues_Crud.task_update import Task_Update_Views
from .Issues_Crud.issue_update import Issue_Update_Views
from .Issues_Crud.client_delete import Client_Delete_Views

Client_Views()
Client_Login_Views()
Client_Get_Views()
Project_Views()
Project_Get_Views()
Task_Views()
Task_Get_Views()
Issue_Views()
Issue_Get_Views()
Client_Password_Change()
Client_Get_By_Id_Views()
Project_Get_By_Project_Id()
Project_Get_By_Client_Id()
Task_Get_Task_Id()
Task_Get_Project_Id()
Issue_Get_By_Id()
Issue_Get_By_Task_Id()
Issue_Filter_By_Status()
Issue_Filter_By_Priority()
Client_Update_Views()
Project_Update_Views()
Task_Update_Views()
Issue_Update_Views()
Client_Delete_Views()



