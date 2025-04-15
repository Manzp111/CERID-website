from django.contrib import admin
from CERIDapp import models


@admin.register(models.LeaderTeam)
class LeaderTeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'position','description', 'image')
    search_fields = ('name',)
    list_filter = ('position',)
    list_per_page = 10
    ordering = ('-id',)

# Register your models here.
