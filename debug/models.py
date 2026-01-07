from django.db import models
from django.utils import timezone
# Create your models here.
# debug_logs: Raw incoming JSON

class DebugLog(models.Model):
    log_type = models.CharField(max_length=30)
    message = models.TextField()
    
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.log_type)
    
    
