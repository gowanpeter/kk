
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()
from gowan.views import GlazeView

urlpatterns = patterns('',
    # Examples:
    url(r'^home$', 'gowan.views.home', name='home'),
    url(r'^glaze$', 'gowan.views.GlazeView', name='glaze'),
    url(r'^documentation$', 'gowan.views.DocumentationView', name='documentation',),
     url(r'^condition$', 'gowan.views.ConditionChoiceView', name='condition',),
     url(r'^exhibition$', 'gowan.views.ExhibitionView', name='exhibition',),

    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
)



    #src/kk
 #   url(r'^gowan/', include('gowan.urls', namespace='gowan', app_name='kk')),
 #   url(r'^$',gowan.views.kk_directory, name='kk')


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
