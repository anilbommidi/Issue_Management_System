from django.contrib.auth.hashers import check_password
from rest_framework import generics
from ..serializers import *
from rest_framework.response import Response
from ..models import *
import json
from genericresponse import GenericResponse
from rest_framework.permissions import IsAuthenticated


class Client_Login_Views(generics.GenericAPIView):
    serializer_class = ClientLoginSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        Client_Email = request.data.get('Client_Email')
        Client_Password = request.data.get('Client_Password')
        if Client_Email.endswith('.com'):
            try:
                a = Client.objects.get(Client_Email=Client_Email)
                if check_password(Client_Password, a.Client_Password):
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Successful"
                    response.Result = ClientSerializer(a).data
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)
                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Incorrect Password/UserName"
                    response.Result = []
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
            except:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Incorrect Password/UserName"
                response.Result = []
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

        elif Client.objects.get(Client_Phone_Number=Client_Email):
            try:
                a = Client.objects.get(Client_Phone_Number=Client_Email)
                if check_password(Client_Password, a.Client_Password):
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Successful"
                    response.Result = ClientSerializer(a).data
                    response.Status = 200
                    response.HasError = False
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=200)

                else:
                    response = GenericResponse("Message", "Result", "Status", "HasError")
                    response.Message = "Incorrect Password/UserName"
                    response.Result = []
                    response.Status = 400
                    response.HasError = True
                    jsonStr = json.dumps(response.__dict__)
                    return Response(json.loads(jsonStr), status=400)
            except:
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Incorrect Password/UserName"
                response.Result = []
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

        else:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "user not found"
            response.Result = []
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
