from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from wallets.views import WalletViewSet
from categories.views import CategoryViewSet
from transactions.views import TransactionViewSet
from support.views import SupportViewSet
from users.views import RegisterView, LoginView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'support', SupportViewSet, basename='support')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]