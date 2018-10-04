from django.urls import path
from app.properties import views

app_name='properties'

urlpatterns = [
	path('property/',views.PropertyView.as_view()),
	path('property/<property_id>',views.PropertyView.as_view()),
]