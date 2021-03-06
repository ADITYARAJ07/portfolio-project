from django.db import models

class Blog(models.Model):
	tittle=models.CharField(max_length=20)
	pub_date=models.DateTimeField()
	body=models.TextField()
	image=models.ImageField(upload_to='images')
	
	def __str__(self):
		return self.tittle
		
	def summary(self):
		return self.body[:100]
		
	def fancy_time(self):
		return self.pub_date.strftime('%b %e %Y')
	
	
