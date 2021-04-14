from django.contrib import admin

from django.contrib.auth import get_user_model  #to avoid Django potentially getting the wrong user model, this function is run.

User = get_user_model()

admin.site.register(User)
