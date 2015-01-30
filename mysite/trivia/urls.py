from django.conf.urls import patterns, url

from trivia import views


urlpatterns = patterns('',
    url(r'^daily/$', views.dailyview, name='daily'),
    url(r'^leader/$', views.leaderview.as_view(), name='leader'),
    url(r'^(?P<userid>\d+)/$', views.profileview, name='profile'),
    url(r'^correctResults/$', views.correctResultsView, name= 'results'),
    url(r'^incorrectResults/$', views.incorrectResultsView, name= 'results'),
    url(r'^$', views.user_login, name='login'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^about/$', views.about_view, name='about'),
#    url(r'^/login/$', view.LoginView.as_view(), name='login')
#    url(r'^(?P<pk>\d+)/$', views.AnswerView.as_view(), name='answer'),
#    url(r'^(?P<pk>\d+)/leader/$', views.LeaderView.as_view(), name='leader'),
#    url(r'^(?P<question_id>\d+)/report/$', views.ReportView.as_view(), name='report'),
)