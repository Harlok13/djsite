from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# request обязательный параметр и ссылка на класс HttpRequest
# HttpResponse простое представление страницы (заглушка)
def index(request):
    return render(request, 'women/index.html')  # путь указываем без папки потому что путь к папке уже прописан в настройках

def categories(request, cat):  # второй аргумент это числовой параметр
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>статьи по категориям</h1><p>{cat}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('/', permanent=True)
        # raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>{year}</p>')

# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Страница не найдена</h1>')

