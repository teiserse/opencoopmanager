from django.urls import include, path

from . import views

app_name = 'opencoopmanager'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vote_id>/', views.votemain, name='votemain'),
    path('<int:vote_id>/send/', views.sendballot, name='sendballot'),
    path('accounts/', include('django.contrib.auth.urls'), name='accounts'),
]
