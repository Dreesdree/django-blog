from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    title_1 = 'hexlet_django_blog.article'
    return render(
        request,
        'articles/index.html',
        context={'title':title_1},
    )

