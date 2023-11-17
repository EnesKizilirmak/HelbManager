from django.shortcuts import render
from blog.models import Post

def chronology(request):
    context = {'posts': Post.objects.all()}

    return render(request, 'chronology/chronology.html', context)