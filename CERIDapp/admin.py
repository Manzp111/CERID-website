from django.contrib import admin
from CERIDapp import models   
from .models import HeroSection, VisionItem, Project


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


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)

@admin.register(VisionItem)
class VisionItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'completion_date')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'phone', 'message')
    search_fields = ('first_name', 'last_name')
    list_filter = ('email',)
    list_per_page = 10
    ordering = ('-id',)