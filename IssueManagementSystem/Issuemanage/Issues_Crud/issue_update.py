from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated
from errormessage import Errormessage
from ..models import *


class Issue_Update_Views(generics.GenericAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, Issue_Id):
        """Here Client Can Update Details
              (Table_Name:'Clients_Table')"""
        try:
            a = Issues.objects.get(Issue_Id=Issue_Id)
            Task_Id = request.data.get('Task_Id')
            Issue_Name = request.data.get('Issue_Name')
            Issue_Raised_By = request.data.get('Issue_Raised_By')
            Issue_Assigned_To = request.data.get('Issue_Assigned_To')
            Issue_Description = request.data.get('Issue_Description')
            Issue_Date = request.data.get('Issue_Date')
            Issue_Status = request.data.get('Issue_Status')
            Issue_Priority = request.data.get('Issue_Priority')
            data = {'Task_Id': Task_Id, 'Issue_Name': Issue_Name, 'Issue_Raised_By': Issue_Raised_By, 'Issue_Assigned_To': Issue_Assigned_To,
                    'Issue_Description': Issue_Description, 'Issue_Date': Issue_Date, 'Issue_Status':Issue_Status, 'Issue_Priority':Issue_Priority
                    }
            serializer = IssueSerializer(a, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = IssueSerializer(user).data
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