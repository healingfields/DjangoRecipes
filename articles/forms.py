from django import forms
from django.core.exceptions import ValidationError
from django.forms.forms import Form

from articles.models import Article

class ArticleFormNewerVersion(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content"]

    
    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs =  Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title",f"{title} already exists")
        return data


        


class ArticleFormOlderVersion(forms.Form):
    title = forms.CharField()
    content = forms.CharField()


    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned_data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "fight club":
    #         raise forms.ValidationError("this title is already taken  ")
    #     print(title)
    #     return title


    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")
        if title.lower().strip() == "fight club":
            self.add_error("title","this title is already taken")
        if "fight" in  content or "fight" in title.lower():
            self.add_error("content","fight cannot be in content or title")
            raise forms.ValidationError("fight is not allowed")
        return cleaned_data