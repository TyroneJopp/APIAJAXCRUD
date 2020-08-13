from django.db import models

# Create your models here.
class Task(models.Model):               #This class will take models from the models import this class
    title = models.CharField(max_length=200) #A variable title will contain the title of the task
    completed = models.BooleanField(default=False, blank=True, null=True)   # Completed varaible with a T/F option

    def __str__(self):                  #function in the class which will return just the title 
        return self.title               #self object assigned from the titile variable

