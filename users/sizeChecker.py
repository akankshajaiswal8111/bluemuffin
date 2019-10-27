from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class SizeRestrictedFileField(FileField):
    def __init__(self):
        self.max_upload_size = settings.MAX_UPLOAD_SIZE
    def clean(self):
        data = super(SizeRestrictedFileField, self).clean()
        file = data.file
        try:
             if file._size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
        except AttributeError:
            pass

        return data
