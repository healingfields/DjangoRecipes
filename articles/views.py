from django.contrib.auth import login
from django.shortcuts import render
from .models import Article
from .forms import ArticleFormNewerVersion

from django.contrib.auth.decorators import login_required
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

# @login_required
# def article_create_view(request):
#     #print(request.POST)
#     form = ArticleForm()
#     print(dir(form))
#     context={
#         "form":form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context["form"]=forms
#         if form.is_valid():
#             title = form.cleaned_data.get("title") 
#             content = form.cleaned_data.get("content")
#             created_object = Article.objects.create(title=title,content=content)
#             context['object']=created_object
#             context['created'] = True
#     return render(request,"articles/create.html",context=context)


@login_required
def article_create_view(request):
    #print(request.POST)
    form = ArticleFormNewerVersion(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        created_object = form.save()
        context["form"]=ArticleFormNewerVersion( )
        # title = form.cleaned_data.get("title") 
        # content = form.cleaned_data.get("content")
        # created_object = Article.objects.create(title=title,content=content)
        # context['object']=created_object
        # context['created'] = True
    return render(request,"articles/create.html",context=context)