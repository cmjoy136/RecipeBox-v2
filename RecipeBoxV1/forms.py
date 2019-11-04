from django import forms
from RecipeBoxV1.models import RecipeItem


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.Charfield(widget=forms.Textarea)


class RecipeItemAddForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = [
            'author',
            'title',
            'body',
            'time_required',
            'instructions'
        ]
