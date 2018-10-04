from django.urls import path
from app.contact import views
app_name='contact'

urlpatterns = [
	# url(r'^contact/(?P<contact_id>[0-9]+)$',views.ContactApi.as_view()),
	path('contact/',views.ContactApi.as_view()),
	path('contact/list/',views.CrmContactApi.as_view())
	
]
