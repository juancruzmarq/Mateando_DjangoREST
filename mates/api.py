from mates import models
from .serializers import MateSerializer, TipoSerializer, ColorSerializer, PriceHistorySerializer
from rest_framework import viewsets, permissions

# ViewSets define the view behavior.
class MateViewSet(viewsets.ModelViewSet):
    queryset = models.Mate.objects.all() # "queryset" means that the serializer class MateSerializer will serialize and deserialize all the objects in the model Mate
    permission_classes = [ # "permission_classes" means that the serializer class MateSerializer will serialize and deserialize all the objects in the model Mate if the user is authenticated or not authenticated (if the user is authenticated, the user will be able to create, update and delete objects in the model Mate, if the user is not authenticated, the user will be able to only read objects in the model Mate)
        permissions.AllowAny
    ]
    serializer_class = MateSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset = models.Tipo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TipoSerializer

class ColorViewSet(viewsets.ModelViewSet):
    queryset = models.Color.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ColorSerializer

class PriceHistoryViewSet(viewsets.ModelViewSet):
    queryset = models.PriceHistory.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PriceHistorySerializer
