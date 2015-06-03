from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from jobooker.models import Jobooker

class JobookerInline(admin.StackedInline):
    model = Jobooker
    can_delete = False
    verbose_name_plural = 'jobooker'

class UserAdmin(UserAdmin):
    inlines = (JobookerInline, )


admin.site.unregister(User)

admin.site.register(User, UserAdmin)


# Register your models here.
