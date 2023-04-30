from django.db import models

from datetime import datetime #lấy ngày giờ hiện tại

# Create your models here.
class Room(models.Model):
	name = models.CharField(max_length = 255)
class Messages(models.Model):
	value = models.CharField(max_length= 10000)
	date = models.DateTimeField(default = datetime.now, blank = True)
	user = models.CharField(max_length= 255)
	room = models.CharField(max_length= 255)


		