from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import io

from .models import Test_member
from .serializers import TestSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


#CRUD operation using ModelViewSet

class CRUD(viewsets.ModelViewSet):
    
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAdminUser]



"""

#CRUD operation using ListCreateAPIView and RetrieveUpdateDestroyAPIView

class list_create(ListCreateAPIView):
    
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer


class list_create(RetrieveUpdateDestroyAPIView):
    
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
"""    




"""

#CRUD operation using ModelMixin

class list_create(GenericAPIView, ListModelMixin, CreateModelMixin):
    
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class retrieve_update_destroy(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        
"""

            


"""

#Get all Model instances using ListModelMixin

class get_data(GenericAPIView, ListModelMixin):
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
        

#Create a Model instance using CreateModelMixin    
    
class create_data(GenericAPIView, CreateModelMixin):
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        

#Retrieve a Model instance using RetrieveModelMixin    
    
class retrieve_data(GenericAPIView, RetrieveModelMixin):
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    
#Update a Model instance using UpdateModelMixin
    
class update_data(GenericAPIView, UpdateModelMixin):
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    
#Delete a Model instance using DestroyModelMixin
    
class delete_data(GenericAPIView, DestroyModelMixin):
    queryset = Test_member.objects.all()
    serializer_class = TestSerializer
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
                       
"""        




"""

#Class based view APIView

class get_data(APIView):
    def get(self, request, pk=None, format=None):
        id = pk 
        if id is not None:
            ai = Test_member.objects.get(id=id)
            serializer = TestSerializer(ai)
            return Response(serializer.data)
        
        ai = Test_member.objects.all()
        serializer = TestSerializer(ai, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully Inserted Data'})
            
        return Response(serializer.errors)
    
    def put(self, request, pk, format=None):
        id = pk
        ai = Test_member.objects.get(id=id)
        serializer = TestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Full Data updated Successfully'})
        
        return Response(serializer.errors)
    
    
    def patch(self, request, pk, format=None):
        id = pk
        ai = Test_member.objects.get(id=id)
        serializer = TestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data updated Successfully'})
        
        return Response(serializer.errors)
    
    
    def delete(self, request, pk, format=None):
        id = pk
        ai = Test_member.objects.get(id=id)
        ai.delete()
        return Response({'msg' : 'Data Deleted Successfully'})
        
"""


    

"""

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

def get_data(request, pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            ai = Test_member.objects.get(id=id)
            serializer = TestSerializer(ai)
            return Response(serializer.data)
        
        ai = Test_member.objects.all()
        serializer = TestSerializer(ai, many=True)
        return Response(serializer.data)
    
    
    if request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Successfully Inserted Data'})
            
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        id = pk
        ai = Test_member.objects.get(id=id)
        serializer = TestSerializer(ai, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Full Data updated Successfully'})
        
        return Response(serializer.errors)
    
    
    if request.method == 'PATCH':
        id = pk
        ai = Test_member.objects.get(id=id)
        serializer = TestSerializer(ai, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Partial Data updated Successfully'})
        
        return Response(serializer.errors)
    
    
    if request.method == 'DELETE':
        id = pk
        ai = Test_member.objects.get(id=id)
        ai.delete()
        return Response({'msg' : 'Data Deleted Successfully'})

"""




"""

# Create your views here.
def test(request):
    return HttpResponse("Welcome to my Django Project")

#Serializer view
def test1(request):
    ai = Test_member.objects.all()
    ser = TestSerializer(ai, many=True)
    ren = JSONRenderer().render(ser.data)
    return HttpResponse(ren, content_type='application/json')


#DeSerializer view
@csrf_exempt
def test2(request):
    if request.method == 'POST':
     json_data = request.body
     
     #json to stream convert
     stream = io.BytesIO(json_data)
     
     #stream to python convert
     python_data = JSONParser().parse(stream)
     
     #python to complex data convert
     serializer = TestSerializer(data=python_data)
     
     if serializer.is_valid():
         serializer.save()
         res = {'msg':'Data Successfully Inserted'}
         in_data = JSONRenderer().render(res)
         return HttpResponse(in_data, content_type='application/json')
     
     error = JSONRenderer().render(serializer.errors)
     return HttpResponse(error, content_type='application/json')
 
    if request.method == 'PUT':
        json_data = request.body
        
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get(id)
        aiq = Test_member.objects.get(id=id)
        serializer = TestSerializer(aiq, data = python_data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Successfully Inserted'}
            in_data = JSONRenderer().render(res)
            return HttpResponse(in_data, content_type='application/json')
     
    error = JSONRenderer().render(serializer.errors)
    return HttpResponse(error, content_type='application/json')


    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get(id)
        aiq = Test_member.objects.get(id=id)
        aiq.delete()
        res = {'msg':'Data Successfully deleted'}
        in_data = JSONRenderer().render(res)
        return HttpResponse(in_data, content_type='application/json')
   
"""