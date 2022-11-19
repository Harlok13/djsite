from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from women.forms import AddPostForm
from women.models import Women, Category




class WomenHome(ListView):
    model = Women  # создает коллекцию из этой модели
    template_name = 'women/index.html'  # переназначаем путь
    context_object_name = 'posts'  # меняет имя переменной с object_list на указанный нами
    # extra_context = {'title': 'Главная страница'}  # меняет заголовок. p.s. только для статических (неизменяемых) данных. списки задать не получится

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # обращаемся к базовому классу ListView и берем у него базовый контекст. этой функции мы передаем все именованные параметры
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)  # возвращает только опубликованные записи

def about(request):
    return render(request, 'women/about.html')


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            form.save()
                # Women.objects.create(**form.cleaned_data)  # для формы без привязки к бд
            return redirect('home')
            # except:
            #     form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'title': 'Добавление статьи', 'form': form})


def contact(request):
    # context['title'] = 'Обратная связь'
    return render(request, 'women/contact.html')


def login(request):
    return HttpResponse('')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {  # эти параметры мы передаем в html файл
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id  # номер рубрики с которой связана статья
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    """Категории"""
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()
    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id
    }
    return render(request, 'women/index.html', context=context)




# request обязательный параметр и ссылка на класс HttpRequest
# HttpResponse простое представление страницы (заглушка)

# def index(request):
#     posts = Women.objects.all()  # все данные с бд помещаем в переменную posts
#     context = {
#         'posts': posts,
#         'title': 'Главная страница',
#         'cat_selected': 0  # этот параметр нужно оставить, он используется не в теге
#     }
#     return render(request, 'women/index.html', context=context)  # путь указываем без папки потому что путь к папке
#     # уже прописан в настройках

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
