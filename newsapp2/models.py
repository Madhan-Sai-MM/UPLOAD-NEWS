from django.db import models
import datetime

# Create your models here.
class first(models.TextChoices):
    SRIKAKULAM =  "SRIKAKULAM"
    VISHAKAPATNAM =  "VISHAKAPATNAM"
    VIZIANAGARAM =  "VIZIANAGARAM"
    EAST_GODAVARI =  "EAST-GODAVARI"
    WEST_GODAVARI =  "WEST-GODAVARI"
    KRISHNA = "KRISHNA"
    GUNTUR = "GUNTUR"
    PRAKASAM = "PRAKASAM"
    NELLORE = "NELLORE"
    KURNOOL = "KURNOOL"
    ANANTAPUR = "ANANTAPUR"
    KADAPA = "KADAPA"
    CHITTOOR = "CHITTOOR"  

class madhan(models.Model): 
    news = models.CharField(max_length=1000, null=False)
    add_image = models.ImageField(blank=False, null=True, upload_to="images/")
    video = models.FileField(blank=False, null=True, upload_to="videos/")
    status = models.CharField(null=False, verbose_name="Course", max_length=20,choices=first.choices)
    place = models.CharField(max_length=1000, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    

def __str__(self):
        return self.news
        madhan.objects.last()
        #madhan.objects.latest('created_on')
        #madhan.objects.values('created_on').annotate(latest_date=Max('date'))