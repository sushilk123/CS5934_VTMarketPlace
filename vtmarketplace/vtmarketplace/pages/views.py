from django.shortcuts import get_object_or_404

from vtmarketplace.views import BaseView
from vtmarketplace.pages.models import Page


class BasePageView(BaseView):
    """
    Renders page under BaseView
    """
    style_name = 'pages'
    template_name = 'pages/base_page.html'

    def get(self, request, slug):
        page = get_object_or_404(Page, slug=slug, status=Page.STATUS_PUBLISHED)
        return super(BasePageView, self).get(request, page_title=page.title, page=page)
