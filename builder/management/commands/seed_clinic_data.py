from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from builder.models import (
    ThemeTemplate, ClinicWebsite, WebsitePage, Doctor, 
    Treatment, GalleryItem, AppointmentEnquiry, WebsiteTestReport, DeploymentLog
)

class Command(BaseCommand):
    help = 'Seeds initial dental themes, sample clinic websites, pages, doctors, treatments, and enquiries'

    def handle(self, *args, **options):
        self.stdout.write("Seeding Dental Clinic Website Builder Data...")

        # 1. Create Themes
        themes_data = [
            {
                'name': 'Aura Dental (Modern Light Blue)',
                'slug': 'aura-dental',
                'description': 'Modern, high-tech dental clinic theme with crisp cyan/sky blue accents, rounded cards, floating appointment badges, and clean typography.',
                'category': 'Modern Technology',
                'primary_color': '#0ea5e9',
                'secondary_color': '#0369a1',
                'accent_color': '#0284c7',
                'background_color': '#ffffff',
                'text_color': '#0f172a',
                'font_family': 'Poppins, sans-serif',
                'is_system_default': True,
                'custom_css': ':root { --theme-radius: 14px; --theme-shadow: 0 10px 25px -5px rgba(14, 165, 233, 0.15); }',
            },
            {
                'name': 'Zenith Smile (White & Soft Green)',
                'slug': 'zenith-smile',
                'description': 'Soothing, organic wellness & holistic dental theme with refreshing soft mint green, calm aesthetics, gentle curves, and relaxing vibe.',
                'category': 'Holistic & Family',
                'primary_color': '#10b981',
                'secondary_color': '#047857',
                'accent_color': '#34d399',
                'background_color': '#f8fafc',
                'text_color': '#1e293b',
                'font_family': 'Inter, sans-serif',
                'is_system_default': False,
                'custom_css': ':root { --theme-radius: 18px; --theme-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.12); }',
            },
            {
                'name': 'Royal Care Dental (Navy Blue & Gold)',
                'slug': 'royal-care',
                'description': 'Prestigious, luxury dental surgical specialist theme with executive deep navy blue, warm gold accents, and authoritative styling.',
                'category': 'Executive & Surgical',
                'primary_color': '#1e3a8a',
                'secondary_color': '#172554',
                'accent_color': '#f59e0b',
                'background_color': '#ffffff',
                'text_color': '#0f172a',
                'font_family': 'Montserrat, sans-serif',
                'is_system_default': False,
                'custom_css': ':root { --theme-radius: 8px; --theme-shadow: 0 10px 30px -5px rgba(30, 58, 138, 0.18); }',
            },
        ]

        themes_dict = {}
        for td in themes_data:
            theme, created = ThemeTemplate.objects.update_or_create(
                slug=td['slug'],
                defaults=td
            )
            themes_dict[theme.slug] = theme
            self.stdout.write(f"  - Theme: {theme.name} ({'Created' if created else 'Updated'})")

        # 2. Seed Primary Clinic: Apex Dental Care & Implant Center
        apex_theme = themes_dict['aura-dental']
        apex_clinic, created = ClinicWebsite.objects.update_or_create(
            slug='apex-dental',
            defaults={
                'name': 'Apex Dental Care & Implant Center',
                'tagline': 'Advanced Implantology, Gentle Care & Radiant Smiles',
                'domain_name': 'www.apexdentalcare.com',
                'status': 'published',
                'theme': apex_theme,
                'phone': '+91 7499077170',
                'whatsapp_number': '917499077170',
                'email': 'care@apexdentalcare.com',
                'address': 'Suite 400, 750 Health Plaza Blvd, Medical District, NY 10001',
                'google_maps_embed': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.119763973046!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1680000000000!5m2!1sen!2sus',
                'working_hours': 'Monday – Friday: 8:30 AM – 7:30 PM\nSaturday: 9:00 AM – 5:00 PM\nSunday: Emergency Care Only',
                'emergency_contact': '+1 (800) 555-3399',
                'facebook_url': 'https://facebook.com/apexdentalcare',
                'instagram_url': 'https://instagram.com/apexdentalcare',
                'twitter_url': 'https://twitter.com/apexdentalcare',
                'youtube_url': 'https://youtube.com/c/apexdentalcare',
                'linkedin_url': 'https://linkedin.com/company/apexdentalcare',
                'about_short': 'Welcome to Apex Dental Care & Implant Center. We deliver state-of-the-art painless dentistry, specialized implant surgery, and comprehensive cosmetic smile transformations with compassionate care.',
                'about_full': 'Founded in 2012 by Dr. Robert Vance, Apex Dental Care has grown into the region’s premier oral healthcare center. Featuring 3D digital CBCT imaging, in-house CAD/CAM porcelain milling, and a sterile surgical operatory suite, our team delivers predictable, long-lasting clinical results in a comforting, anxiety-free atmosphere.',
                'mission': 'To deliver the highest echelon of gentle, pain-free dental healthcare through cutting-edge digital technology, certified dental surgeons, and strict medical sterilization.',
                'vision': 'To set the gold standard in modern aesthetic and restorative dentistry while making premier clinical oral healthcare accessible and comfortable for every family.',
                'history_founded_year': '2012',
                'facilities_text': 'Ultra-low Radiation 3D Digital CBCT Imaging, Computer-Guided Implant Navigations, Painless Computerized Anesthesia Delivery, Class-B European Autoclave Sterilization, Zero-Wait Private Lounges.',
                'primary_color': '#0ea5e9',
                'secondary_color': '#0369a1',
                'accent_color': '#10b981',
                'background_color': '#ffffff',
                'text_color': '#0f172a',
                'font_family': 'Poppins, sans-serif',
                'font_size_base': '16px',
                'header_style': 'modern',
                'footer_style': 'multi-column',
                'banner_headline': 'World-Class Dental Excellence for Your Confident Smile',
                'banner_subheadline': 'Board-certified dental surgeons, computerized zero-pain anesthesia, and same-day dental crowns. Transform your dental wellness today.',
                'banner_cta_text': 'Book Appointment',
                'banner_secondary_cta_text': 'Explore Treatments',
                'enable_whatsapp_float': True,
                'whatsapp_float_position': 'bottom-right',
                'whatsapp_prefilled_message': 'Hello Apex Dental, I would like to book a dental checkup and consultation. Please share available dates.',
                'enable_call_now_button': True,
                'enable_sticky_appointment_bar': True,
                'seo_meta_title': 'Apex Dental Care & Implant Center | Top Rated Dental Clinic',
                'seo_meta_description': 'Award-winning dental clinic offering painless dental implants, root canal treatments, Invisalign aligners, and cosmetic dentistry. Book your appointment online.',
                'seo_keywords': 'dental clinic, dentist in NY, dental implants, root canal specialist, teeth whitening, clear aligners, pain-free dentistry',
                'seo_robots_txt': 'User-agent: *\nAllow: /\nSitemap: https://www.apexdentalcare.com/sitemap.xml',
                'seo_xml_sitemap_enabled': True,
                'hosting_type': 'dynamic_managed',
                'ssl_status': 'active',
                'published_at': timezone.now(),
                'last_tested_at': timezone.now(),
                'last_test_score': 98,
            }
        )
        self.stdout.write(f"  - Clinic: {apex_clinic.name} ({'Created' if created else 'Updated'})")

        # 3. Seed 7 Standard Pages for Apex Dental
        standard_pages = [
            {
                'page_type': 'home',
                'title': 'Home',
                'slug': '',
                'nav_order': 1,
                'hero_title': 'World-Class Dental Care & Implant Center',
                'hero_subtitle': 'Painless treatments, board-certified surgeons, and cutting-edge 3D digital dentistry.',
                'seo_title': 'Apex Dental Care | Home of Radiant Smiles',
                'seo_description': 'Experience gentle, modern dentistry with our experienced specialists. Schedule your visit today.',
                'seo_keywords': 'dentist home, best dental clinic, dental implants, teeth whitening',
            },
            {
                'page_type': 'about',
                'title': 'About Us',
                'slug': 'about',
                'nav_order': 2,
                'hero_title': 'About Apex Dental Care',
                'hero_subtitle': 'A decade of clinical excellence, medical-grade hygiene, and compassionate patient relationships.',
                'seo_title': 'About Us | Apex Dental Care & Implant Center',
                'seo_description': 'Learn about our history, our philosophy of gentle dentistry, and our surgical facility.',
                'seo_keywords': 'about dental clinic, dental surgeons, clinic history, clinic mission',
            },
            {
                'page_type': 'treatments',
                'title': 'Treatments',
                'slug': 'treatments',
                'nav_order': 3,
                'hero_title': 'Comprehensive Dental Treatments',
                'hero_subtitle': 'From preventive cleanings to full-mouth dental implants and cosmetic makeovers.',
                'seo_title': 'Dental Treatments & Procedures | Apex Dental',
                'seo_description': 'Explore our full spectrum of specialized dental treatments: implants, RCT, aligners, veneers, crowns.',
                'seo_keywords': 'dental treatments, tooth extraction, root canal, dental implants cost, braces',
            },
            {
                'page_type': 'doctors',
                'title': 'Our Doctors',
                'slug': 'doctors',
                'nav_order': 4,
                'hero_title': 'Meet Our Dental Specialists',
                'hero_subtitle': 'A dedicated multidisciplinary team of board-certified dental surgeons and prosthodontists.',
                'seo_title': 'Our Doctors & Dental Specialists | Apex Dental',
                'seo_description': 'Meet our oral surgeons, orthodontists, endodontists, and cosmetic dentists.',
                'seo_keywords': 'dental doctors, implantologist, orthodontist, endodontist dentist',
            },
            {
                'page_type': 'gallery',
                'title': 'Gallery',
                'slug': 'gallery',
                'nav_order': 5,
                'hero_title': 'Clinic Tour & Smile Transformations',
                'hero_subtitle': 'Explore our modern sterilization suites, patient lounges, and real before-after results.',
                'seo_title': 'Smile Gallery & Clinic Photographs | Apex Dental',
                'seo_description': 'View our before-and-after smile makeover photographs and high-tech operatory facilities.',
                'seo_keywords': 'dental photos, before after teeth, smile makeover gallery, dental clinic interior',
            },
            {
                'page_type': 'contact',
                'title': 'Contact Us',
                'slug': 'contact',
                'nav_order': 6,
                'hero_title': 'Get In Touch',
                'hero_subtitle': 'We are located centrally with valet parking and direct subway access. Contact us 24/7.',
                'seo_title': 'Contact Apex Dental Care | Address, Map & Hours',
                'seo_description': 'Contact Apex Dental Care for inquiries, directions, or emergency appointments.',
                'seo_keywords': 'dental clinic contact, dentist phone number, dentist address, emergency dental contact',
            },
            {
                'page_type': 'appointment',
                'title': 'Appointment Booking',
                'slug': 'book-appointment',
                'nav_order': 7,
                'hero_title': 'Book Your Dental Consultation',
                'hero_subtitle': 'Select your preferred time slot and treatment. Instant WhatsApp confirmation available.',
                'seo_title': 'Book Dental Appointment Online | Apex Dental',
                'seo_description': 'Quick, hassle-free online dental appointment booking with instant confirmation.',
                'seo_keywords': 'book dentist appointment, dental consultation booking, schedule dentist online',
            },
        ]

        for pdata in standard_pages:
            page, p_created = WebsitePage.objects.update_or_create(
                clinic=apex_clinic,
                page_type=pdata['page_type'],
                defaults=pdata
            )
            self.stdout.write(f"    - Page: {page.title}")

        # 4. Seed Doctors for Apex Dental
        doctors_data = [
            {
                'name': 'Dr. Robert Vance, DDS, FICOI',
                'qualification': 'BDS, MDS - Oral & Maxillofacial Implantology',
                'specialization': 'Chief Surgeon & Senior Implantologist',
                'experience_years': 15,
                'bio': 'Fellow of the International Congress of Oral Implantologists (FICOI) with over 4,500 successful computer-guided implant restorations. Specializes in full-arch rehabilitation.',
                'available_days': 'Mon, Wed, Fri & Sat',
                'consultation_fee': '$65',
                'appointment_enabled': True,
                'order': 1,
            },
            {
                'name': 'Dr. Elena Rostova, DMD, MS',
                'qualification': 'BDS, MDS - Orthodontics & Dentofacial Orthopedics',
                'specialization': 'Certified Diamond Invisalign Specialist',
                'experience_years': 11,
                'bio': 'Pioneered custom 3D aligner workflows and lingual orthodontic aesthetics. Passionate about creating harmonious, balanced facial aesthetics for teens and adults.',
                'available_days': 'Tue, Thu & Sat',
                'consultation_fee': '$50',
                'appointment_enabled': True,
                'order': 2,
            },
            {
                'name': 'Dr. Marcus Sterling, DDS',
                'qualification': 'BDS, MDS - Conservative Dentistry & Endodontics',
                'specialization': 'Microscopic Endodontist (Root Canal Specialist)',
                'experience_years': 13,
                'bio': 'Specializes in single-visit microscopic root canal therapies with zero pain protocols, tooth preservation, and digital laser endodontics.',
                'available_days': 'Mon to Fri',
                'consultation_fee': '$55',
                'appointment_enabled': True,
                'order': 3,
            },
            {
                'name': 'Dr. Chloe Bennett, DDS, AACD',
                'qualification': 'BDS - Aesthetic & Restorative Dentistry',
                'specialization': 'Cosmetic Dentist & Smile Makeover Artist',
                'experience_years': 9,
                'bio': 'Accredited member of the American Academy of Cosmetic Dentistry. Known for ultra-thin porcelain veneers, laser teeth whitening, and non-invasive smile aesthetics.',
                'available_days': 'Mon, Tue, Thu & Fri',
                'consultation_fee': '$50',
                'appointment_enabled': True,
                'order': 4,
            },
        ]

        for doc_data in doctors_data:
            doc, d_created = Doctor.objects.update_or_create(
                clinic=apex_clinic,
                name=doc_data['name'],
                defaults=doc_data
            )
            self.stdout.write(f"    - Doctor: {doc.name}")

        # 5. Seed 8 Core Dental Treatments for Apex Dental
        treatments_data = [
            {
                'name': 'Dental Implants',
                'slug': 'dental-implants',
                'icon_class': 'fa-solid fa-tooth',
                'short_description': 'Permanent titanium or zirconia tooth root replacements that look, feel, and function like natural teeth.',
                'full_description': 'Our 3D computer-guided dental implant procedure ensures pinpoint surgical accuracy and rapid healing. Whether replacing a single missing tooth or undergoing a full All-on-4 or All-on-6 smile restoration, dental implants prevent jawbone resorption and restore 100% biting efficiency.',
                'price_starting_at': 'From $899',
                'duration': '45 – 60 Mins',
                'procedure_steps': '1. High-resolution 3D CBCT digital scan & virtual bone analysis\n2. Minimally invasive computer-guided implant fixture placement\n3. Biocompatible osseointegration healing period\n4. Precision milled ceramic crown attachment and bite check',
                'benefits': 'Permanent lifelong tooth replacement\nPrevents bone loss and facial sagging\nRestores full chewing power with zero dietary restrictions\nIndependent care that does not harm adjacent teeth',
                'faqs': 'Q: Is dental implant surgery painful?\nA: The procedure is carried out under computerized local numbing and is virtually painless. Most patients resume work the next day.\n\nQ: How long do dental implants last?\nA: With routine oral hygiene and annual checkups, dental implants are engineered to last a lifetime.',
                'is_featured': True,
                'order': 1,
            },
            {
                'name': 'Root Canal Treatment',
                'slug': 'root-canal-treatment',
                'icon_class': 'fa-solid fa-shield-virus',
                'short_description': 'Gentle microscopic therapy to save severely infected teeth and eliminate dental pain in a single comfortable visit.',
                'full_description': 'Forget the old myths! Modern microscopic root canal treatment at Apex Dental is as routine and gentle as getting a small filling. Using high-magnification dental surgical microscopes and ultrasonic rotary instruments, we thoroughly clean infected root canals, sanitize them with medical laser, and seal them securely.',
                'price_starting_at': 'From $350',
                'duration': '40 – 50 Mins',
                'procedure_steps': '1. Digital radiographic assessment of root canals\n2. Complete pain-free numbing of the target area\n3. Microscopic cleaning, disinfection, and shaping of the root canals\n4. Biocompatible hermetic obturation seal and protective crown prep',
                'benefits': 'Instantly relieves severe throbbing tooth pain\nSaves your natural tooth from extraction\nPrevents infection from spreading into the jawbone\nCompleted comfortably in a single relaxed visit',
                'faqs': 'Q: Will I feel pain during the root canal?\nA: No. We utilize computer-assisted anesthesia delivery so that the area is fully numb before we begin.\n\nQ: Why do I need a crown after a root canal?\nA: A crown protects the treated tooth from heavy chewing forces and prevents fractures.',
                'is_featured': True,
                'order': 2,
            },
            {
                'name': 'Teeth Whitening',
                'slug': 'teeth-whitening',
                'icon_class': 'fa-solid fa-wand-magic-sparkles',
                'short_description': 'Professional laser whitening delivering up to 8 shades brighter in under 45 minutes with zero enamel damage.',
                'full_description': 'Erase years of coffee, tea, wine, and tobacco stains safely and evenly. Our in-office Philips Zoom laser whitening combines specialized light-activated whitening gel with desensitizing agents to deliver dazzling, vibrant smiles without sensitivity.',
                'price_starting_at': 'From $199',
                'duration': '45 Mins',
                'procedure_steps': '1. Pre-whitening shade assessment and tooth cleaning\n2. Gum protection barrier application\n3. Light-activated whitening gel application in 3 fifteen-minute cycles\n4. Nourishing enamel remineralization and post-care kit',
                'benefits': 'Up to 8 shades whiter in just 45 minutes\nSafe for tooth enamel with advanced anti-sensitivity formula\nEven, brilliant whitening results that outshine OTC kits\nLong-lasting results with provided home touch-up trays',
                'faqs': 'Q: Does laser teeth whitening hurt?\nA: Most patients experience zero discomfort. Our specialized post-treatment gel eliminates tooth sensitivity.',
                'is_featured': True,
                'order': 3,
            },
            {
                'name': 'Braces and Aligners',
                'slug': 'braces-and-aligners',
                'icon_class': 'fa-solid fa-grip-lines',
                'short_description': 'Discreet clear aligners and modern ceramic braces for beautifully aligned teeth and optimal bite mechanics.',
                'full_description': 'Straighten your teeth without metal brackets or wires. Our certified Invisalign clear aligners are virtually invisible, custom 3D printed, and completely removable for meals and brushing. We also offer low-profile ceramic aesthetic braces for complex bite corrections.',
                'price_starting_at': 'From $1,499',
                'duration': '6 – 14 Months',
                'procedure_steps': '1. 3D iTero intraoral digital smile scan\n2. Computerized ClinCheck simulation showing your teeth moving into place\n3. Custom clear aligner fabrication\n4. Periodic progress checkups every 6 to 8 weeks',
                'benefits': '100% clear and virtually invisible while talking\nRemovable for eating your favorite foods\nNo painful metal wires poking cheeks or gums\nFaster treatment timelines with smart 3D tracking',
                'faqs': 'Q: How many hours a day should I wear clear aligners?\nA: You should wear them 20 to 22 hours per day, removing them only to eat and brush.',
                'is_featured': True,
                'order': 4,
            },
            {
                'name': 'Cosmetic Dentistry',
                'slug': 'cosmetic-dentistry',
                'icon_class': 'fa-solid fa-face-smile',
                'short_description': 'Handcrafted porcelain veneers, composite bonding, and digital smile makeovers tailored to your facial harmony.',
                'full_description': 'Whether you have chipped, discolored, misaligned, or uneven teeth, our cosmetic dentistry team creates life-changing smile makeovers. Using ultra-thin custom ceramic veneers and digital smile design simulations, we craft a radiant smile that looks effortlessly natural.',
                'price_starting_at': 'From $599',
                'duration': '2 Visits',
                'procedure_steps': '1. Comprehensive facial aesthetic and smile line design\n2. Conservative, minimal enamel preparation\n3. Temporary aesthetic preview mock-up\n4. Permanent bonding of custom artisan porcelain veneers',
                'benefits': 'Corrects chips, cracks, gaps, and severe stains\nCustom tailored to your skin tone and facial symmetry\nStain-resistant porcelain retains luminosity for 15+ years\nBoosts self-esteem and social confidence',
                'faqs': 'Q: How long do porcelain veneers last?\nA: High-grade porcelain veneers typically last between 15 and 20 years with proper oral care.',
                'is_featured': True,
                'order': 5,
            },
            {
                'name': 'Dental Crowns & Bridges',
                'slug': 'dental-crowns',
                'icon_class': 'fa-solid fa-crown',
                'short_description': 'Same-day digital CAD/CAM zirconia and porcelain crowns providing supreme structural strength and lifelike realism.',
                'full_description': 'Restore broken, heavily filled, or fractured teeth with our German zirconia and all-ceramic crowns. Precision scanned with 3D intraoral lasers and milled in our lab, our crowns provide seamless margins, natural translucency, and long-term durability.',
                'price_starting_at': 'From $450',
                'duration': 'Same-Day or 2 Visits',
                'procedure_steps': '1. Digital intraoral scanning (no messy impression trays!)\n2. CAD digital design of crown morphology\n3. Precision milling from monolithic zirconia block\n4. Permanent adhesive bonding and margin polishing',
                'benefits': 'Prevents damaged or cracked teeth from fracturing\nMatches the exact color, texture, and light translucency of natural teeth\nBiocompatible and metal-free (no dark gum lines!)\nLong-term structural reliability',
                'faqs': 'Q: Will my dental crown look fake?\nA: No! We match the exact shade, gradients, and translucency of your adjacent teeth.',
                'is_featured': True,
                'order': 6,
            },
            {
                'name': 'Teeth Cleaning & Prevention',
                'slug': 'teeth-cleaning',
                'icon_class': 'fa-solid fa-sparkles',
                'short_description': 'Advanced ultrasonic scaling, air polishing, and deep gum therapy to prevent periodontal disease and keep breath fresh.',
                'full_description': 'Routine professional teeth cleaning removes stubborn tartar (calculus) and bio-film that cannot be removed by home brushing alone. Our gentle piezo-ultrasonic scalers and glycine air polishers leave your teeth smooth, sparkling, and free from bacterial plaque.',
                'price_starting_at': 'From $99',
                'duration': '30 – 40 Mins',
                'procedure_steps': '1. Comprehensive periodontal gum pocket evaluation\n2. Piezo-ultrasonic plaque and calculus removal\n3. Gentle air-flow stain removal and polishing\n4. Enamel strengthening fluoride treatment',
                'benefits': 'Prevents gum bleeding, gingivitis, and periodontitis\nEliminates chronic bad breath (halitosis)\nRemoves tough coffee and tobacco surface stains\nProtects overall cardiovascular wellness',
                'faqs': 'Q: How often should I get my teeth cleaned?\nA: The American Dental Association recommends a professional cleaning every 6 months.',
                'is_featured': False,
                'order': 7,
            },
            {
                'name': 'Pediatric Dentistry',
                'slug': 'pediatric-dentistry',
                'icon_class': 'fa-solid fa-child',
                'short_description': 'Gentle, fun, and fear-free dental visits for toddlers, children, and teens in our dedicated colorful operatory.',
                'full_description': 'We believe positive childhood dental experiences build lifelong healthy dental habits. Our specialized pediatric dentists utilize tell-show-do communication, painless techniques, dental sealants, and cavity prevention to keep little smiles glowing and confident.',
                'price_starting_at': 'From $85',
                'duration': '30 Mins',
                'procedure_steps': '1. Welcoming kid-friendly dental tour and orientation\n2. Gentle examination of teeth, jaws, and bite development\n3. Protective cavity-preventing dental sealants application\n4. Fun brushing coaching and kid celebration gift',
                'benefits': 'Fear-free environment builds positive healthcare attitudes\nPrevents early childhood cavities with fluoride and sealants\nEarly interception of orthodontic alignment issues\nFriendly team dedicated specifically to kids',
                'faqs': 'Q: When should my child have their first dental visit?\nA: As soon as their first baby tooth emerges, or by their first birthday.',
                'is_featured': False,
                'order': 8,
            },
        ]

        for tdata in treatments_data:
            t, t_created = Treatment.objects.update_or_create(
                clinic=apex_clinic,
                slug=tdata['slug'],
                defaults=tdata
            )
            self.stdout.write(f"    - Treatment: {t.name}")

        # 6. Seed Gallery Items for Apex Dental
        gallery_data = [
            {
                'title': 'High-Tech Digital Operatory Suite',
                'category': 'clinic_interior',
                'description': 'Ergonomic surgical chairs with ceiling-mounted entertainment displays and HEPA air purification.',
                'alt_text': 'Modern sterile dental clinic treatment room',
                'order': 1,
            },
            {
                'title': 'Class-B European Sterilization Suite',
                'category': 'clinic_interior',
                'description': 'Multi-stage medical sterilization with biological spore testing and sealed packaging.',
                'alt_text': 'Medical grade autoclave sterilization center',
                'order': 2,
            },
            {
                'title': '3D CBCT Digital Imaging Center',
                'category': 'equipment',
                'description': 'Ultra-low radiation 3D cone beam CT scanner for precision implant navigation.',
                'alt_text': 'Advanced 3D CBCT digital dental imaging scanner',
                'order': 3,
            },
            {
                'title': 'CAD/CAM Same-Day Porcelain Milling Unit',
                'category': 'equipment',
                'description': 'High-precision German milling technology for same-day zirconia crowns and inlays.',
                'alt_text': 'In-house CAD CAM digital crown milling unit',
                'order': 4,
            },
            {
                'title': 'Full Arch Smile Makeover (Before & After)',
                'category': 'before_after',
                'description': 'Complete aesthetic rejuvenation utilizing 8 handcrafted porcelain veneers and whitening.',
                'alt_text': 'Cosmetic porcelain veneers before and after result',
                'order': 5,
            },
            {
                'title': 'Single Tooth Implant Restoration',
                'category': 'before_after',
                'description': 'Lifelike titanium implant and custom zirconia crown seamlessly matching adjacent teeth.',
                'alt_text': 'Dental implant single tooth before and after',
                'order': 6,
            },
            {
                'title': 'Patient Review & Smile Reveal',
                'category': 'happy_patients',
                'description': 'Delighted patient following her completed 10-month Invisalign clear aligner journey.',
                'alt_text': 'Happy dental patient smiling after aligner treatment',
                'order': 7,
            },
        ]

        for gdata in gallery_data:
            g, g_created = GalleryItem.objects.update_or_create(
                clinic=apex_clinic,
                title=gdata['title'],
                defaults=gdata
            )
            self.stdout.write(f"    - Gallery: {g.title}")

        # 7. Seed Sample Appointment Enquiries for Apex Dental
        enquiries_data = [
            {
                'patient_name': 'Sarah Jenkins',
                'mobile_number': '+1 (555) 492-8812',
                'email': 'sarah.jenkins@example.com',
                'appointment_date': date.today() + timedelta(days=2),
                'preferred_time': 'morning',
                'treatment': 'Dental Implants',
                'doctor': 'Dr. Robert Vance, DDS, FICOI',
                'message': 'I have a missing lower molar on the left side and would like a consultation for an implant.',
                'status': 'confirmed',
                'admin_notes': 'Patient called and confirmed appointment for 10:00 AM. 3D scan requested.',
            },
            {
                'patient_name': 'Michael Chang',
                'mobile_number': '+1 (555) 831-2940',
                'email': 'mchang88@example.com',
                'appointment_date': date.today() + timedelta(days=3),
                'preferred_time': 'afternoon',
                'treatment': 'Braces and Aligners',
                'doctor': 'Dr. Elena Rostova, DMD, MS',
                'message': 'Interested in clear aligners for mild overcrowding in upper teeth.',
                'status': 'pending',
                'admin_notes': 'Sent initial WhatsApp welcome message and pricing brochure.',
            },
            {
                'patient_name': 'David Miller',
                'mobile_number': '+1 (555) 720-1193',
                'email': 'dmiller@example.com',
                'appointment_date': date.today() - timedelta(days=1),
                'preferred_time': 'morning',
                'treatment': 'Root Canal Treatment',
                'doctor': 'Dr. Marcus Sterling, DDS',
                'message': 'Sharp sensitivity to cold on upper right premolar.',
                'status': 'completed',
                'admin_notes': 'Single-visit endodontics completed with zero pain. Temporary filling placed, crown prep next week.',
            },
            {
                'patient_name': 'Emily Watson',
                'mobile_number': '+1 (555) 349-9921',
                'email': 'emily.w@example.com',
                'appointment_date': date.today() + timedelta(days=5),
                'preferred_time': 'evening',
                'treatment': 'Teeth Whitening',
                'doctor': 'Dr. Chloe Bennett, DDS, AACD',
                'message': 'Looking for in-office laser teeth whitening ahead of my wedding next month.',
                'status': 'confirmed',
                'admin_notes': 'Scheduled for 5:30 PM slot. Pre-whitening cleaning scheduled.',
            },
        ]

        for edata in enquiries_data:
            enq, e_created = AppointmentEnquiry.objects.get_or_create(
                clinic=apex_clinic,
                patient_name=edata['patient_name'],
                appointment_date=edata['appointment_date'],
                defaults=edata
            )
            self.stdout.write(f"    - Enquiry: {enq.patient_name} ({enq.treatment})")

        # 8. Seed Second Sample Clinic: Mint Leaf Holistic Dental Care
        zenith_theme = themes_dict['zenith-smile']
        mint_clinic, created = ClinicWebsite.objects.update_or_create(
            slug='mint-leaf-dental',
            defaults={
                'name': 'Mint Leaf Holistic Dental Studio',
                'tagline': 'Gentle Dentistry, Biocompatible Materials & Peaceful Care',
                'domain_name': 'www.mistletoedental.com',
                'status': 'draft',
                'theme': zenith_theme,
                'phone': '+1 (800) 555-7822',
                'whatsapp_number': '18005557822',
                'email': 'hello@mintleafdental.com',
                'address': 'Level 2, 420 Green Garden Avenue, Eco Wellness District, CA 90210',
                'google_maps_embed': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d193595.15830869428!2d-74.119763973046!3d40.69766374874431!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c24fa5d33f083b%3A0xc80b8f06e177fe62!2sNew%20York%2C%20NY!5e0!3m2!1sen!2sus!4v1680000000000!5m2!1sen!2sus',
                'working_hours': 'Monday – Thursday: 9:00 AM – 6:00 PM\nFriday: 9:00 AM – 4:00 PM\nSaturday & Sunday: Closed',
                'emergency_contact': '+1 (800) 555-7899',
                'facebook_url': 'https://facebook.com/mintleafdental',
                'instagram_url': 'https://instagram.com/mintleafdental',
                'twitter_url': 'https://twitter.com/mintleafdental',
                'youtube_url': 'https://youtube.com',
                'linkedin_url': 'https://linkedin.com',
                'about_short': 'Mint Leaf Holistic Dental Studio focuses on biological, metal-free dentistry, natural fluoride alternatives, and mindful care that respects your entire body.',
                'about_full': 'At Mint Leaf Dental, we integrate modern dental science with holistic body wellness. From ozone therapy and BPA-free fillings to aromatherapy operatory lounges, our gentle philosophy ensures a calming, soothing dental visit.',
                'mission': 'To nurture radiant smiles through biocompatible, eco-conscious, and compassionate dental therapeutics.',
                'vision': 'To lead wellness-driven holistic dental care where patient comfort and biological health thrive together.',
                'history_founded_year': '2018',
                'facilities_text': 'Ozone Water Disinfection, Mercury Safe Amalgam Removal Suites, Digital Low-Dose Sensors, Aromatherapy Diffusers in Every Room, Eco-Friendly Bamboo Disposables.',
                'primary_color': '#10b981',
                'secondary_color': '#047857',
                'accent_color': '#34d399',
                'background_color': '#f8fafc',
                'text_color': '#1e293b',
                'font_family': 'Inter, sans-serif',
                'font_size_base': '16px',
                'header_style': 'modern',
                'footer_style': 'multi-column',
                'banner_headline': 'Gentle Holistic Dentistry for Mindful Oral Wellness',
                'banner_subheadline': 'Metal-free ceramic implants, ozone therapeutics, and relaxation-first dentistry in a tranquil clinic environment.',
                'banner_cta_text': 'Book Your Gentle Visit',
                'banner_secondary_cta_text': 'Our Philosophy',
                'enable_whatsapp_float': True,
                'whatsapp_float_position': 'bottom-right',
                'whatsapp_prefilled_message': 'Hi Mint Leaf Dental! I would like to schedule a holistic oral health consultation.',
                'enable_call_now_button': True,
                'enable_sticky_appointment_bar': True,
                'seo_meta_title': 'Mint Leaf Holistic Dental Studio | Biocompatible Dental Care',
                'seo_meta_description': 'Experience gentle, biological, and anxiety-free dentistry. Metal-free ceramic implants, ozone therapy, and family wellness care.',
                'seo_keywords': 'holistic dentist, biological dentistry, ceramic implants, gentle dentist, eco dental clinic',
                'seo_robots_txt': 'User-agent: *\nAllow: /\nSitemap: https://www.mintleafdental.com/sitemap.xml',
                'seo_xml_sitemap_enabled': True,
                'hosting_type': 'dynamic_managed',
                'ssl_status': 'active',
                'published_at': None,
                'last_tested_at': timezone.now(),
                'last_test_score': 94,
            }
        )
        self.stdout.write(f"  - Clinic: {mint_clinic.name} ({'Created' if created else 'Updated'})")

        # Seed standard pages for Mint Leaf as well
        for pdata in standard_pages:
            WebsitePage.objects.update_or_create(
                clinic=mint_clinic,
                page_type=pdata['page_type'],
                defaults=pdata
            )

        # Seed doctors for Mint Leaf
        mint_doctors = [
            {
                'name': 'Dr. Julian Thorne, DDS, IABDM',
                'qualification': 'BDS, Certified Biological Dentist',
                'specialization': 'Biological Dentist & Ceramic Implantologist',
                'experience_years': 14,
                'bio': 'Certified member of the International Academy of Biological Dentistry & Medicine. Specializes in metal-free zirconia implants and holistic oral therapies.',
                'available_days': 'Mon, Tue, Thu & Fri',
                'consultation_fee': '$75',
                'appointment_enabled': True,
                'order': 1,
            },
            {
                'name': 'Dr. Maya Lin, DMD',
                'qualification': 'BDS - Preventive & Holistic Pediatric Dentistry',
                'specialization': 'Pediatric Wellness & Airway Development',
                'experience_years': 8,
                'bio': 'Passionate about gentle childhood dentistry, myofunctional airway health, and cavity-prevention therapies with natural mineralizing protocols.',
                'available_days': 'Mon, Wed & Fri',
                'consultation_fee': '$50',
                'appointment_enabled': True,
                'order': 2,
            },
        ]
        for md in mint_doctors:
            Doctor.objects.update_or_create(
                clinic=mint_clinic,
                name=md['name'],
                defaults=md
            )

        # Seed treatments for Mint Leaf
        for tdata in treatments_data[:5]:
            Treatment.objects.update_or_create(
                clinic=mint_clinic,
                slug=tdata['slug'],
                defaults=tdata
            )

        # 9. Seed Initial Quality Test Report for Apex Dental
        sample_checks = [
            {'category': 'Page Availability', 'name': 'Homepage (/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, loaded all core modules'},
            {'category': 'Page Availability', 'name': 'About Us (/about/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, mission & facilities populated'},
            {'category': 'Page Availability', 'name': 'Treatments (/treatments/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, 8 treatments active'},
            {'category': 'Page Availability', 'name': 'Our Doctors (/doctors/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, 4 specialist surgeons listed'},
            {'category': 'Page Availability', 'name': 'Gallery (/gallery/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, interior and before/after items active'},
            {'category': 'Page Availability', 'name': 'Contact Us (/contact/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, maps & working hours verified'},
            {'category': 'Page Availability', 'name': 'Appointment Booking (/book-appointment/)', 'status': 'PASS', 'detail': 'HTTP 200 OK, validation working'},
            {'category': 'Functionality', 'name': 'WhatsApp Chat Integration', 'status': 'PASS', 'detail': f'Valid wa.me link configured with number {apex_clinic.whatsapp_number}'},
            {'category': 'Functionality', 'name': 'Call Now Buttons', 'status': 'PASS', 'detail': f'Valid tel: protocol with phone {apex_clinic.phone}'},
            {'category': 'Functionality', 'name': 'Appointment Form Submission', 'status': 'PASS', 'detail': 'CSRF protection and DB record creation verified'},
            {'category': 'Responsiveness', 'name': 'Mobile Viewport Tag', 'status': 'PASS', 'detail': 'Meta viewport present with width=device-width'},
            {'category': 'Responsiveness', 'name': 'Bootstrap 5 Responsive Grid', 'status': 'PASS', 'detail': 'All breakpoints (xs, sm, md, lg, xl) tested'},
            {'category': 'Media & Assets', 'name': 'Image Loading & Alt Attributes', 'status': 'PASS', 'detail': '100% of images have descriptive alt text'},
            {'category': 'SEO Audit', 'name': 'Meta Title & Description', 'status': 'PASS', 'detail': 'Title length (58 chars), Description length (148 chars) optimal'},
            {'category': 'SEO Audit', 'name': 'Sitemap & Robots.txt', 'status': 'PASS', 'detail': 'Dynamic XML sitemap and robots.txt routes configured'},
            {'category': 'Performance', 'name': 'Page Load Speed', 'status': 'PASS', 'detail': 'Optimized asset bundle, estimated load time 0.8s'},
        ]

        WebsiteTestReport.objects.create(
            clinic=apex_clinic,
            overall_score=98,
            passed_checks=16,
            failed_checks=0,
            warning_checks=0,
            results_json=sample_checks,
            summary_text="All 16 quality verification checks passed. The website is fully optimized for mobile responsiveness, appointment conversion, SEO indexing, and production deployment."
        )

        DeploymentLog.objects.create(
            clinic=apex_clinic,
            target_domain='www.apexdentalcare.com',
            status='Success',
            notes="Initial production build verified. Dynamic hosting and SSL enabled."
        )

        self.stdout.write(self.style.SUCCESS("Successfully seeded Dental Clinic Website Builder!"))

