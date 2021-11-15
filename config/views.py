from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string,get_template


def home_view(request):

   
    name = "idriss"
    number = random.randint(10,100)
    # file = open("config/template.html","r")
    # string = file.read()
    obj = Article.objects.get(id=1)
    context = {
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