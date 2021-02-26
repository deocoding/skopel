from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Pengajar

def profil_pengajar(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name="pengajar")
        instance.groups.add(group)

        Pengajar.objects.create(
            user=instance,
            nama=instance.username
        )

post_save.connect(profil_pengajar, sender=User)