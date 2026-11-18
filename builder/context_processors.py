from .models import ClinicWebsite

def clinic_builder_context(request):
    """
    Supplies clinics list and active clinic context to all builder dashboard views.
    """
    clinics = ClinicWebsite.objects.all().order_by('name')
    active_clinic_id = request.session.get('active_clinic_id')
    current_clinic = None
    
    if active_clinic_id:
        current_clinic = ClinicWebsite.objects.filter(id=active_clinic_id).first()
        
    if not current_clinic and clinics.exists():
        current_clinic = clinics.first()
        request.session['active_clinic_id'] = current_clinic.id

    return {
        'dashboard_clinics': clinics,
        'active_clinic': current_clinic,
    }

