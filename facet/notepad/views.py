from django.http import HttpResponse
from notepad.models import Entry
from django.template import Context, loader


def index(request,latest_post_num = 5):
    latest_entry_list = Entry.objects.all().order_by('-pub_date')\
    [:latest_post_num]
    t = loader.get_template('index.html')
    c = Context({
        'latest_entry_list': latest_entry_list,
    })
    
    return HttpResponse(t.render(c))
