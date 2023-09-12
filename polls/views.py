from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import authorModel,bookModel
from .serializers import authorSerializer,bookSerializer
import datetime

# Create your views here.

class getAllBooks(APIView):
    def get(self,request):
        some=bookModel.objects.all()
        serializer=bookSerializer(some,many=True)
        return Response(serializer.data)
    
class getAllAuthors(APIView):
    def get(self,request):
        some=authorModel.objects.all()
        serializer=authorSerializer(some,many=True)
        return Response(serializer.data)
    
class createAuthor(APIView):
    def post(self,request):
        serializer=authorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class createBook(APIView):
    def post(self,request):
        serializer=bookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class changeAuthor(APIView):
    def patch(self,request,*args,**kwargs):
        x=get_object_or_404(authorModel,id=kwargs['forid'])
        serializer=authorSerializer(x,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)

class changeBook(APIView):
    def patch(self,request,*args,**kwargs):
        x=get_object_or_404(bookModel,id=kwargs['forid'])
        serializer=bookSerializer(x,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    
class deleteAuthor(APIView):
    def delete(self,request,*args,**kwargs):
        x=get_object_or_404(authorModel,id=kwargs['forid'])
        x.delete()

class deleteBook(APIView):
    def delete(self,request,*args,**kwargs):
        x=get_object_or_404(bookModel,id=kwargs['forid'])
        x.delete()


class getAllAuthorbooks(APIView):
    def get(self,request,*args,**kwargs):
        x=bookModel.objects.filter(author=kwargs['forid'])
        serializer=bookSerializer(x,many=True)
        return Response(serializer.data)