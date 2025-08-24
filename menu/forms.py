from django import forms
from .models import Comment
from .models import Rating


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'fullname'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'comment'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'date'}),
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ["value"]
        widgets = {
            "value": forms.RadioSelect(choices=[(i, f"{i} ⭐") for i in range(1, 6)])
        }
