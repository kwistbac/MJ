from django.conf.urls import patterns, url


urlpatterns = patterns('',

                       url(r'^$', 'apps.users.views.home'),


                       )