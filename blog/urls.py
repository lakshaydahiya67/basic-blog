from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('login/', auth_views.LoginView.as_view(template_name='auth/login-form.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('', views.login, name='login'),    
]