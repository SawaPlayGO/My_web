from django.contrib import admin
from .models import Marmelad_order

class app_lesson_4Admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date']
    list_filter = ['auction', 'created_at']
    actions = ['false_auction', 'make_auction_true']  # Обратите внимание на название метода

    @admin.action(description='Выключить все торги')
    def false_auction(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Включить все торги')
    def make_auction_true(self, request, queryset):  # Измените название метода
        queryset.update(auction=True)

admin.site.register(Marmelad_order, app_lesson_4Admin)
