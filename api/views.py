from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.decorators import api_view

from .models import Vgames
from .serializers import VgameSerializer

@api_view (['GET'])
def getVgames (request):
    vgame = Vgames.objects.all()
    serializer = VgameSerializer (vgame, many=True)
    return Response(serializer.data)

@api_view (['POST'])
def postVgames(request):
    data = request.data
    vgame = Vgames.objects.create(
        nombre = data['nombre']
    )
    serializer = VgameSerializer(vgame, many = False)
    return Response(serializer.data)

@api_view (['PUT'])
def putVgames(request, pk):
    data = request.data
    vgame = Vgames.objects.get( id = pk)
    serializer = VgameSerializer(instance = vgame, data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view (['DELETE'])
def deleteVgames(request, pk):
    data = request.data
    vgame = Vgames.objects.get( id = pk)
    vgame.delete()
    return Response('Videojuego eliminado.')