from django import forms
from msgs.models import Msg

class MsgsForms(forms.ModelForm):
    msg_send = forms.CharField(label='Mensaje', widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-2'}), required=True)
    
    class Meta:
        model = Msg
        fields = '__all__'
