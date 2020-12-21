from django.shortcuts import render , get_list_or_404
from django.http import HttpResponse

from . models import post
# Create your views here.

def home(request):
    context = {
        'title': 'الصفحه الرئيسيه',
        'posts': post.objects.all(),
    }
    return render(request, 'blog/index.html', context)

def about(request):
    
    return render(request,'blog/about.html', {'title': 'من انا'}, )


def post_detail(request,post_id):
    Post = get_list_or_404(post, pk = post_id)
    context = {
        'title': 'الصفحه الرئيسيه',
        'post': Post,
        }
    return render(request,'blog/post_detail.html',context)