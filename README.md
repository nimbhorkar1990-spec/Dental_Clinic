# Dental Clinic Website Builder & Management System (Python & Django)

A modern, professional, responsive, and user-friendly **Dental Clinic Website Builder and Management Platform** built using Python, Django, MySQL architecture, and Bootstrap 5.

The platform allows an administrator or developer to rapidly create, customize, manage, quality-test, and publish multiple dental clinic websites using standardized dental themes and clinical modules without rebuilding websites from scratch.

---

## 🌟 Key Features

### 1. Main Admin Dashboard
- **Comprehensive KPI Overview:** Total websites, live published clinics, pending patient enquiries, registered doctors, treatments, and active themes.
- **Active Clinic Workspace Switcher:** Seamlessly switch context between different clinics from any dashboard view.
- **Real-Time Appointment Enquiry Hub:** View incoming consultation bookings, update patient statuses, view internal clinical notes, and reply instantly with one click via WhatsApp or Phone.

### 2. Create New Dental Clinic Website
- Input fields:
  - Clinic Name & Unique URL Slug
  - Clinic Tagline & Mission / Vision
  - Clinic Address, Contact Number, WhatsApp Number, and Email
  - Assigned Domain Name
  - Working Hours & Emergency Dental Hotline
  - Google Maps Embed Location
  - Social Media Channels (Facebook, Instagram, Twitter/X, YouTube, LinkedIn)
  - Theme Selection from the Dental Template Library
- **Automated Provisioning:** Automatically initializes the **7 standard dental website pages**, seeds the **8 standard dental treatments**, initial doctor profiles, and default gallery assets upon creation.

### 3. Theme & Template Library
- **Pre-Built Company Dental Themes:**
  1. **Aura Dental (Modern Light Blue & Cyan):** Crisp, high-tech aesthetic, rounded clinical cards, floating appointment card.
  2. **Zenith Smile (White & Soft Mint Green):** Relaxing, holistic & biological dental wellness theme.
  3. **Royal Care Dental (Navy Blue & Gold):** Executive dental surgical specialist theme.
- **Template Capabilities:**
  - Browse available dental themes with color palette swatches.
  - Interactive live preview modal.
  - Apply any theme to existing or new clinic projects.
  - Duplicate existing templates into custom variants.
  - Upload custom HTML/CSS template packages (.zip).

### 4. Website Customization (Live Preview)
- Modify primary brand colors, secondary dark tones, accent colors, and background colors.
- Quick dental color palette presets (Cyan & Navy, Mint & Soft Green, Royal Blue & Gold).
- Typography selector: Poppins, Inter, Montserrat, Roboto, Playfair Display.
- Header styles: Modern Sticky with Emergency Bar, Classic Medical, Minimalist.
- Footer layouts: Four-Column Comprehensive or Compact Clean.
- Upload clinic logos, favicons, and hero banner background graphics.
- Banner headline, subheadline, and primary/secondary button texts.
- Custom CSS code editor injected directly into the website `<head>`.
- **Live Interactive Dual-Pane Preview:** Test changes instantly in real time with responsive viewport buttons (Desktop, Tablet, Mobile).

### 5. The 7 Standard Website Pages
Every dental clinic website automatically comes with these 7 fully responsive, editable pages:
- **Page 1: Home (`/site/<slug>/`):** Main hero banner, clinic introduction, featured treatments grid, our doctors carousel, Why Choose Us, patient testimonials, working hours banner, and appointment booking form.
- **Page 2: About Us (`/site/<slug>/about/`):** Practice overview, founding year & history, clinical mission & vision, facilities & sterile European autoclave technology, and surgical operatory tour.
- **Page 3: Treatments (`/site/<slug>/treatments/`):** All dental treatments with price tags, durations, icons, and individual detail pages (`/site/<slug>/treatments/<treatment_slug>/`) featuring step-by-step procedures, benefits, and patient FAQs.
  1. Dental Implants
  2. Root Canal Treatment
  3. Teeth Whitening
  4. Braces and Clear Aligners
  5. Cosmetic Dentistry & Veneers
  6. Dental Crowns & Bridges
  7. Professional Teeth Cleaning & Scaling
  8. Pediatric Dentistry
- **Page 4: Our Doctors (`/site/<slug>/doctors/`):** Doctor profiles with photos, qualifications (BDS, MDS, FICOI), specializations, years of experience, biographies, consultation fees, available days, and direct appointment booking buttons.
- **Page 5: Gallery (`/site/<slug>/gallery/`):** Interactive filterable photo gallery (Clinic Interior, Modern Equipment, Before & After Transformations, Happy Patients).
- **Page 6: Contact Us (`/site/<slug>/contact/`):** Clinic address, direct phone, WhatsApp chat, opening hours, emergency hotline, interactive Google Maps embed, and working contact enquiry form.
- **Page 7: Appointment Booking (`/site/<slug>/book-appointment/`):** Dedicated appointment engine with date picker, preferred time slot, treatment selection, doctor selection, additional notes, and instant WhatsApp confirmation redirect!

### 6. WhatsApp & Instant Telephony Integration
- Floating WhatsApp click-to-chat button (`https://wa.me/<number>?text=...`) on every page with configurable position (bottom-right vs bottom-left).
- Customizable prefilled patient WhatsApp message.
- Direct "Call Now" buttons (`tel:<phone>`).
- Mobile sticky bottom conversion bar locking Call and Book Visit actions on mobile screens.
- Instant WhatsApp response link generated on every submitted appointment enquiry in the admin dashboard.

### 7. Technical SEO Management
- Global and per-page SEO Page Title, Meta Description, and Focus Keywords.
- Real-time Google Search Result SERP snippet preview with character counter.
- Dynamic XML Sitemap generated at `/site/<slug>/sitemap.xml`.
- Dynamic Robots.txt generated at `/site/<slug>/robots.txt`.
- Schema.org `Dentist` JSON-LD structured data auto-injected in `<head>`.
- Open Graph (OG) meta tags for social media sharing.
- Descriptive image ALT tags and semantic H1/H2/H3 headings.

### 8. Website Testing & Quality Audit
- Automated pre-publish test runner checking:
  1. All 7 standard pages HTTP availability.
  2. Navigation menu links integrity.
  3. Appointment booking form validation & CSRF protection.
  4. WhatsApp direct link and number validation.
  5. Call Now `tel:` protocol verification.
  6. Mobile viewport meta tag and responsive CSS rules.
  7. Image loading and ALT attributes.
  8. Internal link routes.
  9. Asset load speed and TTFB performance.
  10. SEO compliance (Title length, description presence).
- Generates a visual Quality Audit Report with overall score percentage and Pass/Warning/Fail indicators.

### 9. Website Publishing & Deployment
- Domain mapping with DNS records guide (A record & CNAME).
- SSL/HTTPS configuration status (Active TLS 1.3 / Let's Encrypt).
- One-Click Standalone Static Website ZIP Export: Generates a complete deployable `.zip` archive containing all 7 static HTML pages, CSS styles, JavaScript, sitemap.xml, robots.txt, and deployment instructions.
- Auto-generated Nginx / Apache virtual host server configuration.
- Status toggle: Draft, Testing, Published, Maintenance Mode.
- Deployment history audit logs.

---

## 🛠️ Technology Stack

- **Backend:** Python 3.13, Django 6.1
- **Database:** MySQL architecture with PyMySQL 1.2.3 and SQLite portable fallback
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5.3, FontAwesome 6, Google Fonts (Poppins, Inter, Montserrat)
- **Image Processing:** Pillow 13.0

---

## 🚀 Getting Started

### 1. Installation
Clone the repository and install the dependencies:
```bash
pip install django pillow pymysql sqlparse asgiref
```

### 2. Database Migration
Apply the database migrations:
```bash
python manage.py migrate
```

### 3. Seed Initial Dental Data
Populate the 3 company dental themes, sample clinic websites, 7 pages, 8 treatments, and doctors:
```bash
python manage.py seed_clinic_data
```

### 4. Run the Development Server
```bash
python manage.py runserver
```
- **Admin Dashboard:** Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Sample Live Dental Site:** Open [http://127.0.0.1:8000/site/apex-dental/](http://127.0.0.1:8000/site/apex-dental/)

### 5. Running Automated Tests
Run the comprehensive test suite:
```bash
python manage.py test
```

---

## 🗄️ MySQL Database Configuration

To connect the system to a production MySQL database:
```bash
export DB_ENGINE=mysql
export DB_NAME=dental_clinic_db
export DB_USER=root
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=3306
```
The application detects `DB_ENGINE=mysql` and automatically routes through PyMySQL with full utf8mb4 charset support.

