from django.db import models
from django.db.models import fields
from .models import Details
from django.forms import ModelForm

class HeartForm(ModelForm):
    class Meta:
        model = Details
        fields = '__all__'