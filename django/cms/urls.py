from django.conf.urls import url
from cms import views

urlpatterns = [
    # アンケート規約
    url(r'^agreement/$', views.agreement, name='agreement'),

    # 基本質問
    url(r'^question/basic/$', views.question_basic, name='question_basic'),

    # 生命の質
    url(r'^question/lifequality_rank_fix/$', views.question_lifequality_rank_fix,
        name='question_lifequality_rank_fix'),

    # TIPI_J
    url(r'^question/TIPI_J/$', views.TIPI_J, name='TIPI_J'),

    # DAS
    url(r'^question/DAS/$', views.DAS, name='DAS'),

    # 延命治療選択
    url(r'^question/lifeprolonging/$', views.question_lifeprolonging, name='question_lifeprolonging'),

    # ログ
    url(r'^logging/$', views.logging, name='logging'),

    url(r'^finish/$', views.finish, name='finish'),
    url(r'', views.home, name='home'),

]
