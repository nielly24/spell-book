from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from categories.models import Categories
from categories.serializers import CategoriesSerializer

class CategoriesListCreateView(APIView):
    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data = serializer.data,
                status = status.HTTP_201_CREATED 
            )
        return Response(
            data = serializer.errors,
            status= status.HTTP_400_BAD_REQUEST
        )

class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Categories.objects.get(pk = pk)
        except Categories.DoesNotExist:
            return  None
    def get (self, request, pk):
        category = self.get_object(pk)

        if category is None :
            return Response(
                data = {'message': 'Category Not Found.'},
                status = status.HTTP_404_NOT_FOUND
            )  
        serializer = CategoriesSerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = self.get_object(pk)

        if category is None:
            return Response(
                data = {'message': 'Category Not Found'},
                status = status.HTTP_404_NOT_FOUND
            )
        serializer = CategoriesSerializer(category, request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(serializer.data)
        return Response(
            data = serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
        )      
    def delete(self, request, pk):
        category = self.get_object(pk)    
        if category is None:
            return Response(
                data = {'message': 'Category Not Found.'},
                status = status.HTTP_404_NOT_FOUND
            )
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)