from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    description = models.TextField()
    text = models.TextField()
    image = models.ImageField(upload_to='news/')
    visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.id
    
    def __str__(self):
        return str(self.id)
