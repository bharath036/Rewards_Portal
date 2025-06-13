from django.urls import path
from home.views import index,delete_transaction
urlpatterns = [
    path('', index, name='home'),
    path('delete-transaction/<id>',delete_transaction,name="delete_transaction")
]