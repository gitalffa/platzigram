"""platzigram views"""

#Django
from django.http import HttpResponse

#utilities
from datetime import datetime
import json 


def hello_world(request):

    return HttpResponse('!oh¡ hi, Currente server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y %H:%M hrs')
        ))

def sort_integers(request):
    """return a JOSN response with sorted integers."""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb;pdb.set_trace()
    data ={
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted succesfully.'
    }
    return HttpResponse(
        json.dumps(data,indent=4),
        content_type='application/json'
        )


def say_hi(request,name,age):
    """return a greeting"""
    if age < 12:
        message = 'Sorry {},you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to platzogram'.format(name)
    return HttpResponse(message)