from django.urls import path
from .views import PayablesViews, TransactionViews

urlpatterns = [
    path('pending-tax/', PayablesViews.as_view()),
    path('pending-tax/<str:servicio>', PayablesViews.as_view()),
    path('payments/', TransactionViews.as_view()),
    path('payments/<str:start_date>/<str:end_date>', TransactionViews.as_view()),
    path('create-tax/', PayablesViews.as_view()),
    path('pay-tax/', TransactionViews.as_view()),
    
]