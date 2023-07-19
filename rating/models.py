from django.db import models
from django.db.models import Avg
from django.contrib.auth import get_user_model

class Rate(models.Model):
    class Rate_option(models.IntegerChoices):
        ONE_STAR = 1
        TWO_STAR = 2
        THREE_STAR = 3
        FOUR_STAR = 4
        FIVE_STAR = 5
    

    class Meta:
        ordering = ['-date']
        
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    rating = models.IntegerField(choices=Rate_option.choices, blank=True, null=True)

class Estimate(models.Model):
   
    name = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    
    # ra_te = models.ManyToManyField(Rate, null=True, blank=True)
    ra_te = models.ManyToManyField(Rate)

    def get_avg_rate(self):
        return self.ra_te.all().aggregate(Avg('rating')).get('rating__avg', 1)
    
    def __str__(self) -> str:
        return f'{self.name} Рейтинг - {self.get_avg_rate()}'