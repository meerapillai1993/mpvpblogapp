from rest_framework import serializers
from blog_app.models import Post


class Blog_appSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','title','author','body') 
        model=Post
       
    