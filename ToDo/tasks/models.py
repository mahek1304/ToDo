from django.db import models

class Task(models.Model):
    
    title = models.CharField(max_length = 200)
    complete = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)     #To know when each item is created, so we want it to auto add 
                                                            #thus auto_now_add = True (Thus everytime an item is created we need not
                                                            # set its value, it will be created by default)
    def __str__ (self):
        return self.title
