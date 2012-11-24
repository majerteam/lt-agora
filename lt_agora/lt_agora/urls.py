from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from tastypie.api import Api
from agora.api import DecisionResource, VoteResource, UserResource
from agora.models import Decision

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),
    url(r'^comments/', include('fluent_comments.urls')),
    url(r'^accounts/', include('accounts.urls')),
)

# website views
urlpatterns += patterns('agora.views',
    url(r'^$', 'index', name='home'),
    url(r'^about/?$', 'about', name='about'),
    url(r'^logout/?$', 'index', name='logout'),
)

# generic views 
info_dict = {
    'queryset': Decision.objects.all(),
}

urlpatterns += patterns('',
    url(r'^decision/all/?$', 'django.views.generic.list_detail.object_list', info_dict, name="decision_list"),
    url(r'^decision/(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict, name="decision_detail"),
)

# api views
v1_api = Api(api_name='v1')
v1_api.register(DecisionResource())
v1_api.register(VoteResource())
v1_api.register(UserResource())

urlpatterns += patterns('',
    (r'^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
