from rest_framework.viewsets import ModelViewSet

from unit.models import BookInfo
from unit.serializers import BookInfoSerializer


class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
