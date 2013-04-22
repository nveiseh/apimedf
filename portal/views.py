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