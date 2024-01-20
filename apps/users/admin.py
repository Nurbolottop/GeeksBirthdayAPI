from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Users,Gender
# Register your models here.

admin.site.register(Users)
admin.site.register(Gender)
admin.site.unregister(User)
admin.site.unregister(Group) 