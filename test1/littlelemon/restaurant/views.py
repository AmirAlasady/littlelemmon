from django.shortcuts import render
from django.http import HttpResponse
from .serializers import MenuSerializer,BookingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Menu,Booking
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet  

# Create your views here.
def index(request):
    return render(request, 'index.html', {})
""""
@api_view(['GET','POST'])
def MenuItemsView(request):
      if request.method == 'GET':
        items = Menu.objects.all()
        serial = MenuSerializer(items,many=True)
        return Response(serial.data)
      if request.method == 'POST':
          serial=MenuSerializer(data=request.data)
          if serial.is_valid():
              serial.save()
              return Response(serial.data,status=status.HTTP_201_CREATED)
          return Response(status=status.HTTP_400_BAD_REQUEST)
"""""
class MenuItemsView(APIView):
    def get(self,request):
        items = Menu.objects.all()
        serializer=MenuSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer=MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

""""
@api_view(['GET','DELETE'])
def SingleMenuItemView(request,pk):
    try:
        item = Menu.objects.get(pk=pk)
        serial = MenuSerializer(item)
        return Response(serial.data)
    except item.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'DELETE':
        print('asdasdasdasdasdasdasd')
        item.delete()
        return response(status=204)
"""""
class SingleMenuItemView(APIView):
    def get(self,request,pk):
        try:
            item = Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(item)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            item = Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(item,data=request.data)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
     
    def patch(self,request,pk):
        try:
            item = Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = MenuSerializer(item,data=request.data,partial=True)   
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
        
    def delete(self,request,pk):
        try:
            item = Menu.objects.get(id=pk)
        except Menu.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    def get_queryset(self):
        tables = Booking.objects.all()
        return tables