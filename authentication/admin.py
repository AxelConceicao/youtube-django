from django.contrib import admin
from authentication.models import User
from django.contrib.auth.models import Group


# Register your models here.
class UserAdmin(admin.ModelAdmin):
  pass

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)