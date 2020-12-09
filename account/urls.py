from . import views
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
app_name = 'account'
urlpatterns = [

    # path('login/',views.user_login,name='login'),
    path('login/',LoginView.as_view(template_name='account/login.html'),name = 'login'),
    # path('login/', LoginView.as_view(template_name='account/login.html'), name='login')
    path('logout/',LogoutView.as_view(template_name='account/logout.html'),name='logout')
]