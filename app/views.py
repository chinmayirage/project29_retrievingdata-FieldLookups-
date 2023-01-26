from django.shortcuts import render


# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def display_topics(request):
    QST=Topic.objects.all()
    QST=Topic.objects.filter(topic_name='cricket')
    d={'topics':QST}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='cricket')
    QSW=Webpage.objects.exclude(topic_name='cricket')
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='Kabaddi').order_by('-name')    
    QSW=Webpage.objects.all().order_by(Length('name'))    
    QSW=Webpage.objects.all().order_by(Length('name').desc())
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(url__startswith='http')
    QSW=Webpage.objects.filter(url__endswith='com')
    QSW=Webpage.objects.filter(name__startswith='m')
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(name__contains='u') 
    QSW=Webpage.objects.filter(name__regex='\w{3}')
    QSW=Webpage.objects.filter(name__in=['manu','meghana',])
    QSW=Webpage.objects.filter(Q(topic_name='cricket') | Q(name='manu'))
    QSW=Webpage.objects.filter(Q(topic_name='football') & Q(url__startswith='http'))
    d={'webpages':QSW}
    return render(request,'display_webpages.html',d)
    
def display_access(request):
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.all().order_by('date')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date='2023-01-10')    
    QSA=AccessRecords.objects.filter(date__gt='2023-01-6')    
    QSA=AccessRecords.objects.filter(date__gte='2023-01-10') 
    QSA=AccessRecords.objects.filter(date__lte='2023-01-15')
    QSA=AccessRecords.objects.all()
    QSA=AccessRecords.objects.filter(date__year='2023')  
    QSA=AccessRecords.objects.filter(date__month='1')    
    QSA=AccessRecords.objects.filter(date__day='6')   
    QSA=AccessRecords.objects.filter(date__year__gt='2022')
    
    d={'access':QSA}
    return render(request,'display_access.html',d)


