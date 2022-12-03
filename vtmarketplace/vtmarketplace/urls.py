from django.conf.urls import include, url


# vtmarketplace apps urls
urlpatterns = [
    url(r'^', include('vtmarketplace.catalog.urls')),
    url(r'^accounts/', include('vtmarketplace.accounts.urls')),
    url(r'^sales/', include('vtmarketplace.sales.urls')),
    url(r'^payments/', include('vtmarketplace.payments.urls')),
    url(r'^pages/', include('vtmarketplace.pages.urls'))
]
