from wiki.plugins.attachments.forms import AttachmentForm
from django import forms
from django.utils.translation import gettext_lazy as _
from converters.base_converter import docx_to_markdown_io
from wiki.models import ArticleRevision

class NewAttachmentForm(AttachmentForm):
    
    to_convert = forms.BooleanField(label=_("Convert docx to article"),
        help_text=_("Convert docx to article?"),
        required=True,)
    
    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        file = self.cleaned_data["file"]
        to_convert = self.cleaned_data["to_convert"]
        filename = file.name
        if not to_convert:
            return result
        if 'doc' in filename.split('.')[-1]:
            article = self.article
            markdown = docx_to_markdown_io(file, article_obj=article)
            revision = ArticleRevision()
            revision.set_from_request(self.request)
            revision.inherit_predecessor(article)
            revision.content = markdown
            article.add_revision(revision, save=True)
        return result