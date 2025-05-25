from django.contrib import admin
from .models import CustomUser, Challenge, Hint, Submission , UserHint
# Register your models here.

admin.site.register(CustomUser)
@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_filter = ('is_visible','author')  # Replace with actual fields to filter by
# Removed redundant registration of Challenge model
admin.site.register(Hint)
admin.site.register(Submission)
admin.site.register(UserHint)
