from .views import frontpage_view
from django.urls import path
from django.contrib.auth  import views as auth_views 

from . import views



urlpatterns = [
    path('', frontpage_view, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    

    

]
