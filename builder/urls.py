from django.urls import path
from . import views

urlpatterns = [
    # 1. Main Dashboard
    path('', views.dashboard_overview, name='dashboard_overview'),
    
    # 2. Manage & Create Websites
    path('websites/', views.website_list, name='website_list'),
    path('websites/create/', views.website_create, name='website_create'),
    path('websites/<int:clinic_id>/switch/', views.website_switch, name='website_switch'),
    path('websites/<int:clinic_id>/duplicate/', views.website_duplicate, name='website_duplicate'),
    path('websites/<int:clinic_id>/delete/', views.website_delete, name='website_delete'),
    
    # 3. Theme & Template Library
    path('themes/', views.theme_library, name='theme_library'),
    path('themes/<int:theme_id>/apply/', views.theme_apply, name='theme_apply'),
    path('themes/<int:theme_id>/duplicate/', views.theme_duplicate, name='theme_duplicate'),
    path('themes/upload/', views.theme_upload, name='theme_upload'),
    
    # 4. Website Customization
    path('customization/', views.customization_view, name='customization_view'),
    
    # 5. Page Management
    path('pages/', views.pages_list, name='pages_list'),
    path('pages/<int:page_id>/edit/', views.page_edit, name='page_edit'),
    
    # 6. Clinic Information
    path('clinic-info/', views.clinic_info_view, name='clinic_info_view'),
    
    # 7. Doctors Management
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:doctor_id>/edit/', views.doctor_edit, name='doctor_edit'),
    path('doctors/<int:doctor_id>/delete/', views.doctor_delete, name='doctor_delete'),
    
    # 8. Treatments Management
    path('treatments/', views.treatments_list, name='treatments_list'),
    path('treatments/create/', views.treatment_create, name='treatment_create'),
    path('treatments/<int:treatment_id>/edit/', views.treatment_edit, name='treatment_edit'),
    path('treatments/<int:treatment_id>/delete/', views.treatment_delete, name='treatment_delete'),
    
    # 9. Gallery Management
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('gallery/<int:item_id>/delete/', views.gallery_delete, name='gallery_delete'),
    
    # 10. Appointment Enquiries & WhatsApp
    path('enquiries/', views.enquiries_list, name='enquiries_list'),
    path('enquiries/<int:enquiry_id>/update-status/', views.enquiry_update_status, name='enquiry_update_status'),
    path('enquiries/export-csv/', views.enquiry_export_csv, name='enquiry_export_csv'),
    path('whatsapp-integration/', views.whatsapp_config_view, name='whatsapp_config_view'),
    
    # 11. SEO Management
    path('seo/', views.seo_management_view, name='seo_management_view'),
    
    # 12. Website Preview
    path('preview/', views.website_preview_view, name='website_preview_view'),
    path('preview/<int:clinic_id>/', views.website_preview_view, name='website_preview_by_id'),
    
    # 13. Website Testing
    path('testing/', views.website_testing_view, name='website_testing_view'),
    path('testing/<int:clinic_id>/', views.website_testing_view, name='website_testing_by_id'),
    path('testing/run/', views.run_website_test, name='run_website_test'),
    path('testing/run/<int:clinic_id>/', views.run_website_test, name='run_website_test_by_id'),
    
    # 14. Website Publishing & Deployment
    path('publishing/', views.website_publish_view, name='website_publish_view'),
    path('publishing/<int:clinic_id>/', views.website_publish_view, name='website_publish_by_id'),
    path('publishing/export-zip/', views.export_website_zip, name='export_website_zip'),
    path('publishing/export-zip/<int:clinic_id>/', views.export_website_zip, name='export_website_zip_by_id'),
    
    # 15. Settings
    path('settings/', views.settings_view, name='settings_view'),

    # -----------------------------------------------------------------
    # PUBLIC DENTAL CLINIC WEBSITES (MULTI-TENANT ENDPOINTS)
    # -----------------------------------------------------------------
    path('site/<slug:slug>/', views.site_home, name='site_home'),
    path('site/<slug:slug>/about/', views.site_about, name='site_about'),
    path('site/<slug:slug>/treatments/', views.site_treatments, name='site_treatments'),
    path('site/<slug:slug>/treatments/<slug:treatment_slug>/', views.site_treatment_detail, name='site_treatment_detail'),
    path('site/<slug:slug>/doctors/', views.site_doctors, name='site_doctors'),
    path('site/<slug:slug>/gallery/', views.site_gallery, name='site_gallery'),
    path('site/<slug:slug>/contact/', views.site_contact, name='site_contact'),
    path('site/<slug:slug>/book-appointment/', views.site_appointment, name='site_appointment'),
    path('site/<slug:slug>/submit-appointment/', views.site_submit_appointment, name='site_submit_appointment'),
    path('site/<slug:slug>/sitemap.xml', views.site_sitemap, name='site_sitemap'),
    path('site/<slug:slug>/robots.txt', views.site_robots, name='site_robots'),
]

