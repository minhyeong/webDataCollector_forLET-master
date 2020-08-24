"""data_collector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from data_collector import views as local_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wdclet-help/', include('cms.urls', namespace='cms')),

    url(r'^log_view/$', local_views.log_view, name='log_view'),
    url(r'^log_view/(?P<user_id>\d+)/$', local_views.log_view_player, name='log_view_player'),
    url(r'^db_state/$', local_views.db_state, name='db_state'),
    url(r'', local_views.home, name='local_home'),
]
