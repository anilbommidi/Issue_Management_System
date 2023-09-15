from django.db import models
from _datetime import datetime


class Client(models.Model):
    Client_Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Client_Name = models.CharField(max_length=200)
    Client_Email = models.CharField(max_length=200, unique=True)
    Client_Phone_Number = models.CharField(max_length=40)
    Client_Password = models.CharField(max_length=200)
    Client_Address = models.CharField(max_length=200)
    Client_Description = models.CharField(max_length=500)
    objects = models.Manager

    class Meta:
        db_table = 'Client_Table'


Status = (
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed')

)
Priority = (
    ('High', 'High'),
    ('Medium', 'Medium'),
    ('Low', 'Low')
)


class Projects(models.Model):
    Client_Id = models.ForeignKey(Client, related_name='Client', on_delete=models.CASCADE, default=True)
    Project_Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Project_Name = models.CharField(max_length=200)
    Project_Description = models.CharField(max_length=500)
    Project_Start_Date = models.DateField(default=datetime.today)
    Project_End_Date = models.DateField(default=datetime.today)
    Project_Status = models.CharField(max_length=20, choices=Status)
    Project_Priority = models.CharField(max_length=20, choices=Priority)
    objects = models.Manager

    class Meta:
        db_table = 'Projects_Table'


class Tasks(models.Model):
    Project_Id = models.ForeignKey(Projects, related_name='Projects', on_delete=models.CASCADE, default=True)
    Task_Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Task_Name = models.CharField(max_length=200)
    Task_Description = models.CharField(max_length=500)
    Task_Start_Date = models.DateField(default=datetime.today)
    Task_End_Date = models.DateField(default=datetime.today)
    Task_Status = models.CharField(max_length=20, choices=Status)
    Task_Priority = models.CharField(max_length=20, choices=Priority)
    objects = models.Manager

    class Meta:
        db_table = 'Tasks_Table'


class Issues(models.Model):
    Task_Id = models.ForeignKey(Tasks, related_name='Projects', on_delete=models.CASCADE, default=True)
    Issue_Id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    Issue_Name = models.CharField(max_length=200)
    Issue_Raised_By = models.CharField(max_length=200)
    Issue_Assigned_To = models.CharField(max_length=200)
    Issue_Description = models.CharField(max_length=500)
    Issue_Date = models.DateField(auto_now=True)
    Issue_Status = models.CharField(max_length=20, choices=Status)
    Issue_Priority = models.CharField(max_length=20, choices=Priority)
    objects = models.Manager

    class Meta:
        db_table = 'Issues_Table'
