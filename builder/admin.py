from django.contrib import admin
from .models import (
    ThemeTemplate, ClinicWebsite, WebsitePage, Doctor, 
    Treatment, GalleryItem, AppointmentEnquiry, WebsiteTestReport, DeploymentLog
)

@admin.register(ThemeTemplate)
class ThemeTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'primary_color', 'is_system_default', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

@admin.register(ClinicWebsite)
class ClinicWebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain_name', 'status', 'phone', 'theme', 'last_test_score', 'created_at')
    list_filter = ('status', 'theme')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'domain_name', 'phone', 'email')

@admin.register(WebsitePage)
class WebsitePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'clinic', 'page_type', 'nav_order', 'is_active', 'show_in_nav')
    list_filter = ('clinic', 'page_type', 'is_active')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinic', 'specialization', 'experience_years', 'available_days', 'is_active')
    list_filter = ('clinic', 'is_active')
    search_fields = ('name', 'specialization', 'qualification')

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'clinic', 'price_starting_at', 'duration', 'is_featured', 'order')
    list_filter = ('clinic', 'is_featured')
    search_fields = ('name', 'short_description')

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'clinic', 'category', 'order')
    list_filter = ('clinic', 'category')

@admin.register(AppointmentEnquiry)
class AppointmentEnquiryAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'clinic', 'mobile_number', 'appointment_date', 'preferred_time', 'treatment', 'status', 'created_at')
    list_filter = ('clinic', 'status', 'appointment_date')
    search_fields = ('patient_name', 'mobile_number', 'email', 'treatment')

@admin.register(WebsiteTestReport)
class WebsiteTestReportAdmin(admin.ModelAdmin):
    list_display = ('clinic', 'overall_score', 'passed_checks', 'failed_checks', 'run_date')
    list_filter = ('clinic',)

@admin.register(DeploymentLog)
class DeploymentLogAdmin(admin.ModelAdmin):
    list_display = ('clinic', 'target_domain', 'status', 'deployed_at')
    list_filter = ('clinic', 'status')
