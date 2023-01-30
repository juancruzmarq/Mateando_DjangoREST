from rest_framework import serializers
from mates.models import Mate, Tipo, Color, PriceHistory

# Serializers define the API representation. 
class MateSerializer(serializers.ModelSerializer):

  class Meta:
      model = Mate
      fields = "__all__" # "__all__" means all fields in the model will be serialized and deserialized by the serializer class MateSerializer
      read_only_fields = ("created_at", "updated_at",) # "read_only_fields" means that the fields in the list will be serialized but not deserialized by the serializer class MateSerializer

class TipoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tipo
    fields = "__all__"
    read_only_fields = ("created_at", "updated_at",)

class ColorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Color
    fields = "__all__"
    read_only_fields = ("created_at", "updated_at",)

class PriceHistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = PriceHistory
    fields = "__all__"
    read_only_fields = ("created_at", "updated_at",)
