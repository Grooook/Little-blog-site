from articles.models import Article
from django import forms

class AddArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-lg',
            'type':'text', 
            'name': 'title',
            'placeholder':'Enter the title'
            }))

    text = forms.CharField(widget=forms.Textarea(
        attrs=
        {
            'class':'form-control form-control-lg',
            'placeholder':'Enter the text of article'
            }))
    
    class Meta:
        model = Article
        fields = ['title','text',]
       
