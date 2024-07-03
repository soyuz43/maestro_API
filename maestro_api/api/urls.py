from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListView, ConversationListView, UserSettingsView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
    path('settings/<int:pk>/', UserSettingsView.as_view(), name='user-settings')
]
