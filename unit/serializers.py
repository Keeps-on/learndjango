from rest_framework import serializers

from unit.models import BookInfo

class BookInfoSerializer(serializers.ModelSerializer):
    """序列化器类"""
    class Meta:
        model = BookInfo
        fields = '__all__'
        # fields = ('id', 'btitle', 'bpub_date', 'bread', 'bcomment', 'image')



