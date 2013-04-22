#PACKAGES
from django.db import models
import datetime
from django.utils import timezone


#GLOBALS

#CLASSES
# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateField('Date Published')
    
    def __unicode__(self):
        return self.question
    
    def whatis_pub_date(self):
        return self.pub_date
    
    def was_published_recently(self):
        return True
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    #Makes the field and column specific to the display of this field of Poll, sexier
        #Broken line because of mismatch in data formats, from imported modules
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.choice_text
    
    def whatis_votes(self):
        return self.votes
    