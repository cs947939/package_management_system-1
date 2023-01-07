from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import File



def main(request):
    Files = File.objects.all()
    return render(request, 'Uploads/main.html', { 'files': files})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploads/uploader.html', {
            'uploaded_file_url': uploaded_file_url
        })

   
    return render(request, 'Uploads/uploader.html')


# Create your views here.
