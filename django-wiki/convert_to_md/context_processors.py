from django.conf import settings

def admin_processor(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'WIKI_HEADER_BRANDING': settings.WIKI_HEADER_BRANDING,
            'WIKI_HEADER_NAVLINKS': settings.WIKI_HEADER_NAVLINKS,
            'WIKI_SITE_TITLE': settings.WIKI_SITE_TITLE}