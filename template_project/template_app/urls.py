from django.urls import path
from template_app import views

app_name='template_app'

urlpatterns=[
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative')
]
