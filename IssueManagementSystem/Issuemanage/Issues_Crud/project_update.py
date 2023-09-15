from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated
from errormessage import Errormessage
from ..models import *


class Project_Update_Views(generics.GenericAPIView):
    serializer_class = ProjectsSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, Project_Id):
        """Here Client Can Update Details
              (Table_Name:'Clients_Table')"""
        try:
            a = Projects.objects.get(Project_Id=Project_Id)
            Client_Id = request.data.get('Client_Id')
            Project_Name = request.data.get('Project_Name')
            Project_Description = request.data.get('Project_Description')
            Project_Start_Date = request.data.get('Project_Start_Date')
            Project_End_Date = request.data.get('Project_End_Date')
            Project_Status = request.data.get('Project_Status')
            Project_Priority = request.data.get('Project_Priority')
            data = {'Client_Id': Client_Id, 'Project_Name': Project_Name, 'Project_Description': Project_Description, 'Project_Start_Date': Project_Start_Date,
                    'Project_End_Date': Project_End_Date, 'Project_Status': Project_Status, 'Project_Priority':Project_Priority
                    }
            serializer = ProjectsSerializer(a, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = ProjectsSerializer(user).data
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