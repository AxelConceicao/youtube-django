from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
  list_display = ('title', 'created_at', 'views',)
  ordering = ('-created_at', 'title',)
  search_fields = ('title',)
  readonly_fields = ('id', 'created_at', 'updated_at', )

admin.site.register(Video, VideoAdmin)