import os
import json
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class ThemeTemplate(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, default='Modern')
    preview_image = models.ImageField(upload_to='themes/previews/', null=True, blank=True)
    
    # Color scheme defaults
    primary_color = models.CharField(max_length=30, default='#0ea5e9')
    secondary_color = models.CharField(max_length=30, default='#0369a1')
    accent_color = models.CharField(max_length=30, default='#06b6d4')
    background_color = models.CharField(max_length=30, default='#ffffff')
    text_color = models.CharField(max_length=30, default='#1e293b')
    font_family = models.CharField(max_length=100, default='Poppins, sans-serif')
    
    is_active = models.BooleanField(default=True)
    is_system_default = models.BooleanField(default=False)
    custom_css = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class ClinicWebsite(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft / In Progress'),
        ('testing', 'Testing & Review'),
        ('published', 'Published & Live'),
        ('maintenance', 'Maintenance Mode'),
    ]

    HEADER_STYLES = [
        ('modern', 'Modern Sticky (Clean with Top Emergency Bar)'),
        ('classic', 'Classic Hospital (Detailed Header)'),
        ('minimal', 'Minimalist Floating Nav'),
    ]

    FOOTER_STYLES = [
        ('multi-column', 'Four Column Full Info'),
        ('compact', 'Compact Clean Footer'),
    ]

    # 1. Basic Info
    name = models.CharField(max_length=200, help_text="e.g. Aura Dental Care & Implant Center")
    slug = models.SlugField(max_length=200, unique=True, help_text="Unique website slug identifier")
    tagline = models.CharField(max_length=255, default="Precision Dentistry, Gentle Care & Radiant Smiles")
    logo = models.ImageField(upload_to='clinics/logos/', null=True, blank=True)
    favicon = models.ImageField(upload_to='clinics/favicons/', null=True, blank=True)
    domain_name = models.CharField(max_length=255, blank=True, help_text="Assigned Domain (e.g. www.auradentalcare.com)")
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='draft')
    theme = models.ForeignKey(ThemeTemplate, on_delete=models.SET_NULL, null=True, blank=True, related_name='clinics')

    # 2. Contact Details
    phone = models.CharField(max_length=50, default="+91 7499077170")
    whatsapp_number = models.CharField(max_length=50, default="917499077170", help_text="Digits only with country code, e.g. 917499077170")
    email = models.EmailField(default="contact@auradentalcare.com")
    address = models.TextField(default="Suite 400, 750 Health Plaza Blvd, Medical District, NY 10001")
    google_maps_embed = models.TextField(blank=True, default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.119763973046!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1680000000000!5m2!1sen!2sus")
    working_hours = models.TextField(default="Monday – Friday: 8:30 AM – 7:30 PM\nSaturday: 9:00 AM – 5:00 PM\nSunday: Emergency Appointments Only")
    emergency_contact = models.CharField(max_length=50, blank=True, default="+1 (800) 555-3399")

    # 3. Social Media Links
    facebook_url = models.URLField(blank=True, default="https://facebook.com")
    instagram_url = models.URLField(blank=True, default="https://instagram.com")
    twitter_url = models.URLField(blank=True, default="https://twitter.com")
    youtube_url = models.URLField(blank=True, default="https://youtube.com")
    linkedin_url = models.URLField(blank=True, default="https://linkedin.com")

    # 4. About Clinic
    about_short = models.TextField(default="Welcome to our state-of-the-art dental clinic. We deliver pain-free, specialized dental treatments with world-class technology, compassion, and transparent care.")
    about_full = models.TextField(default="Founded with a mission to redefine contemporary dental excellence, our clinic combines cutting-edge dental innovations with human-centric hospitality. From routine preventive checkups to complex full-mouth dental implant rehabilitations, our board-certified specialists ensure every patient leaves with renewed confidence.")
    mission = models.TextField(default="To deliver highest-standard, gentle, and ethical dental care utilizing evidence-based techniques and state-of-the-art clinical sterilization.")
    vision = models.TextField(default="To be the regional benchmark in advanced cosmetic, implant, and preventive dentistry, inspiring lifelong dental wellness.")
    history_founded_year = models.CharField(max_length=20, default="2012")
    facilities_text = models.TextField(default="3D CBCT Digital Imaging, Laser Gum Therapy, Zero-Pain Anesthesia Delivery, In-House CAD/CAM Milling Lab, Class-B European Autoclave Sterilization Suite, Dedicated Pediatric Operatory.")

    # 5. Styling & Customization
    primary_color = models.CharField(max_length=30, default='#0ea5e9', help_text="Main theme brand color")
    secondary_color = models.CharField(max_length=30, default='#0369a1', help_text="Secondary/accent dark blue")
    accent_color = models.CharField(max_length=30, default='#10b981', help_text="Highlight/success accent")
    background_color = models.CharField(max_length=30, default='#ffffff')
    text_color = models.CharField(max_length=30, default='#1e293b')
    font_family = models.CharField(max_length=100, default='Poppins, sans-serif')
    font_size_base = models.CharField(max_length=20, default='16px')
    header_style = models.CharField(max_length=50, choices=HEADER_STYLES, default='modern')
    footer_style = models.CharField(max_length=50, choices=FOOTER_STYLES, default='multi-column')
    
    # Banner / Hero section
    banner_image = models.ImageField(upload_to='clinics/banners/', null=True, blank=True)
    banner_headline = models.CharField(max_length=255, default="World-Class Dental Care for Your Perfect Smile")
    banner_subheadline = models.TextField(default="Experience painless treatments, board-certified dental surgeons, and advanced digital imaging under one roof.")
    banner_cta_text = models.CharField(max_length=100, default="Book Consultation")
    banner_secondary_cta_text = models.CharField(max_length=100, default="View Treatments")
    custom_css = models.TextField(blank=True, default="")

    # 6. WhatsApp & Floating CTAs
    enable_whatsapp_float = models.BooleanField(default=True)
    whatsapp_float_position = models.CharField(max_length=30, default='bottom-right')
    whatsapp_prefilled_message = models.CharField(max_length=255, default="Hello! I would like to book a dental appointment. Please share available slots.")
    enable_call_now_button = models.BooleanField(default=True)
    enable_sticky_appointment_bar = models.BooleanField(default=True)

    # 7. SEO Management
    seo_meta_title = models.CharField(max_length=255, blank=True, default="Premier Dental Care Clinic & Implant Center")
    seo_meta_description = models.TextField(blank=True, default="Visit our clinic for high-standard dental implants, painless root canals, cosmetic smile makeovers, and orthodontic aligners. Book your visit online.")
    seo_keywords = models.TextField(blank=True, default="dental clinic, dentist near me, dental implants, root canal, teeth whitening, clear aligners, cosmetic dentistry")
    seo_robots_txt = models.TextField(blank=True, default="User-agent: *\nAllow: /\nSitemap: /sitemap.xml")
    seo_xml_sitemap_enabled = models.BooleanField(default=True)
    seo_og_image = models.ImageField(upload_to='clinics/seo/', null=True, blank=True)

    # 8. Publishing & Deployment
    hosting_type = models.CharField(max_length=50, default='dynamic_managed')
    ssl_status = models.CharField(max_length=50, default='active')
    published_at = models.DateTimeField(null=True, blank=True)
    last_tested_at = models.DateTimeField(null=True, blank=True)
    last_test_score = models.IntegerField(default=95)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.slug})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_public_url(self):
        return reverse('site_home', kwargs={'slug': self.slug})


class WebsitePage(models.Model):
    PAGE_TYPES = [
        ('home', 'Home'),
        ('about', 'About Us'),
        ('treatments', 'Treatments'),
        ('doctors', 'Our Doctors'),
        ('gallery', 'Gallery'),
        ('contact', 'Contact Us'),
        ('appointment', 'Appointment Booking'),
        ('custom', 'Custom Page'),
    ]

    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='pages')
    page_type = models.CharField(max_length=50, choices=PAGE_TYPES)
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150, blank=True, help_text="Leave blank for Home, or specify like 'about', 'treatments', etc.")
    nav_order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    show_in_nav = models.BooleanField(default=True)
    
    hero_title = models.CharField(max_length=200, blank=True)
    hero_subtitle = models.CharField(max_length=300, blank=True)
    hero_image = models.ImageField(upload_to='pages/heroes/', null=True, blank=True)
    
    content_html = models.TextField(blank=True)
    section_config = models.JSONField(default=dict, blank=True)

    # Page-specific SEO
    seo_title = models.CharField(max_length=255, blank=True)
    seo_description = models.TextField(blank=True)
    seo_keywords = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['clinic', 'nav_order']
        unique_together = ('clinic', 'page_type')

    def __str__(self):
        return f"{self.clinic.name} - {self.get_page_type_display()}"


class Doctor(models.Model):
    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='doctors')
    name = models.CharField(max_length=150, help_text="e.g. Dr. Robert Vance, DDS")
    qualification = models.CharField(max_length=150, default="BDS, MDS - Oral & Maxillofacial Implantology")
    specialization = models.CharField(max_length=150, default="Senior Implantologist & Dental Surgeon")
    experience_years = models.IntegerField(default=12)
    bio = models.TextField(default="Specializes in computer-guided painless implant placement, full arch restoration, and smile design with over a decade of surgical expertise.")
    photo = models.ImageField(upload_to='doctors/photos/', null=True, blank=True)
    available_days = models.CharField(max_length=100, default="Mon, Wed, Fri & Sat")
    consultation_fee = models.CharField(max_length=50, default="$40 - $60")
    appointment_enabled = models.BooleanField(default=True)
    order = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    
    # Social links
    linkedin_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)

    class Meta:
        ordering = ['clinic', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.clinic.name})"


class Treatment(models.Model):
    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='treatments')
    name = models.CharField(max_length=150, help_text="e.g. Dental Implants, Root Canal Treatment")
    slug = models.SlugField(max_length=150)
    icon_class = models.CharField(max_length=100, default="fa-solid fa-tooth")
    short_description = models.TextField(default="Permanent, lifelike replacement for missing teeth offering superior chewing efficiency and bone preservation.")
    full_description = models.TextField(default="Our advanced implantology protocol utilizes 3D surgical guides and premium grade titanium or zirconia fixtures to restore single, multiple, or full arches with natural aesthetics and lifetime reliability.")
    image = models.ImageField(upload_to='treatments/images/', null=True, blank=True)
    price_starting_at = models.CharField(max_length=80, default="From $499")
    duration = models.CharField(max_length=80, default="45 - 60 Mins")
    
    # Detail lists
    procedure_steps = models.TextField(default="1. 3D Digital CBCT Scan & Treatment Plan\n2. Gentle Computer-Guided Placement\n3. Healing & Osseointegration\n4. Custom Ceramic Crown Fitting", help_text="One step per line")
    benefits = models.TextField(default="Permanent teeth replacement\nPrevents facial bone recession\nLooks, feels & chews like natural teeth\nHigh 98% long-term success rate", help_text="One benefit per line")
    faqs = models.TextField(default="Q: Is dental implant surgery painful?\nA: Not at all! The procedure is performed under local numbing with zero discomfort.\n\nQ: How long do dental implants last?\nA: With routine oral hygiene, implants can last a lifetime.", help_text="Q&A format")
    
    is_featured = models.BooleanField(default=True, help_text="Show on Homepage featured treatments")
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['clinic', 'order', 'name']
        unique_together = ('clinic', 'slug')

    def __str__(self):
        return f"{self.name} - {self.clinic.name}"

    def get_steps_list(self):
        return [s.strip() for s in self.procedure_steps.split('\n') if s.strip()]

    def get_benefits_list(self):
        return [b.strip() for b in self.benefits.split('\n') if b.strip()]

    def get_faqs_list(self):
        items = []
        cur_q = None
        cur_a = []
        for line in self.faqs.split('\n'):
            line = line.strip()
            if not line:
                continue
            if line.upper().startswith('Q:') or line.upper().startswith('Q.'):
                if cur_q:
                    items.append({'q': cur_q, 'a': ' '.join(cur_a)})
                cur_q = line[2:].strip()
                cur_a = []
            elif line.upper().startswith('A:') or line.upper().startswith('A.'):
                cur_a.append(line[2:].strip())
            else:
                if cur_q:
                    cur_a.append(line)
        if cur_q:
            items.append({'q': cur_q, 'a': ' '.join(cur_a)})
        return items


class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('clinic_interior', 'Clinic Interior & Operatory'),
        ('equipment', 'Modern Dental Equipment'),
        ('before_after', 'Before & After Smile Makeovers'),
        ('happy_patients', 'Happy Patient Stories'),
    ]

    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='gallery_items')
    title = models.CharField(max_length=150, default="Modern Operatory Suite")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='clinic_interior')
    image = models.ImageField(upload_to='gallery/images/', null=True, blank=True)
    before_image = models.ImageField(upload_to='gallery/before_after/', null=True, blank=True, help_text="For Before & After transformations")
    after_image = models.ImageField(upload_to='gallery/before_after/', null=True, blank=True)
    description = models.CharField(max_length=255, blank=True, default="Hygienic sterilised private operatory")
    alt_text = models.CharField(max_length=150, blank=True, default="Modern dental clinic treatment room")
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['clinic', 'order', '-id']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class AppointmentEnquiry(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending Review'),
        ('confirmed', 'Appointment Confirmed'),
        ('completed', 'Visit Completed'),
        ('cancelled', 'Cancelled'),
    ]

    TIME_SLOTS = [
        ('morning', 'Morning (9:00 AM – 12:00 PM)'),
        ('afternoon', 'Afternoon (12:00 PM – 4:00 PM)'),
        ('evening', 'Evening (4:00 PM – 7:30 PM)'),
    ]

    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='enquiries')
    patient_name = models.CharField(max_length=150)
    mobile_number = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    appointment_date = models.DateField()
    preferred_time = models.CharField(max_length=50, choices=TIME_SLOTS, default='morning')
    treatment = models.CharField(max_length=150, blank=True, default="General Consultation")
    doctor = models.CharField(max_length=150, blank=True, default="Any Available Specialist")
    message = models.TextField(blank=True)
    
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    admin_notes = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.patient_name} - {self.appointment_date} ({self.clinic.name})"

    def get_whatsapp_reply_url(self):
        phone = ''.join(c for c in self.mobile_number if c.isdigit())
        msg = f"Hello {self.patient_name}, thank you for contacting {self.clinic.name}. Regarding your appointment on {self.appointment_date} for {self.treatment}:"
        from urllib.parse import quote
        return f"https://wa.me/{phone}?text={quote(msg)}"


class WebsiteTestReport(models.Model):
    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='test_reports')
    run_date = models.DateTimeField(auto_now_add=True)
    overall_score = models.IntegerField(default=100)
    passed_checks = models.IntegerField(default=0)
    failed_checks = models.IntegerField(default=0)
    warning_checks = models.IntegerField(default=0)
    results_json = models.JSONField(default=list)
    summary_text = models.TextField(blank=True)

    class Meta:
        ordering = ['-run_date']

    def __str__(self):
        return f"Test for {self.clinic.name} - Score {self.overall_score}% ({self.run_date.strftime('%Y-%m-%d %H:%M')})"


class DeploymentLog(models.Model):
    clinic = models.ForeignKey(ClinicWebsite, on_delete=models.CASCADE, related_name='deployments')
    deployed_at = models.DateTimeField(auto_now_add=True)
    target_domain = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default='Success')
    export_bundle_path = models.CharField(max_length=300, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-deployed_at']

    def __str__(self):
        return f"{self.clinic.name} deployed to {self.target_domain} at {self.deployed_at}"
