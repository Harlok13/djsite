from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from women.models import Women

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Вход', 'url_name': 'login'},
]
# request обязательный параметр и ссылка на класс HttpRequest
# HttpResponse простое представление страницы (заглушка)
posts = Women.objects.all()  # все данные с бд помещаем в переменную posts
context = {
    'posts': posts,
    'menu': menu,
    'title': 'Главная страница'
}

def index(request):
    return render(request, 'women/index.html', context=context)  # путь указываем без папки потому что путь к папке
    # уже прописан в настройках


def about(request):
    context['title'] = 'О нас'
    return render(request, 'women/about.html', context=context)

def addpage(request):
    context['title'] = 'Добавить запись'
    return render(request, 'women/add_page.html', context=context)


def contact(request):
    # сontext['title'] = 'Обратная связь'
    return HttpResponse('')


def login(request):
    return HttpResponse('')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')







# def categories(request, cat):  # второй аргумент это числовой параметр
#     if request.GET:
#         print(request.GET)
#     return HttpResponse(f'<h1>статьи по категориям</h1><p>{cat}</p>')
#
#
# def archive(request, year):
#     if int(year) > 2020:
#         return redirect('/', permanent=True)  # если год больше 2020, то перенаправит на главную страницу
#         # raise Http404()
#     return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

