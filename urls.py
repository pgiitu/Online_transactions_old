from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Online_transactions.views.home', name='home'),
    # url(r'^Online_transactions/', include('Online_transactions.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^Online_transactions/','transactions.views.login'),
    url(r'^home_page/','transactions.views.home'),
    url(r'^funds_transfer/','transactions.views.show_funds_transfer'),
    url(r'^interbank_transfer/','transactions.views.show_interbank_transfer'),
    url(r'^thirdparty_transfer/','transactions.views.show_thirdparty_transfer'),
)
