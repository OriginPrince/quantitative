"""QService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import quantitative.views as qu
import quantitative.displaydata.disHistDataCYB as h_cyb
import quantitative.displaydata.disHistDataHS300 as h_hs300
import quantitative.displaydata.disHistDataSH as h_sh
import quantitative.displaydata.disHistDataSZ as h_sz
import quantitative.displaydata.disHistDataSZ50 as h_sz50
import quantitative.displaydata.disHistDataZXB as h_zxb
import quantitative.displaydata.disNowDataCYB as n_cyb
import quantitative.displaydata.disNowDataHS300 as n_hs300
import quantitative.displaydata.disNowDataSH as n_sh
import quantitative.displaydata.disNowDataSZ as n_sz
import quantitative.displaydata.disNowDataSZ50 as n_sz50
import quantitative.displaydata.disNowDataZXB as n_zxb
import quantitative.registerLogin.register as rl
import quantitative.registerLogin.login as rel
import django
import settings
import quantitative.analysis.changeData as QC

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^disHist/$', qu.DispalyHist),
    url(r'^disNow/$', qu.DispalyNow),
    url(r'^disRecord/$', qu.DisRecord),
    url(r'^register/$', qu.register),
    url(r'^change/$', qu.change),
    url(r'^change_final/$', QC.change_final),
    url(r'^change_initial/$', QC.change_initial),
    url(r'^post_register/$',rl.post_register ),
    url(r'^post_login/$', rel.post_login),
    url(r'^logout/$', rel.logout),
    url(r'^display_hist_sh/$', h_sh.display_hist_sh),
    url(r'^display_hist_sh_price/$', h_sh.display_hist_sh_price),
    url(r'^display_hist_sz/$', h_sz.display_hist_sz),
    url(r'^display_hist_sz_price/$', h_sz.display_hist_sz_price),
    url(r'^display_hist_hs300/$', h_hs300.display_hist_hs300),
    url(r'^display_hist_hs300_price/$', h_hs300.display_hist_hs300_price),
    url(r'^display_hist_sz50/$', h_sz50.display_hist_sz50),
    url(r'^display_hist_sz50_price/$', h_sz50.display_hist_sz50_price),
    url(r'^display_hist_zxb/$', h_zxb.display_hist_zxb),
    url(r'^display_hist_zxb_price/$', h_zxb.display_hist_zxb_price),
    url(r'^display_hist_cyb/$', h_cyb.display_hist_cyb),
    url(r'^display_hist_cyb_price/$', h_cyb.display_hist_cyb_price),
    url(r'^display_now_sh/$', n_sh.display_now_sh),
    url(r'^display_now_sh_price/$', n_sh.display_now_sh_price),
    url(r'^display_now_sz/$', n_sz.display_now_sz),
    url(r'^display_now_sz_price/$', n_sz.display_now_sz_price),
    url(r'^display_now_hs300/$', n_hs300.display_now_hs300),
    url(r'^display_now_hs300_price/$', n_hs300.display_now_hs300_price),
    url(r'^display_now_sz50/$', n_sz50.display_now_sz50),
    url(r'^display_now_sz50_price/$', n_sz50.display_now_sz50_price),
    url(r'^display_now_zxb/$', n_zxb.display_now_zxb),
    url(r'^display_now_zxb_price/$', n_zxb.display_now_zxb_price),
    url(r'^display_now_cyb/$', n_cyb.display_now_cyb),
    url(r'^display_now_cyb_price/$', n_cyb.display_now_cyb_price),
    url(r'^static/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATICFILES_DIRS,'show_indexes': True}),
]
