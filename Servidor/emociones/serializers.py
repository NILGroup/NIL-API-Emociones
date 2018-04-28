from rest_framework import serializers
from emociones.models import Palabra

class PalabraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Palabra
		fields = ('id','palabra','lexema','grados')