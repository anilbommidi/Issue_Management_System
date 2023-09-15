from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
from ..models import *
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated
from errormessage import Errormessage


class Issue_Filter_By_Priority(generics.GenericAPIView):
    serializer_class = IssueSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, Issue_Priority):
        try:
            data = Issues.objects.filter(Issue_Priority=Issue_Priority)
            serializer = self.get_serializer(data, many=True)
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = serializer.data
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