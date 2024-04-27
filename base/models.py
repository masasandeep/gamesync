from django.db import models

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class BattleRoyale(models.Model):
    Game = models.ForeignKey(Games, on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=True,blank=True)
    player_id = models.CharField(max_length=50,null=True,blank=True)
    Level = models.IntegerField()
    Rank = models.CharField(max_length=150)
    kd_ratio = models.FloatField()
    headshot_rate = models.FloatField()
    no_of_headshots = models.IntegerField()
    top_3_ratio = models.FloatField()
    Avg_damage = models.FloatField()
    def __str__(self):
        return self.name


    