from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','city',  'phone', 'website','user_info')

    def user_info(self, obj):
        return obj.description
    user_info.short_description = 'Info'

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone')
        return queryset
