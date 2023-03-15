# Django imports
from django.urls import path


# Views imports
from apps.transaction.api.views import (
    transaction_api_view,
    transaction_detail_view,
    transfer_api_view,
    deposit_api_view,
    extraction_api_view
)


# Urls
urlpatterns = [
    path(
        'transaction/',
        transaction_api_view,
        name='transaction_api_view'
    ),
    path(
        'transaction/<int:pk>/',
        transaction_detail_view,
        name='transaction_detail_api_view'
    ),
    path(
        'deposit/',
        deposit_api_view,
        name='transaction_deposit_api_view'
    ),
    path(
        'extraction/',
        extraction_api_view,
        name='transaction_extraction_api_view'
    ),
    path(
        'transfer/',
        transfer_api_view,
        name='transaction_transfer_api_view'
    )
]