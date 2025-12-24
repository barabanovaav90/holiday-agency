from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('services/', views.services_list, name='services'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('portfolio/', views.portfolio_list, name='portfolio'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('news/', views.news_list, name='news'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('sitemap/', views.sitemap, name='sitemap'),
    path('search/', views.search, name='search'),
    
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('accessibility/toggle/', views.toggle_accessibility, name='toggle_accessibility'),
    path('accessibility/set/<str:theme_name>/', views.set_accessibility_theme, name='set_theme'),
]
