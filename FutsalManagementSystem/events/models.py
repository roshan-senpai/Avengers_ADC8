from django.db import models

# Create your models here.
# creating objects for table in database 
class Event(models.Model):
    event_name = models.CharField('Event Name',max_length=100)
    venue = models.CharField('Venue',max_length=100)
    event_date = models.DateField('Event Date')
    manager = models.CharField('Manager Name', max_length=100)

    def __str__(self):
        return str(self.id) + " " + self.event_name + " " + self.venue+ " " + str(self.event_date) + " " + self.manager