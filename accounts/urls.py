from django.urls import path
from accounts.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/freelancer/', RegisterFreelancerAPIView.as_view()),
    path('register/client/', RegisterClientAPIView.as_view()),

    path('activate/freelancer/<uuid:activation_code>/', ActivationFreelancerAPIView.as_view()),
    path('activate/client/<uuid:activation_code>/', ActivationClientAPIView.as_view()),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('reset_password', ForgotPasswordAPIView.as_view()),
    path('reset_password_complete', ForgotPasswordCompleteAPIView.as_view())

    # TODO: написвать сброс пароля
]
