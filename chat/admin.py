from django.contrib import admin
from .models import GlobalGroup,GroupMessage,Message,BlockedUser,Search


admin.site.register(GlobalGroup)
admin.site.register(GroupMessage)
admin.site.register(Message)
admin.site.register(BlockedUser)
admin.site.register(Search)



# Register your models here.
