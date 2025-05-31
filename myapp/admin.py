from django.contrib import admin
from .models import User,CustomUserManager,Xulosa,Ertak,File,Item,Course

class ItemAdmin(admin.ModelAdmin):
    # Используем filter_horizontal для улучшенного интерфейса выбора
    filter_horizontal = ('courses',)  # Удобный интерфейс для выбора курсов

admin.site.register(Item, ItemAdmin)
admin.site.register(Course)

admin.site.register(User)
admin.site.register(Xulosa)
admin.site.register(Ertak)
admin.site.register(File)

