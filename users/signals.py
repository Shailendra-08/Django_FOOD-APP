from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save,sender=User)         #decoratoer which is used that these block need to have the permission to do that 
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)



@receiver(post_save,sender=User)         #decoratoer which is used that these block need to have the permission to do that 
def save_profile(sender,instance,**kwargs):
    instance.profile.save()