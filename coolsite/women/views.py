from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from women.models import Women

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
# request обязательный параметр и ссылка на класс HttpRequest
# HttpResponse простое представление страницы (заглушка)
def index(request):
    posts = Women.objects.all()  # все данные с бд помещаем в переменную posts
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})  # путь указываем без папки потому что путь к папке уже прописан в настройках


def about(request):
    posts = Women.objects.all()
    return render(request, 'women/about.html', {'posts': posts, 'menu': menu, 'title': 'О сайте'})


def categories(request, cat):  # второй аргумент это числовой параметр
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>статьи по категориям</h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True)  # если год больше 2020, то перенаправит на главную страницу
        # raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

