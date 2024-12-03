from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from .models import Contact
from .serializers import ContactSerializer
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