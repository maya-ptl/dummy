from django.contrib import admin
from .models import *

#admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Comment_Like)
admin.site.register(Like)
# admin.site.register()
class UserModel_Admin(admin.ModelAdmin):
  list_display = ['username','bio','first_name']
admin.site.register(UserProfile,UserModel_Admin)


