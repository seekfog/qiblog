from . import views
from django.urls import path, include
app_name = 'blog'
urlpatterns = [

    path('title/',views.blog_title,name='blog_title'),
    path('title/<article_id>',views.blog_content,name='blog_content'),

]
