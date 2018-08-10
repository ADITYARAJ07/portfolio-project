from django.db import models

class Qualification(models.Model):
	image=models.ImageField(upload_to='images')
	tittle=models.CharField(max_length=20)
	
def __str__(self):
	return self.tittle
