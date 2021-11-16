from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string,get_template


def home_view(request,*args,**kwargs):

    print(args,kwargs)
    name = "idriss"
    number = random.randint(10,100)
    # file = open("config/template.html","r")
    # string = file.read()
    obj = Article.objects.get(id=1)
    article_queryset = Article.objects.all()
    my_list = [10,50,14,656,86]
    # my_list_string = ""
    # for x in my_list :
    #     my_list_string += f"number is {x}/n"


    context = {
        "object_list":article_queryset,
        "obj":obj,
        "title":obj.title,
        "content":obj.content,
        "id":obj.id
        
    }
    
    html_String = """
        <h1>{title} (id : {id})</h1>
        <h3>{content}
        """.format(**context) 

    html_String2 = render_to_string("template.html",context=context)
    tmpl = get_template("template.html") 
    html_string3 = tmpl.render(context=context)

    return HttpResponse(html_string3)