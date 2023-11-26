from django.urls import path
from . import views

app_name = 'cotizaciones'
urlpatterns = [
    path('', views.index, name='index'),
    path('cotizacion/<int:item_id>/', views.cotizacion, name='cotizacion'),
    path('nuevo/', views.nueva_cotizacion, name='nueva_cotizacion'),
    path('eliminar_item/<int:item_id>/', views.eliminar_item_cot, name='eliminar_item'),

    path('pdf_1covid/<int:item_id>/', views.pdf_1covid, name='pdf_1covid'),
    path('pdf_1v_desinsec/<int:item_id>/', views.pdf_1v_desinsec, name='pdf_1v_desinsec'),
    path('pdf_2v_desinsec/<int:item_id>/', views.pdf_2v_desinsec, name='pdf_2v_desinsec'),
    path('pdf_des_int/<int:item_id>/', views.pdf_des_int, name='pdf_des_int'),
    path('pdf_bio_desrat/<int:item_id>/', views.pdf_bio_desrat, name='pdf_bio_desrat'),
    path('pdf_bloq_desrat/<int:item_id>/', views.pdf_bloq_desrat, name='pdf_bloq_desrat'),
    path('pdf_covid_desinsec/<int:item_id>/', views.pdf_covid_desinsec, name='pdf_covid_desinsec'),
    path('pdf_desinsec_biorat/<int:item_id>/', views.pdf_desinsec_biorat, name='pdf_desinsec_biorat'),
    path('pdf_desinsec_biorat_cov/<int:item_id>/', views.pdf_desinsec_biorat_cov, name='pdf_desinsec_biorat_cov'),
    path('pdf_desinsec_bloq_rat/<int:item_id>/', views.pdf_desinsec_bloq_rat, name='pdf_desinsec_bloq_rat'),
    path('pdf_desinsec_bloq_rat_cov/<int:item_id>/', views.pdf_desinsec_bloq_rat_cov, name='pdf_desinsec_bloq_rat_cov'),
    path('pdf_tanq_cist/<int:item_id>/', views.pdf_tanq_cist, name='pdf_tanq_cist'),
    path('pdf_extint/<int:item_id>/', views.pdf_extint, name='pdf_extint'),
    path('pdf_basic/<int:item_id>/', views.pdf_basic, name='pdf_basic'),
    path('pdf_basic_info/<int:item_id>/', views.pdf_basic_info, name='pdf_basic_info'),
    path('pdf_basic_serv_info/<int:item_id>/', views.pdf_basic_serv_info, name='pdf_basic_serv_info'),
    
]