# from django.conf.urls import url
from django.urls import path
from app.job import views
app_name='job'

urlpatterns = [
	path('deal/',views.CrmJobApi.as_view()),
	path('job/<int:job_id>/',views.JobApi.as_view()),
	path('job/',views.JobApi.as_view()),
	
]
