# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Submission

@receiver(pre_save, sender=Submission)
def update_points_on_correct_submission(sender, instance, **kwargs):
    if not instance.pk:
        return  # new submission, not an update

    old = Submission.objects.get(pk=instance.pk)
    
    if not old.is_correct and instance.is_correct:
        instance.user.score += old.challenge.points 
        instance.user.save()

    if  old.is_correct and not instance.is_correct:
        instance.user.score -= old.challenge.points 
        instance.user.save()


