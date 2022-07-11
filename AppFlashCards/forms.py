# import form class from django
from django import forms
  
# import GeeksModel from models.py
from .models import Data
# create a ModelForm
class flashcardsform(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Data
        fields = [
            "question",
            "answer",
            "tag",
            "choice"
        ] 