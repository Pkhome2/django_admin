from django.contrib import admin
from .models import Advertisement

class Advertisements_admin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'auction', 'created_date', 'updated_date'] # здесь прописываем отображаемые поля БД
    list_filter = ['auction', 'created_at']  # добавляем возможность фильтрации
    actions = ['make_auction_as_false', 'make_auction_as_true'] # чтобы action работал, для него нужно создать функцию

    # добавляет разделение на подразделы при добавлении нового объекта
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']   # чтобы можно было сворачивать поле
        }),
    )
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)


admin.site.register(Advertisement, Advertisements_admin)

# Register your models here.
