from django.db import models

# Create your models here.
class AvailablePoints(models.Model):
    availablepoints = models.FloatField(default=0)

    def __str__(self):
        return f"{self.availablepoints}"




class TrackingHistory(models.Model):
    available_points = models.ForeignKey(AvailablePoints,on_delete=models.CASCADE)
    points = models.FloatField()
    points_type = models.CharField(choices=(('GIVE','GIVE'),('TAKE','TAKE')),max_length=100)
    appreciation = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"The points are {self.points} for {self.appreciation} type is {self.points_type}"