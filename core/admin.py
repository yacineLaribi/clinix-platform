from django.contrib import admin
from .models import CustomUser, Challenge, Hint, Submission , UserHint
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Challenge)
admin.site.register(Hint)
admin.site.register(Submission)
admin.site.register(UserHint)
