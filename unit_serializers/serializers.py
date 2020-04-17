from rest_framework import serializers

from unit.models import BookInfo


class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)

"""
序列化 
    DB --- > chrome
read_only = true 表示前台提交表单可以不用提交(也可以表示该字段只从数据库中读取)
requires = False 表示该字段可以不用提交 默认requires = True

反序列化
    chrome --- > DB
write_only 表明该字段仅用于反序列化输入，默认False
default 反序列化时使用的默认值

"""