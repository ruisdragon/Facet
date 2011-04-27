from django.http import HttpResponse
from blog.models import Entry
from django.template import Context, loader
from django.shortcuts import render_to_response


def index(request,latest_post_num = 5):
    latest_entry_list = Entry.objects.all().order_by('-pub_date')\
    [:latest_post_num]
    t = loader.get_template('index.html')
    c = Context({
        'latest_entry_list': latest_entry_list,
    })
    
    return HttpResponse(t.render(c))


def blog(request):
    latest_blog_list = Entry.objects.filter(is_notepad=False).order_by('-pub_date')
    t = loader.get_template('blog.html')
    c = Context({
        'latest_blog_list': latest_blog_list,
    })
    
    return HttpResponse(t.render(c))


def notepad(request):
    latest_notepad_list = Entry.objects.filter(is_notepad=True).order_by('-pub_date')
    t = loader.get_template('notepad.html')
    c = Context({
        'latest_notepad_list': latest_notepad_list,
    })
    
    return HttpResponse(t.render(c))


def detail(request, pk_id):
    entry = Entry.objects.get(pk=pk_id)
    t = loader.get_template('detail.html')
    c = Context({
        'entry': entry,
    })
    
    return HttpResponse(t.render(c))

def about(request):
    return render_to_response("about.html")


