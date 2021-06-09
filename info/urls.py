from django.shortcuts import render
from django.urls import path
from .views import home_view, render_pdf_download, info_render_pdf_view, PeopleListView

app_name = 'info'

urlpatterns = [
    path('', PeopleListView.as_view(), name='user-list-view'),
    path('pdf/download/<pk>/', render_pdf_download, name='user-pdf-download'),
    path('pdf/view/<pk>/', info_render_pdf_view, name='user-pdf-view'),
    path('forms/', home_view, name='forms')
]