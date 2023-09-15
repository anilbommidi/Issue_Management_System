from rest_framework.utils import json
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import PasswordChangeSerializer
from ..models import *
from genericresponse import GenericResponse
from errormessage import Errormessage
from django.contrib.auth.hashers import make_password, check_password


class Client_Password_Change(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, Client_Id):
        try:
            current_password = request.data.get('CurrentPassword')
            new_password = request.data.get('NewPassword')
            confirm_password = request.data.get('ConfirmPassword')
            user_query = Client.objects.get(Client_Id=Client_Id)
            n = check_password(current_password, user_query.Client_Password)
            if n and new_password == confirm_password:
                s = make_password(confirm_password)
                user_query.Client_Password = s
                user_query.save()
                response = GenericResponse("Message", "Result", "Status", "HasError")
                response.Message = "Successful"
                response.Result = "Successfully Changed Your Password"
                response.Status = 200
                response.HasError = False
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=200)
            else:
                response = GenericResponse("message", "result", "status", "has_error")
                response.Message = Errormessage("you entered password is wrong")
                response.Result = False
                response.Status = 400
                response.HasError = True
                jsonStr = json.dumps(response.__dict__)
                return Response(json.loads(jsonStr), status=400)

        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = False
            response.Status = 400
            response.HasError = True
            jsonStr = json.dumps(response.__dict__)
            return Response(json.loads(jsonStr), status=400)
