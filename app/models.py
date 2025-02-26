from django.db import models

# Create your models here.



class Referral(models.Model):
    referrer_name = models.CharField(max_length=255)
    referrer_email = models.EmailField()
    referee_name = models.CharField(max_length=255)
    referee_email = models.EmailField()
    course_name = models.CharField(max_length=255)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer_name} referred {self.referee_name}"

