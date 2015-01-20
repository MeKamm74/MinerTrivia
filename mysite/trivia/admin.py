from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from trivia.models import Question, MyUser

admin.site.register(Question)


# Define an inline admin descriptor for MyUser model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'MyUser'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)