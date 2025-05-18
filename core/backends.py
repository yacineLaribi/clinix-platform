from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class TeamNameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(teamname=username)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
