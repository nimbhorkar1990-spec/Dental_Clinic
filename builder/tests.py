import io
import zipfile
from datetime import date, timedelta
from django.test import TestCase, Client
from django.urls import reverse

from .models import (
    ThemeTemplate, ClinicWebsite, WebsitePage, Doctor, 
    Treatment, GalleryItem, AppointmentEnquiry, WebsiteTestReport
)

class DentalClinicBuilderTests(TestCase):
    def setUp(self):
        self.client = Client()

        # Create theme
        self.theme = ThemeTemplate.objects.create(
            name='Aura Dental Test Theme',
            slug='aura-dental-test',
            description='Test theme',
            primary_color='#0ea5e9',
            secondary_color='#0369a1',
            accent_color='#10b981',
            font_family='Poppins, sans-serif'
        )

        # Create clinic
        self.clinic = ClinicWebsite.objects.create(
            name='Test Dental Clinic',
            slug='test-dental-clinic',
            tagline='Painless Smile Specialists',
            phone='+1 (800) 555-0199',
            whatsapp_number='18005550199',
            email='test@clinic.com',
            address='100 Medical Plaza, NY',
            theme=self.theme,
            status='published'
        )

        # Create the 7 standard pages
        pages = [
            ('home', 'Home', ''),
            ('about', 'About Us', 'about'),
            ('treatments', 'Treatments', 'treatments'),
            ('doctors', 'Our Doctors', 'doctors'),
            ('gallery', 'Gallery', 'gallery'),
            ('contact', 'Contact Us', 'contact'),
            ('appointment', 'Appointment Booking', 'book-appointment'),
        ]
        for idx, (ptype, title, slug) in enumerate(pages, 1):
            WebsitePage.objects.create(
                clinic=self.clinic,
                page_type=ptype,
                title=title,
                slug=slug,
                nav_order=idx,
                is_active=True,
                show_in_nav=True
            )

        # Create doctor
        self.doctor = Doctor.objects.create(
            clinic=self.clinic,
            name='Dr. Test Surgeon',
            qualification='BDS, MDS',
            specialization='Chief Oral Surgeon',
            experience_years=10,
            available_days='Mon-Fri',
            consultation_fee='$50'
        )

        # Create treatment
        self.treatment = Treatment.objects.create(
            clinic=self.clinic,
            name='Dental Implants Test',
            slug='dental-implants-test',
            short_description='Permanent tooth replacement',
            price_starting_at='From $799',
            duration='45 Mins',
            is_featured=True
        )

        # Create gallery item
        self.gallery = GalleryItem.objects.create(
            clinic=self.clinic,
            title='Clean Operatory',
            category='clinic_interior',
            alt_text='Sterile operatory'
        )

    def test_dashboard_overview_loads(self):
        response = self.client.get(reverse('dashboard_overview'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Dental Clinic')
        self.assertContains(response, 'Dashboard Overview')

    def test_create_new_website_automation(self):
        response = self.client.post(reverse('website_create'), {
            'name': 'Elite Smile Studio',
            'slug': 'elite-smile-studio',
            'tagline': 'Luxury Cosmetic Dentistry',
            'phone': '+1 (800) 555-9988',
            'whatsapp_number': '18005559988',
            'email': 'care@elitesmile.com',
            'address': '500 Fifth Avenue, Suite 10, NY 10036',
            'theme': self.theme.id,
        })
        self.assertEqual(response.status_code, 302)
        new_clinic = ClinicWebsite.objects.filter(slug='elite-smile-studio').first()
        self.assertIsNotNone(new_clinic)
        # Verify 7 standard pages were automatically created
        self.assertEqual(new_clinic.pages.count(), 7)
        # Verify standard treatments were seeded
        self.assertTrue(new_clinic.treatments.count() >= 8)
        # Verify doctors were seeded
        self.assertTrue(new_clinic.doctors.count() >= 3)

    def test_duplicate_website(self):
        response = self.client.get(reverse('website_duplicate', kwargs={'clinic_id': self.clinic.id}))
        self.assertEqual(response.status_code, 302)
        clone = ClinicWebsite.objects.filter(slug__startswith='test-dental-clinic-copy').first()
        self.assertIsNotNone(clone)
        self.assertEqual(clone.pages.count(), 7)

    def test_customization_update(self):
        response = self.client.post(reverse('customization_view'), {
            'primary_color': '#10b981',
            'secondary_color': '#047857',
            'accent_color': '#34d399',
            'background_color': '#ffffff',
            'text_color': '#1e293b',
            'font_family': 'Inter, sans-serif',
            'font_size_base': '16px',
            'header_style': 'modern',
            'footer_style': 'multi-column',
            'banner_headline': 'New Customized Dental Headline',
            'banner_subheadline': 'New Customized Dental Subheadline',
            'banner_cta_text': 'Book Now',
            'banner_secondary_cta_text': 'View Details',
        })
        self.assertEqual(response.status_code, 302)
        self.clinic.refresh_from_db()
        self.assertEqual(self.clinic.primary_color, '#10b981')
        self.assertEqual(self.clinic.banner_headline, 'New Customized Dental Headline')

    def test_public_pages_rendering(self):
        # 1. Home
        res = self.client.get(reverse('site_home', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Test Dental Clinic')

        # 2. About
        res = self.client.get(reverse('site_about', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)

        # 3. Treatments
        res = self.client.get(reverse('site_treatments', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Dental Implants Test')

        # Treatment Detail
        res = self.client.get(reverse('site_treatment_detail', kwargs={'slug': self.clinic.slug, 'treatment_slug': self.treatment.slug}))
        self.assertEqual(res.status_code, 200)

        # 4. Doctors
        res = self.client.get(reverse('site_doctors', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Dr. Test Surgeon')

        # 5. Gallery
        res = self.client.get(reverse('site_gallery', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)

        # 6. Contact
        res = self.client.get(reverse('site_contact', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)

        # 7. Appointment Booking
        res = self.client.get(reverse('site_appointment', kwargs={'slug': self.clinic.slug}))
        self.assertEqual(res.status_code, 200)

    def test_submit_appointment_enquiry(self):
        tomorrow = date.today() + timedelta(days=1)
        response = self.client.post(reverse('site_submit_appointment', kwargs={'slug': self.clinic.slug}), {
            'patient_name': 'Alice Williams',
            'mobile_number': '+1 (555) 333-4444',
            'email': 'alice@example.com',
            'appointment_date': tomorrow.strftime('%Y-%m-%d'),
            'preferred_time': 'morning',
            'treatment': 'Dental Implants Test',
            'doctor': 'Dr. Test Surgeon',
            'message': 'Need lower jaw implant consult',
        })
        self.assertEqual(response.status_code, 302)
        enquiry = AppointmentEnquiry.objects.filter(patient_name='Alice Williams').first()
        self.assertIsNotNone(enquiry)
        self.assertEqual(enquiry.clinic, self.clinic)
        self.assertEqual(enquiry.treatment, 'Dental Implants Test')
        # Check WhatsApp reply generator
        self.assertIn('wa.me', enquiry.get_whatsapp_reply_url())

    def test_run_website_quality_audit(self):
        response = self.client.post(reverse('run_website_test_by_id', kwargs={'clinic_id': self.clinic.id}))
        self.assertEqual(response.status_code, 302)
        report = WebsiteTestReport.objects.filter(clinic=self.clinic).first()
        self.assertIsNotNone(report)
        self.assertTrue(report.overall_score >= 80)
        self.assertTrue(report.passed_checks > 10)

    def test_export_website_zip(self):
        response = self.client.get(reverse('export_website_zip_by_id', kwargs={'clinic_id': self.clinic.id}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/zip')

        # Inspect zip contents
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        file_list = zip_file.namelist()
        self.assertIn('index.html', file_list)
        self.assertIn('about.html', file_list)
        self.assertIn('treatments.html', file_list)
        self.assertIn('doctors.html', file_list)
        self.assertIn('gallery.html', file_list)
        self.assertIn('contact.html', file_list)
        self.assertIn('book-appointment.html', file_list)
        self.assertIn('sitemap.xml', file_list)
        self.assertIn('robots.txt', file_list)
        self.assertIn('README.txt', file_list)
