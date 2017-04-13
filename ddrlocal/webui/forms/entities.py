import logging
logger = logging.getLogger(__name__)

from django import forms
from django.conf import settings

class NewEntityForm(forms.Form):
    repo = forms.CharField(max_length=100)  # TODO should be disabled/non-editable
    org = forms.CharField(max_length=100)  # TODO should be disabled/non-editable
    cid = forms.IntegerField()  # TODO should be disabled/non-editabel
    eid = forms.IntegerField()

class JSONForm(forms.Form):
    json = forms.CharField(widget=forms.Textarea)

class UpdateForm(forms.Form):
    xml = forms.CharField(widget=forms.Textarea)

class DeleteEntityForm(forms.Form):
    confirmed = forms.BooleanField(help_text='Yes, I really want to delete this object.')

class RmDuplicatesForm(forms.Form):
    confirmed = forms.BooleanField(help_text='Yes, remove the duplicates.')
