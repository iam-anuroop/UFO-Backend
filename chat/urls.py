from django.urls import path
from .views import (
    ManageGlobalGroup,
    GetGlobalGrroups
)

urlpatterns = [
    path('creategroup/',ManageGlobalGroup.as_view(),name='creategroup'),
    path('globalgroups/',GetGlobalGrroups.as_view(),name='globalgroups'),
]