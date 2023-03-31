from django.urls import path
from .views import MemberDetailView, AppointmentCreateView

urlpatterns = [
    path('', MemberDetailView.as_view(), name='book'),
    path('<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('<slug:slug>/', MemberDetailView.as_view(), name='member_detail'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='create_appointment'),
]
