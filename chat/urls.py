from django.urls import path
from .views import (
    ManageGlobalGroup
)

urlpatterns = [
    path('creategroup/',ManageGlobalGroup.as_view(),name='creategroup'),
]