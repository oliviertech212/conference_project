from django.urls import path, re_path
from conf import views
urlpatterns = [
    # conference
    path('speakers/', views.speakers,name='speakers'),
    path('speakers/create', views.create,name='createspeaker'),
]