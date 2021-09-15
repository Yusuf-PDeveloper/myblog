from django.shortcuts import render
from .models import Post
from django.views import generic

def home(request):
    return render(request, "home.html")


def cv(request):
    return render(request, "cv.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class DetailViw(generic.DetailView):
    model = Post
    template_name = 'post_details.html'