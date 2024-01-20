from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Users,Level
# Register your models here.

admin.site.register(Users)
admin.site.register(Level)
admin.site.unregister(User)
admin.site.unregister(Group) 