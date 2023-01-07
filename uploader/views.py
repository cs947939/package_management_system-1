from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from .models import Document
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
     if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploader/main.html', {
            'uploaded_file_url': uploaded_file_url
        })
     documents = Document.objects.all()
     return render(request, 'uploader/main.html', { 'documents': documents })


  #  return render(request, 'uploader/uploading.html')
   
   

@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploader/uploading.html', {
            'uploaded_file_url': uploaded_file_url
        })


    return render(request, 'uploader/uploading.html')