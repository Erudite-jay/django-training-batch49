from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileForm
from . models import FileFormUpload
# Create your views here.

def file_uploader(request):
    if request.method =="POST":
        form=FileForm(request.POST, request.FILES)
        print(request.POST)
        try:
            if form.is_valid():
                # file_upload=FileFormUpload(name=form.cleaned_data['name'],file=form.cleaned_data['file'])
                # file_upload.save()
                form.save()
                return JsonResponse({
                    "success": True,
                    "message": "File uploaded successfully"
                },status=200)
            else:
                return JsonResponse({
                    "success": False,
                    "message": form.errors.as_json(),    
                },status=400)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            },status=500)
           
    if request.method=="GET":
        form=FileForm()

    return render(request, 'Form_app/file.html', {'form': form})
        
