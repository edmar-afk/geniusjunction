from django.shortcuts import render
from .models import Files
# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def files_section(request):
    files = Files.objects.all().order_by('id')
    
    context = {
        'files' : files
    }
    
    return render(request, 'files_section.html', context)


def admin(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        subtitle = request.POST['subtitle']
        file_type = request.FILES['files']
        type = request.POST['type']
        
        new_file = Files(title=title, subtitle=subtitle, files=file_type, type=type)
        new_file.save()
        
    return render(request, 'admin.html')