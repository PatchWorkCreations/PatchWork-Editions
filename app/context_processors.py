from .models import SoulThread
from .views import LANGUAGE_CHOICES

def language_context(request):
    preferred_language = 'en'
    if request.user.is_authenticated:
        try:
            soul = SoulThread.objects.get(user=request.user)
            preferred_language = soul.preferred_language or 'en'
        except SoulThread.DoesNotExist:
            pass

    return {
        'preferred_language': preferred_language,
        'language_choices': LANGUAGE_CHOICES
    }
