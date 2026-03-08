from django.db import models
from django.utils.timezone import now
# Create your models here.
# debug_logs: Raw incoming JSON

class DebugLog(models.Model):
    # treat 'id' as Message ID
    topic = models.TextField()
    payload = models.TextField()
    response = models.TextField()
        
    created_at = models.DateTimeField(default=now)
    
    def __str__(self):
        return str(self.topic)
    
    
