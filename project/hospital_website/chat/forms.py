from ckeditor.widgets import CKEditorWidget
from django import forms
class MailForm(forms.Form):
    email_reply=forms.CharField(max_length=255)
    subject=forms.CharField(max_length=255)
    content = forms.CharField(widget = CKEditorWidget())