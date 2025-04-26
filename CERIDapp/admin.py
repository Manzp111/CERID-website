from django.contrib import admin
from CERIDapp import models


@admin.register(models.LeaderTeam)
class LeaderTeamAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'position','description', 'image')
    search_fields = ('name',)
    list_filter = ('position',)
    list_per_page = 10
    ordering = ('-id',)


@admin.register(models.ImageSlider)
class ImageSliderAdmin(admin.ModelAdmin):
    list_display = ('id','image','caption')

@admin.register(models.FinancialReport)
class FinancialReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'year')

@admin.register(models.ImpactMetric)
class ImpactMetricAdmin(admin.ModelAdmin):
    list_display = ('year', 'projects', 'people', 'regions')

@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')

@admin.register(models.LegalDocument)
class LegalDocumentAdmin(admin.ModelAdmin):
    list_display = ('name',)