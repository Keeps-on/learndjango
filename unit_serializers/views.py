from rest_framework.viewsets import ModelViewSet

from unit.models import BookInfo
from unit_serializers.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


