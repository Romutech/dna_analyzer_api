from rest_framework import serializers
from .models import Sequence

class SequenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sequence
        fields = ('user_id', 'title', 'file_path', 'note')