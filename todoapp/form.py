from django import forms
from django .forms import ModelForm
from.models import Todo


class PostForm(ModelForm):
    class Meta:
        model =Todo
        fields ='__all__'