from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', views.do_login, name='login'),
    url(r'^graficos$', views.graficos, name='graficos'),
    url(r'^login$', views.do_login, name='login'),
    url(r'^logout$', views.do_logout, name='logout'),
	
    # ex: /polls/5/
    url(r'^(?P<cliente_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<cliente_id>[0-9]+)/results/$', views.results, name='results'),
]
urlpatterns += staticfiles_urlpatterns()
