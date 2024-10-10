from django.urls import path
from .views import LoginView, LogOutView, LoginRefreshView, CreateUserView, VerifyAPIView, GetNewVerification, \
    ChangeUserInfoView, ChangeUserPhotoView, ForgotPasswordView, ResetPasswordView, NewPhoneNumberView, \
    VerifyCodeAndUpdatePhoneNumber, CodesView

urlpatterns = [
    # Authentication
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('refresh-token/', LoginRefreshView.as_view(), name='token_refresh'),

    # User Signup and Verification
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('verify/new/', GetNewVerification.as_view(), name='new_verification'),

    # User Info
    path('user/info/', ChangeUserInfoView.as_view(), name='change_user_info'),
    path('user/photo/', ChangeUserPhotoView.as_view(), name='change_user_photo'),

    # Password Management
    path('password/forgot/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('password/reset/', ResetPasswordView.as_view(), name='reset_password'),

    # Phone Number Management
    path('user/phone/', NewPhoneNumberView.as_view(), name='new_phone_number'),
    path('user/phone/verify/', VerifyCodeAndUpdatePhoneNumber.as_view(), name='verify_new_phone_number'),

    # Code Handling
    path('codes/', CodesView.as_view(), name='codes'),
]
