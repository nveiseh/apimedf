#PACKAGES
from django.db import models
from django.utils import timezone
import datetime



#GLOBALS

#CLASSES
# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('Date Published')
    
    def __unicode__(self):
        return self.question
    
    def whatis_pub_date(self):
        return self.pub_date
    
    def was_published_recently(self):
        now = timezone.now()
        return now > self.pub_date >= now - datetime.timedelta(days = 1)
        #return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)
    
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    #Makes the field and column specific to the display of this field of Poll, sexier
        #Broken line because of mismatch in data formats, from imported modules
        #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    #EXTENTIONS: poll_id will refer to the id number of the enterprise
    #Define variables within the class, that are unique to each Enterprise object, ie company
    ent_name = models.CharField(max_length = 200)
    inst_date = models.DateTimeField('Date of Instantation with MEDF')
    country = models.CharField(max_length = 100)
    country_code = models.CharField(max_length = 3)
    manager = models.CharField(max_length = 100)
    address = models.CharField(max_length = 200)
    biz_type = models.CharField(max_length = 100)
    biz_code = models.IntegerField(default = 0 )
    
    #Define Functions to return parts of object when called
    def get_country(self):
        return self.country
    
    def get_country_code(self):
        return self.country_code
    
    def get_manager(self):
        return self.manager
    
    def get_address(self):
        return self.address
    
    def get_biz_address(self):
        return self.biz_type
    
    def get_biz_code(self):
        return self.biz_code

    
    
class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default = 0)
    
    def __unicode__(self):
        return self.choice_text
    
    def whatis_votes(self):
        return self.votes
    
    #EXTENTIONS: poll_id will refer to the id number of the enterprise
    booking_date = models.DateTimeField('Date when Book Entry made with MEDF')
    
    revenue = models.FloatField()
    cogs = models.FloatField()
    depreciation = models.FloatField()
    interestpaidondebt = models.FloatField()
    interestearnedoncash = models.FloatField()
    profitbeforetax = models.FloatField()
    taxes = models.FloatField()
    profitaftertax = models.FloatField()
    dividends = models.FloatField()
    retainedearnings = models.FloatField()
    
    totalinventory = models.FloatField()
    totalwagespaid = models.FloatField()
    gacostspaid = models.FloatField()
    employeecount = models.IntegerField()
    transactioncount = models.IntegerField()
    