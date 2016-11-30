import logging
logger = logging.getLogger(__name__)
import os

from django import forms
from django.conf import settings

from DDR import docstore
from webui import set_docstore_index


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255)


def _index_choices( request, show_missing=False, default=None ):
    """
    @param request: 
    @param show_missing: 
    @param default: choice tuple or None
    """
    # current indices in Elasticsearch
    indices = []
    ds = docstore.Docstore()
    for index in ds.index_names():
        indices.append(index)
    if show_missing:
        # session index
        session_index = None
        if request:
            set_docstore_index(request)
            session_index = request.session.get('docstore_index', None)
            if session_index and (session_index not in indices):
                indices.append(session_index)
        # if current storage has no index
        storage_label = request.session.get('storage_label', None)
        if request and storage_label:
            if storage_label:
                store_index = docstore.make_index_name(storage_label)
                if store_index and (store_index not in indices):
                    indices.append(store_index)
    # make list of tuples for choices menu
    choices = [(index,index) for index in indices]
    if default:
        choices.insert(0, default)
    return choices

class IndexConfirmForm(forms.Form):
    index = forms.ChoiceField(choices=[])
    
    def __init__(self, *args, **kwargs):
        if kwargs.get('request', None):
            request = kwargs.pop('request')
        else:
            request = None
        super(IndexConfirmForm, self).__init__(*args, **kwargs)
        # add current index to list
        if request:
            self.fields['index'].choices = _index_choices(
                request, show_missing=True, default=('', 'Select an index'))

class DropConfirmForm(forms.Form):
    index = forms.ChoiceField(choices=[])
    confirm = forms.BooleanField(label=None, help_text='I really want to do this')
    
    def __init__(self, *args, **kwargs):
        if kwargs.get('request', None):
            request = kwargs.pop('request')
        else:
            request = None
        super(DropConfirmForm, self).__init__(*args, **kwargs)
        # add current index to list
        if request:
            self.fields['index'].choices = _index_choices(
                request, default=('', 'Select an index'))
