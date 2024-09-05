from django.urls import path
from .views import ManuBsnCreateView, ManuBsnUpdateView, ManuBsnDeleteView, ManuBsnDetailView
from .views import ManuAccountCreateView, ManuAccountUpdateView, ManuAccountDeleteView, ManuAccountDetailView

urlpatterns = [
    path('business/create/', ManuBsnCreateView.as_view(), name='manubsn_create'),
    path('business/<int:pk>/update/', ManuBsnUpdateView.as_view(), name='manubsn_update'),
    path('business/<int:pk>/delete/', ManuBsnDeleteView.as_view(), name='manubsn_delete'),
    path('business/<int:pk>/', ManuBsnDetailView.as_view(), name='manubsn_detail'),
    path('account/create/', ManuAccountCreateView.as_view(), name='manuaccount_create'),
    path('account/<int:pk>/update/', ManuAccountUpdateView.as_view(), name='manuaccount_update'),
    path('account/<int:pk>/delete/', ManuAccountDeleteView.as_view(), name='manuaccount_delete'),
    path('account/<int:pk>/', ManuAccountDetailView.as_view(), name='manuaccount_detail'),
]
