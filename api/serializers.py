from rest_framework import serializers
from .models import Sequence

class SequenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sequence
        fields = (
            "id",
            "user_id",
            "title",
            "sequence",
            "note",
            "nb_bases",
            "nb_a",
            "nb_c",
            "nb_g",
            "nb_t",
            "percentage_a",
            "percentage_c",
            "percentage_g",
            "percentage_t",
            "percentage_gc",
            "percentage_at",
        )