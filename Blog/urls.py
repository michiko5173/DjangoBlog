from django.conf.urls import url
from django.contrib import admin

from cmdb.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    #url(r'^(?P<my_args>\d+)/$', detail, name='detail'),
    #url(r'^test/$', test,name='test'),
]