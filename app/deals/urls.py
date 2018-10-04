from django.urls import path
from app.deals import views
app_name='deals'


urlpatterns = [
	# url(r'^deal/(?P<job_id>[0-9]+)$',views.DealByJobId.as_view()),
	# url(r'^deal/(?P<deal_id>[0-9]+)$',views.DealApi.as_view()),
	path('deal/',views.DealApi.as_view()),

]