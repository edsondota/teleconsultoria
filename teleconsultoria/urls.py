from django.conf.urls import include, url
from django.contrib import admin
from teleconsultoria.views import LoginView

urlpatterns = [

    url(r'^$', LoginView.as_view(), name="login_view"),
    url(r'^admin/', include(admin.site.urls)),
]
