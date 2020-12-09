from django.shortcuts import render, get_object_or_404
from .models import BlogArticles
# Create your views here.
def blog_title(request):
    blogs = BlogArticles.objects.all()

    print( blogs)
    # return render(request,'blog/titles.html',{'blogs':blogs})
    return render(request,'blog/title.html',locals())
def blog_content(request, article_id):

    #article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    publish = article.publish
    return render(request,'blog/content.html',{'article':article,'publish':publish,})