from django import forms


class AddCommentForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
