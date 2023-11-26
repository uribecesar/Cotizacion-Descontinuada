from django.shortcuts import render, redirect
from django.conf import settings
from .models import *
from .forms import *
# Para exportar a pdf
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile


def index(request):
    cotizaciones = Cotizacion.objects.all().order_by('-fecha_hora')
    valor_cotizacion = ValorCotizacion.objects.all()
    context = {
        'cotizaciones' : cotizaciones,
        'valor_cotizacion' : valor_cotizacion,
        'header' : 'Cotizaciones'
    }
    return render(request, 'index.html', context)

def cotizacion(request, item_id):
    try:
        cotizacion = Cotizacion.objects.get(id=item_id)
        items = ItemCotizacion.objects.filter(cotizacion=item_id)
        valores = ValorCotizacion.objects.get(cotizacion=item_id) 
        form_item = FormItemCotizacion(request.POST or None)
        form_editar_cot = FormCotizacion(request.POST or None, instance=cotizacion)

        if form_item.is_valid():
            form = form_item.save(commit=False) # Don't save it yet
            form.cotizacion = cotizacion # Add person
            form.save() # Now save it
            return redirect('cotizaciones:cotizacion', item_id=item_id)

        if form_editar_cot.is_valid():
            form = form_editar_cot.save()
            return redirect('cotizaciones:cotizacion', item_id=item_id)
        
        context = {
        'form_item' : form_item,
        'items' : items,
        'cotizacion' : cotizacion,
        'valores' : valores,
        'form_editar_cot' : form_editar_cot,
        }
    except Cotizacion.DoesNotExist:
        raise Http404("Cotización no existe")
    return render(request, 'cotizacion.html', context)



def eliminar_item_cot(request, item_id):
    item_cot = ItemCotizacion.objects.get(id=item_id)
    cotizacion = getattr(item_cot, 'cotizacion')
    id_cotizacion = cotizacion.id
    item_cot.delete()
    return redirect('cotizaciones:cotizacion', item_id=id_cotizacion)

def nueva_cotizacion(request):
    if request.method == "POST":
        formcotizacion = FormCotizacion(request.POST)
        if formcotizacion.is_valid():
            cotizacion = formcotizacion.save()
            return redirect("cotizaciones:cotizacion", item_id=cotizacion.id)
    else:
        formcotizacion = FormCotizacion()
        context = {
            'formcotizacion' : formcotizacion,
        }
        return render(request, 'nueva_cotizacion.html', context)

def cotizacion_pdf(request, context):
    try:
        item_id = context['item_id']
        plantilla = context['plantilla']
        cotizacion = Cotizacion.objects.get(id=item_id)
        items = ItemCotizacion.objects.filter(cotizacion=item_id)
        valores = ValorCotizacion.objects.get(cotizacion=item_id) 
        context = {
        'items' : items,
        'cotizacion' : cotizacion,
        'valores' : valores,
        'plantilla' : plantilla,
        }

         # Rendered
        html_string = render_to_string('cotizacion_pdf.html', context)
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        result = html.write_pdf(
            stylesheets=[
        # Change this to suit your css path
                settings.BASE_DIR + '/static/css/pdf.css',
                ],
                )
        # Creating http response
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline; filename="cotizacion_{cot}_{plant}.pdf"'.format(cot = cotizacion.id, plant=plantilla)
        response['Content-Transfer-Encoding'] = 'binary'
        with tempfile.NamedTemporaryFile(delete=True) as output:
            output.write(result)
            output.flush()
            output = open(output.name, 'rb')
            response.write(output.read())
        return response
    except Cotizacion.DoesNotExist:
        raise Http404("Cotización no existe")

def pdf_1covid(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : '1covid',
    }
    return cotizacion_pdf(request, context)

def pdf_1v_desinsec(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : '1v-desinsec',
    }
    return cotizacion_pdf(request, context)

def pdf_2v_desinsec(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : '2v-desinsec',
    }
    return cotizacion_pdf(request, context)

def pdf_des_int(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'des-int',
    }
    return cotizacion_pdf(request, context)

def pdf_bio_desrat(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'bio-desrat',
    }
    return cotizacion_pdf(request, context)

def pdf_bloq_desrat(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'bloq-desrat',
    }
    return cotizacion_pdf(request, context)

def pdf_covid_desinsec(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'covid-desinsec',
    }
    return cotizacion_pdf(request, context)

def pdf_desinsec_biorat(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'desinsec-biorat',
    }
    return cotizacion_pdf(request, context)

def pdf_desinsec_biorat_cov(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'desinsec-biorat-cov',
    }
    return cotizacion_pdf(request, context)

def pdf_desinsec_bloq_rat(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'desinsec-bloq-rat',
    }
    return cotizacion_pdf(request, context)

def pdf_desinsec_bloq_rat_cov(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'desinsec-bloq-rat-cov',
    }
    return cotizacion_pdf(request, context)

def pdf_tanq_cist(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'tanq-cist',
    }
    return cotizacion_pdf(request, context)

def pdf_extint(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'extint',
    }
    return cotizacion_pdf(request, context)

def pdf_basic(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'basic',
    }
    return cotizacion_pdf(request, context)

def pdf_basic_info(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'basic-info',
    }
    return cotizacion_pdf(request, context)

def pdf_basic_serv_info(request, item_id):
    context = {
        'item_id' :  item_id,
        'plantilla' : 'basic-serv-info',
    }
    return cotizacion_pdf(request, context)

   