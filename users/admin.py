from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import UserToken

admin.site.register(UserToken, UserAdmin)
