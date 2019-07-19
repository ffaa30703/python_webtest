from django.urls import path
from sign import views_if

urlpatterns = [
    path('test/', views_if.test, name='test'),
    path('add_event/', views_if.add_event, name='add_event'),

    path('get_event_list/', views_if.get_event_list, name='get_event_list'),

]
