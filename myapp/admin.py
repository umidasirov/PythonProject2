from django.contrib import admin
from .models import User,CustomUserManager,Xulosa,Ertak,File,Course,Item

admin.site.register(User)
admin.site.register(Xulosa)
admin.site.register(Ertak)
admin.site.register(File)
admin.site.register(Item)
admin.site.register(Course)
