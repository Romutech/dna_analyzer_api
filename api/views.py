from rest_framework import viewsets
from .serializers import SequenceSerializer
from .models import Sequence


class SequenceViewSet(viewsets.ModelViewSet):
    queryset = Sequence.objects.all().order_by('title')
    serializer_class = SequenceSerializer
