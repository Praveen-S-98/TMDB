from django.shortcuts import render
from django.http import HttpResponse
from .models import Movies
# Create your views here.


def index(request):
    return render(request, 'index.html')


def response(request):
    if request.method == 'GET':
        title = request.GET.get("title")
        try:
            temp_list = list(title)
            temp_list[0] = temp_list[0].upper()
            title = ''.join(temp_list)
            movie = Movies.objects.get(title=title)
            return render(request, 'response.html', {'movie': movie})
        except Movies.DoesNotExist:
            return render(request, 'not-found.html')
