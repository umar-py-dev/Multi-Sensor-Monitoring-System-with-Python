from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class AppUsers(models.Model):
    name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, default='viewer') # Roles may be: admin, accoountant, viewer
    created_at = models.DateTimeField(auto_now_add=True)
    
    # i must 'always' save password as hashed pass
    def save(self, *args, **kwargs):
        if self.password.startswith('pbkdf2_') == False:  # pehle se hashed to ni
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    
    
    def __str__(self):
        return self.name