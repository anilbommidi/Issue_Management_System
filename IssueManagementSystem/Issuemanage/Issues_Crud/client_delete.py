from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Client
from genericresponse import GenericResponse
from errormessage import Errormessage
import json


class Client_Delete_Views(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, Client_Id):
        try:
            client = Client.objects.get(Client_Id=Client_Id)
            client.delete()
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Successfully deleted"
            response.Result = None
            response.Status = 200
            response.HasError = False
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=204)
        except Client.DoesNotExist:
            response = GenericResponse("Message", "Result", "Status", "HasError")
            response.Message = "Client not found"
            response.Result = None
            response.Status = 404
            response.HasError = True
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=404)
        except Exception as e:
            response = GenericResponse("message", "result", "status", "has_error")
            response.Message = Errormessage(e)
            response.Result = None
            response.Status = 500
            response.HasError = True
            json_str = json.dumps(response.__dict__)
            return Response(json.loads(json_str), status=500)
