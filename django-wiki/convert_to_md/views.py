from wiki.plugins.attachments.views import AttachmentView
from .forms import NewAttachmentForm


class NewAttachmentView(AttachmentView):

    # template_name = "wiki/new_index_attachment.html"
    # form_class = NewAttachmentForm
    
    def get_form_class(self):
        return NewAttachmentForm
