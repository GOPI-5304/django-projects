from django.shortcuts import render
from .models import Movie
from .serializers import Movieserializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

# Create your views here.
@api_view(['GET','POST'])
def movie_Name(request):
    if request.method == "GET":
        films = Movie.objects.all()
        s=Movieserializers(films, many=True)
        return JsonResponse(s.data, safe=False)
    if request.method == "POST":
        se=Movieserializers(data=request.data)
        if se.is_valid():
            se.save()
            return Response(se.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def movie_details(request,id):
    try:
        film = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
        return Response (status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        ser=Movieserializers(film)
        return JsonResponse(ser.data)
    elif request.method == "PUT":
        seri=Movieserializers(film,data=request.data)
        if seri.is_valid():
            seri.save()
            return Response(seri.data)
        return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    