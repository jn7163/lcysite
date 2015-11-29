from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Author,Passage,Reply
from django.template import RequestContext,loader
from django.core.urlresolvers import reverse
from django.http import Http404
from django.utils import timezone
from .forms import NewReplyForm

# Create your views here.

def index(request):
    passages=Passage.objects.order_by('time')[:10]
    context={
        'passages':passages,        
    }
    return render(request,'blog/index.html',context)

def passages(request,passage_page):
    passage_page=int(passage_page)
    passages=Passage.objects.order_by("time").reverse()[passage_page*10:(passage_page+1)*10]
    context={
        'passages':passages,    
        'passage_page':passage_page,
    }
    return render(request,'blog/passages.html',context)

def passage(request,passage_id):
    try:
        passage=Passage.objects.get(id=passage_id)   
    except Passage.DoesNotExist:
        raise Http404("can't find the passage ")
    try:
        reply=passage.reply_set.all()
        context={'the_passage':passage,
             'reply':reply,
        }        
    except:
        context={'the_passage':passage,}   
    return render(request,'blog/passage.html',context)
    
    

def author(request,author_name):
    try:
        author=Author.objects.get(name=author_name)
    except Author.DoesNotExist:
        raise Http404("can't find the author")
    context={
        'author':author,    
    }
    return render(request,'blog/author.html',context)
    

    
def newpassage(request):
    p=Passage(title=str(request.POST['title']),body=str(request.POST['body']))    
    #//newtitle=p.title.get(pk=request.POST['title'])   
    p.save()
def replys(request,passage_id):
    context={
        'passage_id':passage_id,        
    }
    return render(request,'blog/replys.html',context)
    
def get_new_reply(request,passage_id):
    newname=request.POST.get('name')
    newbody=request.POST.get('body')
    newinpassage=Passage.objects.get(id=passage_id)
    newreply=Reply(name=newname,body=newbody,time=timezone.now(),inpassage=newinpassage) 
    try:
        oldreply=Reply.objects.get(name=newname,body=newbody,inpassage=newinpassage)
        oldreply.time=timezone.now()
                
    except:
        newreply.save()
    #pid=request.POST.get('passage')
    context={'passage_id':passage_id, 
            }        
    return render(request,'blog/get_new_reply.html',context)
   # return HttpResponseRedirect(reverse('passage',pid))
    # return HttpResponseRedirect(reverse('passage',args=(passage_id=pid,)))
    
        
    