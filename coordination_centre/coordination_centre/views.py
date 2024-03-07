from django.shortcuts import render

from apps.news.models import News

from django.core.paginator import Paginator

def index(request):
    return render(request, 'index.html')

def news(request):
    news = News.objects.all().filter(visible=True).order_by('-created_at')

    paginator = Paginator(news, 10)
    pageNumber = request.GET.get('page')
    if pageNumber == None:
        pageNumber = 1
    pageObj = paginator.get_page(pageNumber)

    return render(request, 'news.html', {'news':pageObj})

def news_id(request, news_id):
    news = News.objects.filter(id=news_id).first()

    return render(request, 'news_id.html', {'news':news})