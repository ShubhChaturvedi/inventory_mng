from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_id = models.AutoField(primary_key=True) 
    contact_number = models.CharField(max_length=10)
    image_key = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'user_profile'


