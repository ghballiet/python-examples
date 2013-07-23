from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
	(r'^$', 'flutemusic.views.index'),
	(r'^biblio/$', 'flutemusic.views.view_biblio'),
	(r'^manage_db/$', 'flutemusic.views.manage_db'),
	(r'^add_piece/$', 'flutemusic.views.add_piece'),
	(r'^add_composer/$', 'flutemusic.views.add_composer'),
	(r'^add_instrumentation/$', 'flutemusic.views.add_instrumentation'),
	(r'^add_category/$', 'flutemusic.views.add_category'),
	(r'^add_biblio/$', 'flutemusic.views.add_biblio'),
	(r'^login/$', 'flutemusic.views.login_view'),
	(r'^logout/$', 'flutemusic.views.logout_view'),
	(r'^delete_piece/$', 'flutemusic.views.delete_piece'),
	(r'^delete_biblio/$', 'flutemusic.views.delete_biblio'),
	(r'^composers/$', 'flutemusic.views.composers'),
	(r'^instrument/$', 'flutemusic.views.instrumentation'),
	# (r'^search/', include('haystack.urls')),
	(r'^search/$', 'flutemusic.views.search'),
)
