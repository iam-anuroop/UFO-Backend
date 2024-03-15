from django.urls import path
from .views import (
    ManageGlobalGroup,
    GetGlobalGrroups,
    SearchRandomPerson,
    BlockUserFromGroup,
)

urlpatterns = [
    path('creategroup/',ManageGlobalGroup.as_view(),name='creategroup'),
    path('globalgroups/',GetGlobalGrroups.as_view(),name='globalgroups'),
    path('find/',SearchRandomPerson.as_view(),name='find'),
]
