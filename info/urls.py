from django.shortcuts import render
from django.urls import path
from .views import home_view, render_pdf_download, info_render_pdf_view, PeopleListView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'info'

urlpatterns = [
    path('', PeopleListView.as_view(), name='user-list-view'),
    path('pdf/download/<pk>/', render_pdf_download, name='user-pdf-download'),
    path('pdf/view/<pk>/', info_render_pdf_view, name='user-pdf-view'),
    path('forms/', home_view, name='forms')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)