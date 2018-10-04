from django.urls import path
from app.owner import views

app_name='owner'

urlpatterns = [
	path('owner/',views.OwnerView.as_view()),
	path('owner/<property_id>',views.OwnerView.as_view()),
]