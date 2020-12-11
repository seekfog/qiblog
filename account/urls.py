from . import views
from django.urls import path, include,reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
app_name = 'account'
urlpatterns = [

    # path('login/',views.user_login,name='login'),
    path('login/',LoginView.as_view(template_name='account/login.html'),name = 'login'),
    # path('login/', LoginView.as_view(template_name='account/login.html'), name='login')
    path('logout/',LogoutView.as_view(template_name='account/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    # path('password-change/',views.hello,name='password_change'),
    path('change/',PasswordChangeView.as_view(template_name='registration/password_change_form.html',success_url=reverse_lazy('account:password_change_done')),name='password_change'),
    path('change-done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='password_change_done'),

]