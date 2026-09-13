from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from spells.models import Spells
from spells.serializers import SpellSerializer

class SpellListCreateView(APIView):
    def get(self, request):
        spells = Spells.objects.all()
        serializer = SpellSerializer(spells, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class SpellDetailView(APIView):
    def get_object(self, pk):
        try:
            return Spells.objects.get(pk=pk)
        except Spells.DoesNotExist:
            return None

    def get(self, request, pk):
        spell = self.get_object(pk)

        if spell is None:
            return Response(
                data={'message': 'Spell not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SpellSerializer(spell)
        return Response(serializer.data)

    def put(self, request, pk):
        spell = self.get_object(pk)

        if spell is None:
            return Response(
                data={'message': 'Spell not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = SpellSerializer(spell, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        spell = self.get_object(pk)

        if spell is None:
            return Response(
                data={'message': 'Spell not found.'},
                status=status.HTTP_404_NOT_FOUND
            )
        spell.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)