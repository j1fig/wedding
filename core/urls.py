from django.conf.urls import patterns, url

import views

urlpatterns = patterns(
    '',
    url(r'^guest/add/$', views.GuestAdd.as_view(), name='guest_add'),
)
