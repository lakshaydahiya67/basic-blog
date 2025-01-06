# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogs, Signup_details
from django.contrib.auth.decorators import login_required   
# from django.contrib.auth import login
# Create your views here.
# @login_required
def post_list(request):
    posts = Blogs.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
# @login_required
def post_detail(request, post_id):
    post = get_object_or_404(Blogs, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
# @login_required
# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('post_list')
#     return render(request, 'blog/sign-up-page.html')
def signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email= request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cred1 = Signup_details(username=username, password=password, email=email, fullname=fullname)
        cred1.save()
        return render(request, "auth/login-form.html", {})
    return render(request, "auth/sign-up-page.html", {})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        cred1 = Signup_details.objects.filter(username=username, password=password)
        if cred1:
            return redirect('post_list')
        else:
            return render(request, "auth/login-form.html", {})
    return render(request, "auth/login-form.html", {})