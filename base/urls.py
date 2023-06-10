from django.urls import path, include
from .views import *


urlpatterns = [
    #landing-page
    path('',Home, name='home'),

    #Authentication Pages
    path('/login', Login, name='login'),
    path('/logout', Logout, name='logout'),

    #Main Page
    path('/Dashboard', Index,name='dashboard'),

    #Statistics Pages
    path('General-Diagnosis-Stats', generalstats, name='gstats'),

    path("chart-option/", get_filter_options, name="chart-filter-options"),
    path("chart/<int:year>/", get_generalpatient_chart, name="chart-sales"),
    path("patient-success/<int:year>/", general_status_chart, name="chart-payment-success"),

    
    path('Early-Diagnosis-Stats', earlystats, name='earlystats'),

    path("chart-options/", get_filter_options_early, name="chart-filter-options"),
    path("early-chart/<int:year>/", get_earlydiagnosis_chart, name="chart-sales"),
    path("early-patient-success/<int:year>/", early_status_chart, name="chart-payment-success"),

    path("early-patient-males/<int:year>/", get_early_males, name="chart-males"),

    #Chat Pages
    path('/Chat', Chat, name='chat'),
    path('/Start-Chat/<str:id>', StartChat, name='start-chat'),
    
    #Diagnosis Pages
    path('/Early-Diagnosis', Diagnosis, name='diagnosis'),
    path('EarlyDiagnosis', DiagnosisResult, name='early-diagnosis'),

    path('/General-Diagnosis',GDiagnosis, name='gdiagnosis'),
    path('General-Diagnosis',GeneralDiagnosis, name='general-diagnosis'),

    #DataTables 
    path('/Early-Diagnosis DataTable', TableList, name='table'),
    path('/General-Diagnosis DataTable', DataTable, name='datatable'),

    #SingleDataView
    path('/Early-Diagnosis Patient-Data View/<int:id>', SingleData, name='single-data'),
    path('/General-Diagnosis Patient-Data View/<int:id>', SingleView, name='single-view'),

    #NewData
    path('/New Early-Diagnosis Patient', NewData, name='newdata'),
    path('/New General-Diagnosis Patient', NewlyData, name='newlydata'),

    #Generating Reports
    path('General-Diagnosis Patient-Data Report', gen_single_report, name='gen-report'),
    path('Early-Diagnosis Patient-Data Report ', early_single_report, name='get-ealry-report'),

    #Delete Record
    path('General-Diagnosis Delete Patient/<int:id>', del_single_gen, name='del-patient'),
    path('Early-Diagnosis Delete Patient/<int:id>', del_early_gen, name='del-early-patient'),

]
