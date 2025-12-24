from django.contrib import admin
from .models import Service, News, Portfolio, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)
