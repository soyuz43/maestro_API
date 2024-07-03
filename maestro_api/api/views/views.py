from rest_framework import generics
from .models import Conversation, UserSettings
from .serializers import ConversationSerializer, UserSettingsSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ConversationListView(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

class UserSettingsView(generics.RetrieveUpdateAPIView):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
    permission_classes = [IsAuthenticated]
