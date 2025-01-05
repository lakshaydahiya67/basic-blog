from django.shortcuts import render, get_object_or_404
from .models import Blogs   
# Create your views here.
def post_list(request):
    posts = Blogs.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, post_id):
    post = get_object_or_404(Blogs, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})