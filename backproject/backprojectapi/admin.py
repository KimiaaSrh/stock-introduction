from django.contrib import admin

# Register your models here.
from .models import Post, Rating,JointoChat

admin.site.register(Post)
admin.site.register(Rating)
admin.site.register(JointoChat)