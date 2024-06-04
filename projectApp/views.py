from django.shortcuts import render
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from .serializer import *
from .models import *

# Create your views here.

class projectDetailsViewset(viewsets.ModelViewSet):

    # CREATE METHODE    :
    def createData(self, request):
        try:
            data = request.data
            serializer=projectDataSerializers(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'data has been successfuly Added.', 'payload': serializer.data})
            return JsonResponse({'message': 'data is not valid.','errors':serializer.errors})
        except Exception as ex:
            return JsonResponse({'message':f'somthing went wrong. {ex}'})
        


    # UPDATE METHOD   :
    def updateData(self,request):
        try:
            data=request.data
            obj=projectModel.objects.get(id=data.get('id'))
            serializer=projectDataSerializers(obj,data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'data has been successfuly Updated.', 'payload': serializer.data})
            return JsonResponse({'message': 'data is not valid.','errors':serializer.errors})
            
        except Exception as ex:
            return JsonResponse({'message':f'somthing went wrong. {ex}'})

    # DELETE METHOD CREATE HERE  :
    def deleteData(self, request):
        try:
            data=request.data
            if data.get('id') is not None:
                obj=projectModel.objects.get(id=data.get('id'))
                obj.delete()
                return JsonResponse({'message': 'data has been successfuly Deleted.','payload':data})
            
            return JsonResponse({'message': 'data is not valid.'})
        
        except Exception as ex:

            return JsonResponse({'message':f'somthing went wrong. {ex}'})

    # VIEW MODEL  :
    def viewData(self, request):
        try:
            data=request.data
            if data.get('id') is not None:
                obj = projectModel.objects.get(id=data.get('id'))
                serializers = projectDataSerializers(obj,many=True)
    
                return JsonResponse({'message': 'data has been fatched successfuly .','payload':serializers.data})
            
            else:
                objs = projectModel.objects.filter('id')
                serializers = projectDataSerializers(objs)

                return JsonResponse({'message':'ok','payload':serializers.data})
               


            
            #return JsonResponse({'message': 'data is not valid.','errors':serializer.errors})
        
        except Exception as ex:
            

            return JsonResponse({'message':f'somthing went wrong. {ex}'})
    
    # LISTDATA MODEl :
    def listData(self,request):
        try:
            data=request.data
            if data.get('id') is not None:
                obj=projectModel.objects.get(id=data.get('id'))
                serializers=projectDataSerializers(obj)
                return JsonResponse({'message': 'All thedata has been fatched successfuly .', 'payload': serializers.data})
            else:
                objs = projectModel.objects.filter('id')
                serializers = projectDataSerializers(objs)
                return JsonResponse({'message': 'All thedata has been fatched successfuly .', 'payload': serializers.data})

            #return JsonResponse({'message': 'data is not valid.','errors':serializers.errors})
        
        except Exception as ex:

            return JsonResponse({'message':f'somthing went wrong. {ex}'})
        




            


            



