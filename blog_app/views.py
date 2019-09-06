from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView,DeleteView  
from django.urls import reverse_lazy 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from blog_app.models import Post
from	rest_framework	import	generics
from blog_app.serializers import Blog_appSerializer
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): 
    model = Post
    template_name= 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): 
    model = Post
    template_name= 'post_edit.html'
    fields = ['title', 'body']  

class BlogDeleteView(DeleteView): 
    model = Post
    template_name= 'post_delete.html'
    success_url = reverse_lazy('home')

class	PostListView(generics.ListAPIView):
		queryset	=	Post.objects.all()
		serializer_class	=	Blog_appSerializer
        
class PostDetailView(generics.RetrieveAPIView):
				queryset	=	Post.objects.all()
				serializer_class	=	Blog_appSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Blog_appSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Blog_appSerializer