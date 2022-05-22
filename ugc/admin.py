from django.contrib import admin

from .forms import ProfileForm
from .models import Profile, Message

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'external_id', 'name', 'username', 'group')
    form = ProfileForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at', 'group')
