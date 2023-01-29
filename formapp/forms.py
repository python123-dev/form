from django.forms import ModelForm
from.models import customer

class customerform(ModelForm):
    class Meta:
        model=customer
        fields='__all__'