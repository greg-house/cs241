from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cs241.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^sriru/', include('sriru.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^account/prof/', 'cs241.views.proflogin', name='proflogin'),
#    url(r'^account/stud/', 'cs241.views.studlogin', name='studlogin'),
#    url(r'^account/spons/', 'cs241.views.sponslogin', name='sponslogin'),
#    url(r'^account/vend/', 'cs241.views.vendlogin', name='vendlogin'),
    # url(r'^$', TemplateView.as_view(template_name='sriru/index.html'), name="home"),
)
