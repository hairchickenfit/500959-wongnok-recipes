from django.db import models
from django.urls import reverse

from base import models as base_models


class WongnokRecipe(models.Model):
    
    auto_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    image_address = models.TextField(blank=False, null=False)
    ingredient = models.TextField(blank=False, null=False)
    step = models.TextField(blank=False, null=False)
    duration = models.CharField(
        max_length=50,
        choices=(
            ('1) 5 to 10 minutes', '1) 5 to 10 minutes'),
            ('2) 11 to 30 minutes', '2) 11 to 30 minutes'),
            ('3) 31 to 60 minutes', '3) 31 to 60 minutes'),
            ('4) 60+ minutes', '4) 60+ minutes'),
        )
    )
    cooking_level = models.CharField(
        max_length=50,
        choices=(
            ('1) Rookie', '1) Rookie'),
            ('2) Beginner', '2) Beginner'),
            ('3) Amateur', '3) Amateur'),
            ('4) Pro', '4) Pro'),
            ('5) Master', '5) Master'),
            ('6) Legend', '6) Legend'),
        )
    )
    owner = models.ForeignKey(base_models.WongnokUser, on_delete=models.CASCADE)
    updated_timestamp = models.DateTimeField(blank=False, null=False)
    
    class Meta:
        verbose_name = 'wongnok recipe'
        verbose_name_plural = 'wongnok recipe(s)'
    
    def __str__(self):
        return str(self.auto_id)
    
    def get_absolute_url(self):
        return reverse(
            'wongnok_recipe_auto_id',
            kwargs={'pk': self.auto_id}
        )   

class RatingLog(models.Model):
    
    auto_id = models.BigAutoField(primary_key=True)
    rating = models.CharField(
        max_length=5,
        choices=(
            ('0.0', '0.0'),
            ('0.5', '0.5'),
            ('1.0', '1.0'),
            ('1.5', '1.5'),
            ('2.0', '2.0'),
            ('2.5', '2.5'),
            ('3.0', '3.0'),
            ('3.5', '3.5'),
            ('4.0', '4.0'),
            ('4.5', '4.5'),
            ('5.0', '5.0'),
        )
    )
    rated_recipe = models.ForeignKey(WongnokRecipe, on_delete=models.CASCADE)
    rater = models.ForeignKey(base_models.WongnokUser, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(blank=False, null=False)
    
    class Meta:
        verbose_name = 'rating log'
        verbose_name_plural = 'rating log(s)'
    
    def __str__(self):
        return str(self.auto_id)
    
    def get_absolute_url(self):
        return reverse(
            'rating_log_auto_id',
            kwargs={'pk': self.auto_id}
        ) 
