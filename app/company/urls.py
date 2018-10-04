# from django.conf.urls import url
from app.company import views
from django.urls import path
app_name='company'


urlpatterns = [
	path('company/list/',views.CrmCompanyApi.as_view()),
	path('company/',views.CompanyApi.as_view()),

]