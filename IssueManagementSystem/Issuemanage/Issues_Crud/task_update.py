from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated
from errormessage import Errormessage
from ..models import *


class Task_Update_Views(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, Task_Id):
        """Here Client Can Update Details
              (Table_Name:'Clients_Table')"""
        try:
            a = Tasks.objects.get(Task_Id=Task_Id)
            Project_Id = request.data.get('Project_Id')
            Task_Name = request.data.get('Task_Name')
            Task_Description = request.data.get('Task_Description')
            Task_Start_Date = request.data.get('Task_Start_Date')
            Task_End_Date = request.data.get('Task_End_Date')
            Task_Status = request.data.get('Task_Status')
            Task_Priority = request.data.get('Task_Priority')
            data = {'Project_Id': Project_Id, 'Task_Name': Task_Name, 'Task_Description': Task_Description, 'Task_Start_Date': Task_Start_Date,
                    'Task_End_Date': Task_End_Date, 'Task_Status': Task_Status, 'Task_Priority':Task_Priority
                    }
            serializer = TaskSerializer(a, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = TaskSerializer(user).data
            response.Status = 200
            response.HasError = False
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=200)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)