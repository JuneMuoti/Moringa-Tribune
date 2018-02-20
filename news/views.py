from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')

def news_today(request):
    date =dt.date.today()
    return render(request,'all-news/today-news.html',{"date":date,})

def past_days_news(request,past_date):
    try:
        date=dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_today)
    return render(request,'all-news/past-news.html',{"date":date})
