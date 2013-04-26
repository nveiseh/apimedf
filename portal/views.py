# Create your views here.
#MODULES
from django.http import HttpResponse, Http404

#from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from portal.models import Poll, Choice
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


#This is for the homepage, ie INDEX, and if you type nothing after 0.0.0.0:8000/portal
def index(request):
    #Basic response:  return HttpResponse("Hello, world. You're at the poll index.")
    #More sophisticated with HTTPResponse, Context and loader
    '''
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = Context({
        'latest_poll_list': latest_poll_list,
    })
    return HttpResponse(template.render(context))
    '''
    #BEST SHORTCUT is with render
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    #Render takes (request, the template location, context DICTIONARY we give to the template)
    return render(request, 'polls/index.html', context)


def detail(request, poll_id):
    #BEST SHORTCUT, instead of try-ing to catch the exception.
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

    
    '''
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})
    '''
    #return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})
    #return HttpResponse("You're looking at the results of poll %s." % poll_id)


def vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('portal:results', args=(p.id,)))

def fin_vote(request, poll_id):
    #return HttpResponse("You're voting on poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        #This is where we add the new data to each field
        
        
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('portal:results', args=(p.id,)))    

def csv_view(request, poll_id):
    '''
    To access this view: 0.0.0.0:8000/portal/1/csv_view
    Through the portal app.
    Addressing poll_id = 1
    And want to download the CSV view.
    
    The Question is now, what information can/need extract given the poll_id
    is the poll_id = enterprise_id, or is it = report_id?
    TRY:
    poll_id = enterprise_info...
    choices = periodic financial reports
    '''
    import csv
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="MEDFClient001.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response