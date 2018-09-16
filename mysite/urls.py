"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from .yelp.views import index, eventList, eventDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index.page, name='index'),
    re_path(r'^events$', eventList.page, name='events'),
    path('event_detail/<str:event_id>&<str:miles_away>', eventDetail.page, name='eventDetail'),
    re_path(r'^json/events$', eventList.api, name='eventsJSON'),
    path('json/event_detail/<str:event_id>&<str:miles_away>', eventDetail.api, name='eventDetailJSON'),

    re_path(r'^react/events$', eventList.ReactView.as_view(), name='react_events'),
]
