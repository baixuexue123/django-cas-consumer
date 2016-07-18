from django.conf.urls import url, patterns

from cas_consumer.views import *

urlpatterns = patterns('',
    url(r'^login/', login, name="cas_login"),
    url(r'^logout/', logout, name="cas_logout"),
)
