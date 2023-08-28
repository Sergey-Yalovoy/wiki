from mammoth import convert_to_html
from markdownify import MarkdownConverter
import base64
from wiki.plugins.images.models import ImageRevision, Image
from wiki.models import Article
import io
from django.core.files.images import ImageFile
from wiki.plugins.images.forms import SidebarForm 

def docx_to_html(path: str) -> str:
    """A function that converts a WORD document to a html string

    Args:
        path (str): path to file

    Returns:
        str: html string
    """
    with open(path, "rb") as docx_file:
        result = convert_to_html(docx_file)
        html = result.value
        return html

def docx_to_html_io(file) -> str:
    """A function that converts a WORD document to a html string

    Args:
        path (str): path to file

    Returns:
        str: html string
    """
    result = convert_to_html(file)
    html = result.value
    return html


def create_image(src: str, article_obj) -> int:
    image = Image()
    image.article = article_obj
    base64_image = src.split(',')[-1]
    info = src.split(',')[0]
    image_bytes = base64.b64decode((base64_image)) 
    filename = base64_image[-10:]
    if 'png' in info:
        filename += '.png'
    elif 'jpeg' in info:
        filename += '.jpg'
    image_to_save = ImageFile(io.BytesIO(image_bytes), 
                      name=filename)
    revision = ImageRevision(image=image_to_save)
    image.add_revision(revision, save=True)
    return image.id

class ImageBlockConverter(MarkdownConverter):
    """
    Custom MarkdownConverter 
    """
    
    # class Options(MarkdownConverter.DefaultOptions):
    #     article_obj = None
    
    def convert_img(self, el, text, convert_as_inline):
        alt = el.attrs.get('alt', None) or ''
        src = el.attrs.get('src', None) or ''
        title = el.attrs.get('title', None) or ''
        title_part = ' "%s"' % title.replace('"', r'\"') if title else ''
        if (convert_as_inline
                and el.parent.name not in self.options['keep_inline_images_in']):
            return alt
        image_id = create_image(src, self.options.get('article_obj'))
        return f'[image:{image_id} size:orig]'

# Create shorthand method for conversion
def md(html, **options):
    print(options)
    return ImageBlockConverter(**options).convert(html)


def docx_to_markdown(path: str) -> str:
    """A function that converts a WORD document to a markdown string

    Args:
        path (str): path to file

    Returns:
        str: html string
    """
    html = docx_to_html(path)
    markdown = md(html)
    return markdown


def docx_to_markdown_io(file, article_obj) -> str:
    """A function that converts a WORD document to a markdown string

    Args:
        path (str): path to file

    Returns:
        str: html string
    """
    html = docx_to_html_io(file)
    markdown = md(html, article_obj=article_obj)
    return markdown