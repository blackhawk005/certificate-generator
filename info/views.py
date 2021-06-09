from django.db import models
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import Detail
from .forms import DetailForm
# Create your views here.

class PeopleListView(ListView):
    models = Detail
    template_name = 'info/main.html'

    def get_queryset(self):
      return Detail.objects.order_by('id')

def info_render_pdf_view(request, *args, **kwargs):

    pk = kwargs.get('pk')
    user = get_object_or_404(Detail, pk=pk)
    template_path = 'info/certificate.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # for downloading
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # for previewing
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def render_pdf_download(request, *args, **kwargs):
    pk = kwargs.get('pk')
    user = get_object_or_404(Detail, pk=pk)
    template_path = 'info/certificate.html'
    context = {
        'pagesize':'A5',
        'user': user
        }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # for downloading
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # for previewing
    # response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def home_view(request):
   context ={}

   # create object of form
   form = DetailForm(request.POST, request.FILES)
   # check if form data is valid
   if form.is_valid():
      # save the form data to model
      form.save()
      context['form']= form
      return redirect('/')

   context['form']= form
   return render(request, "info/form.html", context)

   
