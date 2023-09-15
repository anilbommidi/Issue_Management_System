from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated
from errormessage import Errormessage


class Task_Views(generics.GenericAPIView):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """Here Tasks Can Register but Project_Id is mandatory
              (Table_Name:'Tasks_Table')"""
        try:
            serializer = self.get_serializer(data=request.data)
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