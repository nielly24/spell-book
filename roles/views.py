from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin
from roles.models import Roles
from roles.serializers import RoleSerializer

class RoleListView(APIView):
    def get(self, request):
        roles = Roles.objects.all()
        serializer = RoleSerializer(roles, many = True)
        return Response(serializer.data)
        
class RoleCreateView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        serializer = RoleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data = serializer.data,
                status = status.HTTP_201_CREATED
            )
        return Response(
            data = serializer.errors,
            status =status.HTTP_400_BAD_REQUEST

        )

class RoleDetailView(APIView):
    permission_classes = [IsAdmin]
    def get_object(self, pk):
        try:
            return Roles.objects.get(pk=pk)
        except Roles.DoesNotExist:
                return None
   
    def get(self, request, pk):
        role = self.get_object(pk)

        if role is None:
            return Response(
                data = {'message': 'Role Not Found.'},
                status = status.HTTP_404_NOT_FOUND
 
            )
        serializer =  RoleSerializer(role)
        return Response(serializer.data)

    def put(self, request, pk):
        role = self.get_object(pk)

        if role is None:
            return Response(
                data = {'message':  'Role not Found.'},
                status = status.HTTP_404_NOT_FOUND
            )
        serializer = RoleSerializer(role, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            data = serializer.errors,
            status = status.HTTP_400_BAD_REQUEST 
        ) 

    def delete(self, request, pk):
        role = self.get_object(pk)

        if role is None:
            return Response(
                data = {'message': 'Role not found.'},
                status = status.HTTP_404_NOT_FOUND
            )
        role.delete()
        return Response(status = status.HTTP_204_NO_CONTENT
        )





        