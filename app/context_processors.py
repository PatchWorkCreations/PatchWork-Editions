from .models import Service

def global_services(request):
    services = Service.objects.all()
    return {'services': services}
