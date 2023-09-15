from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated
from errormessage import Errormessage
from ..models import *


class Client_Update_Views(generics.GenericAPIView):
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, Client_Id):
        """Here Client Can Update Details
              (Table_Name:'Clients_Table')"""
        try:
            a = Client.objects.get(Client_Id=Client_Id)
            Client_Name = request.data.get('Client_Name')
            Client_Email = request.data.get('Client_Email')
            Client_Phone_Number = request.data.get('Client_Phone_Number')
            Client_Password = request.data.get('Client_Password')
            Client_Address = request.data.get('Client_Address')
            Client_Description = request.data.get('Client_Description')
            data = {'Client_Name': Client_Name, 'Client_Email': Client_Email, 'Client_Phone_Number': Client_Phone_Number, 'Client_Password': Client_Password,
                    'Client_Address': Client_Address, 'Client_Description': Client_Description
                    }
            serializer = ClientSerializer(a, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successful"
            response.Result = ClientSerializer(user).data
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