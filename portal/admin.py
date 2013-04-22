#admin.py dicates the representation of this app in the administrative settings

#Most basic things to include
from django.contrib import admin
from portal.models import Poll
from portal.models import Choice

#1. most basic representation in admin page
'''
#admin.site.register(Poll)
'''

#2. next most sophisticated representation
'''
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
'''

#3. a representation that can handle many more fields in an elegant way
#4. A more flexible way of representing with collapsable 
'''
class PollAdmin(admin.ModelAdmin):
    #First element in fieldset is TITLE, then the field itself
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Poll, PollAdmin)
'''


#5. Nested Poll AND Choice Data, represented together
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    
    #Add specific macro features, like display, what to filter by, and what to search by
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)

