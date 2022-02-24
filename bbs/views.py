from django.shortcuts import render
from bbs.models import Board

# Create your views here.

def b_list(request):
    posts = Board.objects.all().order_by('-id')
    context = {
        'posts': posts
    }

    return render(request, 'list.html', context)