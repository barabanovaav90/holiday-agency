from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Service, News, Portfolio
from .forms import ContactForm

def index(request):
    """Главная страница"""
    last_news = News.objects.all()[:3]
    return render(request, 'index.html', {'last_news': last_news})

def services_list(request):
    """Каталог услуг"""
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'services.html', context)

def service_detail(request, pk):
    """Детальная страница услуги"""
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

def portfolio_list(request):
    """Портфолио"""
    items = Portfolio.objects.all()
    context = {'items': items}
    return render(request, 'portfolio.html', context)

def portfolio_detail(request, pk):
    """Детальная страница проекта"""
    item = get_object_or_404(Portfolio, pk=pk)
    return render(request, 'portfolio_detail.html', {'item': item})

def news_list(request):
    """Список новостей"""
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news_list.html', context)

def news_detail(request, pk):
    """Детальная страница новости"""
    news_item = get_object_or_404(News, pk=pk)
    return render(request, 'news_detail.html', {'news_item': news_item})

def contacts(request):
    """Контакты и форма обратной связи"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')
            return redirect('contacts')
    else:
        form = ContactForm()
    
    return render(request, 'contacts.html', {'form': form})

def sitemap(request):
    """Карта сайта"""
    return render(request, 'sitemap.html')

def signup(request):
    """Регистрация нового пользователя"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Автоматический вход после регистрации
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def profile(request):
    """Личный кабинет пользователя"""
    return render(request, 'profile.html')

def toggle_accessibility(request):
    """Старый переключатель (можно оставить для совместимости или удалить)"""
    return set_accessibility_theme(request, 'bw')

def set_accessibility_theme(request, theme_name):
    """Установка конкретной темы: 'wb', 'bw', 'blue', 'normal'"""
    if theme_name == 'normal':
        request.session['accessibility_theme'] = None
        request.session['accessibility_mode'] = False
    elif theme_name in ['wb', 'bw', 'blue']:
        request.session['accessibility_theme'] = theme_name
        request.session['accessibility_mode'] = True
    
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def search(request):
    """Поиск по сайту"""
    query = request.GET.get('q')
    results = {
        'services': [],
        'news': [],
        'portfolio': []
    }
    
    if query:
        import re
        query_regex = re.escape(query)
        results['services'] = Service.objects.filter(
            Q(title__iregex=query_regex) | Q(description__iregex=query_regex) | Q(keywords__iregex=query_regex)
        )
        results['news'] = News.objects.filter(
            Q(title__iregex=query_regex) | Q(text__iregex=query_regex) | Q(keywords__iregex=query_regex)
        )
        results['portfolio'] = Portfolio.objects.filter(
            Q(title__iregex=query_regex) | Q(description__iregex=query_regex)
        )
        
    return render(request, 'search_results.html', {'query': query, 'results': results})

def custom_404(request, exception):
    """Кастомная страница 404"""
    return render(request, '404.html', status=404)
