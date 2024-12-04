from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from .models import Contact
from .serializers import ContactSerializer

import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def print_hello(request):
    return HttpResponse("Hello, world, this is django backend")

def home_page(request):
    return render(request, 'Auth_app/index.html')

def get_data(request):
    if request.method == 'GET':
        try:
            all_contact = Contact.objects.all() #queryset -> list of object
            serialized_data=ContactSerializer(all_contact,many=True) #serailized_data

            return JsonResponse(serialized_data.data,safe=False,status=200) 
        
        except Exception as e:
            return JsonResponse({"error": str(e)})

@csrf_exempt    
def save_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serialized_data = ContactSerializer(data=data)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse({"message": "Data saved successfully"}, status=200)
            else:
                return JsonResponse({"error": serialized_data.errors}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)})

@csrf_exempt
def single_user_data(request,pk):
    if request.method == 'GET':
        try:
            user = Contact.objects.get(id=pk) #object #queryset

            serialized_data = ContactSerializer(user) #serialized data
            return JsonResponse(serialized_data.data, status=200)
        except Contact.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)})
    
    if request.method=="PUT":
        try:
            user = Contact.objects.get(id=pk) #finding the user 
            input_data = json.loads(request.body) 
            serialized_data = ContactSerializer(user, data=input_data)
            if serialized_data.is_valid():
                serialized_data.save()
                return JsonResponse({"message": "Data updated successfully"}, status=200)
            else:
                return JsonResponse({"error": serialized_data.errors}, status=400)
        except Contact.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)})
        
    if request.method == 'PATCH':
        try:
            user = Contact.objects.get(id=pk) #finding the user 
            input_data = json.loads(request.body) 
            serialized_data=ContactSerializer(user,data=input_data,partial=True)

            if serialized_data.is_valid():
                serialized_data.save()
            return JsonResponse({"message": "Data updated successfully"}, status=200)
        
        except Contact.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)})

    if request.method == 'DELETE':
        try:
            user = Contact.objects.get(id=pk) #finding the user 
            user.delete()
            return JsonResponse({"message": "Data deleted successfully"}, status=204)
        except Contact.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)})