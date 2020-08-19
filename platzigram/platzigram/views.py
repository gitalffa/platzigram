"""platzigram views"""

#Django
from django.http import HttpResponse

#utilities
from datetime import datetime


def hello_world(request):

    return HttpResponse('!oh¡ hi, Currente server time is {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y %H:%M hrs')
        ))

def hi(request):
    """hi"""
    numbers = request.GET['numbers']
    return HttpResponse(str(numbers))
