from rest_framework import serializers
from .models import Sequence

class SequenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sequence
        fields = (
            "uuid",
            "user_id",
            "file_path",
            "title",
            "file",
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
            "dna_walk_graph_data",
            "ratio_g_c_graph_data",
        )