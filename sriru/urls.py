from django.conf.urls import patterns, url, include
from sriru import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^super$', views.superlogin, name='superlogin'),
    url(r'^manual/$', views.manual, name='manual'),
    url(r'^msg$', views.msg, name='message'),
    url(r'^deptadd$', views.deptadd, name='deptadd'),
    url(r'^msg_seen/(?P<_id>\d+)/$', views.msg_seen, name='msg_seen'),
    url(r'^prof/(?P<prof_id>\w+)/$', views.prof, name='prof'),
    url(r'^stud/(?P<stud_id>\w+)/$', views.stud, name='stud'),
    url(r'^spons/(?P<spons_name>\w+)/$', views.spons, name='spons'),
    url(r'^officer$', views.officer, name='officer'),
    url(r'^director$', views.director, name='director'),
    url(r'^approveproj/(?P<proj_id>\d+)/$', views.approveproj, name='approve'),
    url(r'^projapprove/(?P<proj_id>\d+)/$', views.projapprove, name='pro_approve'),
    url(r'^sponsorship/(?P<proj_id>\d+)/$', views.addsponsorship, name='sponsorship'),
    url(r'^fellowship$' , views.fellowship, name='fellowship'),
    url(r'^changepass$' , views.changepass, name='changepass'),
    url(r'^copi/(?P<prof_id>\w+)/$' , views.copi, name='copi'),
    url(r'^projupdt/(?P<proj_id>\d+)/$', views.projupdt, name='projupdt'),
    url(r'^appr_sanchead/(?P<proj_id>\d+)/$', views.apprsanc, name='appr_sanchead'),
    url(r'^approve1/(?P<pur_id>\d+)/$', views.approve1, name='approve1'),
    url(r'^approve2/(?P<pur_id>\d+)/$', views.approve2, name='approve2'),
    url(r'^approve3/(?P<pur_id>\d+)/$', views.approve3, name='approve3'),
    url(r'^dirapprove/(?P<pur_id>\d+)/$', views.dirapprove, name='dirapprove'),
    url(r'^dirpur/(?P<pur_id>\d+)/$', views.dirpur, name='approve2'),
    url(r'^rejdir/(?P<pur_id>\d+)/$', views.rejdir, name='rejdir'),
    url(r'^sanctions$', views.sanction, name='sanctions'),
    url(r'^logout1$', views.logout1, name='logout1'),
    url(r'^logout2$', views.logout2, name='logout2'),
    url(r'^logout3$', views.logout3, name='logout3'),
    url(r'^logout4$', views.logout4, name='logout4'),
    url(r'^logout5$', views.logout5, name='logout5'),
    url(r'^logout6$', views.logout6, name='logout6'),
    url(r'^new_proj$', views.newproj, name='create'),
    url(r'^purchase$', views.purchase, name='buy'),
    url(r'^purchasedur$', views.purchaseduration, name='pur_dur'),
    url(r'^comppurchase$', views.completepurchase, name='comp_pur'),
    url(r'^admin$', views.admin, name='admin'),
    url(r'^proj/(?P<project_id>\d+)/$', views.proj, name='proj'),
    url(r'^vendadd$', views.vendadd, name='vendadd'),
    url(r'^sponsadd$', views.sponsadd, name='sponsadd'),
    url(r'^profadd$', views.profadd, name='profadd'),
    url(r'^studadd$', views.studadd, name='studadd'),
    url(r'^purchase$' , views.purchase, name='purchase'),
    url(r'^tenderlist$', views.tenderlist, name='tenderlist'),
    url(r'^tender/(?P<ten_id>\d+)/$', views.tender, name='tender'),
    url(r'^grant/(?P<proj_id>\d+)/$' , views.grant, name='grant'),
    url(r'^up_sanc/(?P<proj_id>\d+)/$', views.up_sanc, name='up_sanc'),
    url(r'^das$' , views.das, name='das'),
    url(r'^dascomp$' , views.dascomp, name='dascomp'),
    url(r'^apprsanc/(?P<proj_id>\d+)/$' , views.apprsanc, name='apprsanc'),
    url(r'^gentable/(?P<proj_id>\d+)/$' , views.generateTable, name='gentable'),
    url(r'^search/(?P<text>\w+)/$', views.search_project, name='search'),
)