from django import forms
from .models import ManuBsn, ManuAccount

class ManuBsnForm(forms.ModelForm):
    class Meta:
        model = ManuBsn
        fields = ['img_url', 'bsn_name', 'reg_no', 'ceo_name', 'user']

class ManuAccountForm(forms.ModelForm):
    class Meta:
        model = ManuAccount
        fields = ['img_url', 'bank_name', 'account_no', 'user']
