from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from news.models import News


def news(request):
    newsList = News.objects.all().order_by('-dateTime')

    per_page = 12
    paginator = Paginator(newsList, per_page)

    page_number = request.GET.get('page')
    try:
        pageObj = paginator.page(page_number)
    except PageNotAnInteger:
        pageObj = paginator.page(1)
    except EmptyPage:
        pageObj = paginator.page(paginator.num_pages)

    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Новости', 'url': '/news/'},
    ]

    context = {
        'css_file': 'news/css/styleNews.css',
        'js_file': 'news/js/scriptsNews.css',
        'title': 'Новости',
        'newsList': pageObj,  # Передаем объект страницы вместо всего списка новостей
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'news/news.html', context)


def newsPage(request, news_id):
    # newsList = News.objects.all().order_by('-dateTime')
    newsPageList = News.objects.get(id=news_id)

    # per_page = 1
    # paginator = Paginator(newsList, per_page)

    # page_number = request.GET.get('page')
    # try:
    #     pageObj = paginator.page(page_number)
    # except PageNotAnInteger:
    #     pageObj = paginator.page(1)
    # except EmptyPage:
    #     pageObj = paginator.page(paginator.num_pages)

    breadcrumbs = [
        {'text': 'Главная', 'url': '/'},
        {'text': 'Новости', 'url': '/news/'},
        {'text': News.objects.get(id=news_id), 'url': '/news/' + str(news_id) + '/'},
    ]

    context = {
        'css_file': 'newsPage/css/styleNewsPage.css',
        'js_file': 'newsPage/js/scriptsNewsPage.css',
        'title': 'Новости',
        'newsPageList': newsPageList,
        'breadcrumbs': breadcrumbs,
    }
    return render(request, 'news/newsPage.html', context)
