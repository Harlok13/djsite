from django.http import HttpResponse, Http404
from django.shortcuts import render
from women.models import Women, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Вход', 'url_name': 'login'},
]
# request обязательный параметр и ссылка на класс HttpRequest
# HttpResponse простое представление страницы (заглушка)


def index(request):
    posts = Women.objects.all()  # все данные с бд помещаем в переменную posts
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0
    }
    return render(request, 'women/index.html', context=context)  # путь указываем без папки потому что путь к папке
    # уже прописан в настройках


def about(request):
    return render(request, 'women/about.html')


def addpage(request):
    return render(request, 'women/add_page.html')


def contact(request):
    # context['title'] = 'Обратная связь'
    return HttpResponse('')


def login(request):
    return HttpResponse('')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def show_category(request, cat_id):
    """Категории"""
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам ',
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)







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
