from django.shortcuts import render
from .models import Article
# Create your views here.

def article_detail_view(request,id=None):
    article_obj = None 
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object":article_obj
    }
    return render(request,"articles/detail.html",context=context)


def article_search_view(request):

    #print(dir(request))
    #print(request.GET)

    article_obj = None
    query_dict = request.GET
  #  print(dir(query_dict))  
   # query = query_dict.get("query")#<input type="text" name="query"/>
    try : 
        query = query_dict.get("query")
    except :
        query = None
    if query is not None:
        #print("+++++++++++++++++++++++++++++++",query)
        article_obj = Article.objects.get(id=query)
    context = {
        "object":article_obj
    }
    return render(request,"articles/search.html",context=context)

def article_create_view(request):
    #print(request.POST)
    context={}
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title,content)
        created_object = Article.objects.create(title=title,content=content)
        context['object']=created_object
        context['created'] = True
    return render(request,"articles/create.html",context=context)
