""" Posts views"""
#Django
#from django.http import HttpResponse
from django.shortcuts import render

#utilities
from datetime import datetime

# Create your views here

posts =[
    {
        'title' : 'Mont Blac',
        'user': {
            'name':'Yesica Cortes',
            'picture':'https://picsum.photos/60/60/?image=1027',
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=1036',
    },
    {
        'title' : 'Via Lactea',
        'user': {
            'name':'Cristian Van der Henst',
            'picture':'https://picsum.photos/60/60/?image=1005',
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=903',
    },
    {
        'title' : 'Nuevo Auditorio',
        'user': {
            'name':'Uriel',
            'picture':'https://picsum.photos/60/60/?image=883',
        },
        'timestamp':datetime.now().strftime('%b %dth, %Y %H:%M hrs'),
        'photo':'https://picsum.photos/200/200/?image=1076',
    },
    
]

def list_posts(request):
    """List existing posts"""
    # content =[]
    # for post in posts:
    #     content.append("""
    #         <p><strong>{name}</strong></p>
    #         <p><small>{user} - <i>{timestamp}</i></small></p>
    #         <figure><img src="{picture}"/></figure>
    #     """.format(**post)
    #     )
    # return HttpResponse('<br>'.join(content))
    return render(request,'feed.html',{'posts':posts})