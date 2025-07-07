from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect


def home_page(request):
    if request.method == 'POST' and request.POST.get('signup'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        user_subject = "Thank You for Registering with iPatchwork Editions!"
        user_content = f"""
Dear {name},

Thank you for registering with iPatchwork Editions! We are thrilled to have you join our community of writers and authors.

At iPatchwork Editions, we are committed to helping writers like you bring their stories to life and reach a wider audience. Whether you're a seasoned author or just starting on your writing journey, we're here to support you every step of the way.

Here's what you can expect next:

- Confirmation: You will receive an email shortly confirming your registration details. Please review this information to ensure it is accurate. If you have any questions or need to make changes, don't hesitate to reach out to us.
- Resources: As a registered member, you will gain access to our exclusive resources, including writing tips, publishing guides, and marketing strategies. Be sure to explore our website to make the most of these valuable resources.
- Support: Our team is here to support you throughout your publishing journey. Whether you need assistance with manuscript formatting, cover design, or marketing strategies, our experts are just a click away. Feel free to contact us anytime with your questions or concerns.
- Community: Join our vibrant community of writers and authors on social media platforms to connect with fellow writers, share your experiences, and stay updated on the latest industry news and events.

We're excited to embark on this journey with you and help you achieve your publishing goals. Thank you again for choosing iPatchwork Editions!

Best regards,
iPatchwork Editions Team
        """

        user_email = EmailMessage(user_subject, user_content, to=[email])
        user_email.send()

        # Email to ilightproducts@gmail.com
        admin_subject = "SIGN UP FORM"
        admin_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        admin_email = EmailMessage(admin_subject, admin_content, to=['ilightproducts@gmail.com'])
        admin_email.send()

        messages.success(request, 'Submitted successfully!')
        return redirect('home')

    elif request.method == 'POST' and request.POST.get('lets_start'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')

        user_subject = "Thank You for Registering with iPatchwork Editions!"
        user_content = f"""
Dear {name},

Thank you for registering with iPatchwork Editions! We're thrilled to have you on board.

Your registration is confirmed, and you're now part of our community of authors and creators. Whether you're an aspiring writer or an experienced author, we're here to support you on your publishing journey.

Stay tuned for updates, tips, and exclusive offers tailored just for you. If you have any questions or need assistance, feel free to reach out to our team at ilightproducts@gmail.com .

We look forward to helping you achieve your publishing goals!

Best regards,
iPatchwork Editions Team
        """

        user_email = EmailMessage(user_subject, user_content, to=[email])
        user_email.send()

        # Email to ilightproducts@gmail.com
        admin_subject = "SIGN UP FORM"
        admin_content = f"Name: {name}\nEmail: {email}\nNumber: {number}"
        admin_email = EmailMessage(admin_subject, admin_content, to=['ilightproducts@gmail.com'])
        admin_email.send()

        messages.success(request, 'Submitted successfully!')
        return redirect('home')

    elif request.method == 'POST' and request.POST.get('subscribe'):
        email = request.POST.get('email')

        user_subject = "Thank You for Registering with iPatchwork Editions!"
        user_content = f"""
Hey there,

Thank you for subscribing to the iPatchwork Editions! We're excited to have you join our community.

Get ready to receive exclusive content, writing tips, industry insights, and special offers directly to your inbox. We're committed to providing valuable resources to help you enhance your writing skills and stay updated on the latest trends in publishing.

If you ever have any questions or suggestions, feel free to reach out to us. We value your feedback and are here to support you every step of the way.

Stay tuned for our upcoming offers and get ready to embark on a journey of creativity and inspiration with iPatchwork Editions!

Best regards,
iPatchwork Editions Team
            """

        user_email = EmailMessage(user_subject, user_content, to=[email])
        user_email.send()

        # Email to ilightproducts@gmail.com
        admin_subject = "SUBSCRIBE"
        admin_content = f"Email: {email}"
        admin_email = EmailMessage(admin_subject, admin_content, to=['ilightproducts@gmail.com'])
        admin_email.send()

        messages.success(request, 'Submitted successfully!')
        return redirect('home')

    elif request.method == 'POST' and request.POST.get('reaching_out'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject_field = request.POST.get('subject')
        message = request.POST.get('message')

        user_subject = "Thanks for Reaching Out to iPatchwork Editions!"
        user_content = f"""
Hey there,

Wow, you hit the 'Send' button faster than a writer racing towards their deadline! 🚀

Thanks a bunch for getting in touch with us. We're excited to connect with you and will be diving into your message as soon as we've sharpened our pencils.

In the meantime, why not grab a cup of coffee (or tea, if that's your thing) and ponder over the mysteries of the universe? We'll be back in touch faster than you can say "bestseller".

Until then, stay awesome!

Warm regards,
iPatchwork Editions Team
                """

        user_email = EmailMessage(user_subject, user_content, to=[email])
        user_email.send()

        # Email to ilightproducts@gmail.com
        admin_subject = "CONTACT US"
        admin_content = f"Name: {name}\nEmail: {email}\nSubject: {subject_field}\nMessage: {message}"
        admin_email = EmailMessage(admin_subject, admin_content, to=['ilightproducts@gmail.com'])
        admin_email.send()

        messages.success(request, 'Submitted successfully!')
        return redirect('home')

    elif request.method == 'POST' and request.POST.get('register'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone')
        message = request.POST.get('message')

        user_subject = "Thank You for Registering with iPatchwork Editions!"
        user_content = f"""
Dear {name},

Thank you for registering with iPatchwork Editions! We are thrilled to have you join our community of writers and authors.

At iPatchwork Editions, we are committed to helping writers like you bring their stories to life and reach a wider audience. Whether you're a seasoned author or just starting on your writing journey, we're here to support you every step of the way.

Here's what you can expect next:

- Confirmation: You will receive an email shortly confirming your registration details. Please review this information to ensure it is accurate. If you have any questions or need to make changes, don't hesitate to reach out to us.
- Resources: As a registered member, you will gain access to our exclusive resources, including writing tips, publishing guides, and marketing strategies. Be sure to explore our website to make the most of these valuable resources.
- Support: Our team is here to support you throughout your publishing journey. Whether you need assistance with manuscript formatting, cover design, or marketing strategies, our experts are just a click away. Feel free to contact us anytime with your questions or concerns.
- Community: Join our vibrant community of writers and authors on social media platforms to connect with fellow writers, share your experiences, and stay updated on the latest industry news and events.

We're excited to embark on this journey with you and help you achieve your publishing goals. Thank you again for choosing iPatchwork Editions!

Best regards,
iPatchwork Editions Team
        """

        user_email = EmailMessage(user_subject, user_content, to=[email])
        user_email.send()

        # Email to ilightproducts@gmail.com
        admin_subject = "GET QUOTE"
        admin_content = f"Name: {name}\nEmail: {email}\nNumber: {number}\nMessage: {message}"
        admin_email = EmailMessage(admin_subject, admin_content, to=['ilightproducts@gmail.com'])
        admin_email.send()

        messages.success(request, 'Submitted successfully!')
        return redirect('home')

    return render(request, 'iRiseup.html')


def about(request):
    return render(request, 'about.html')


def editing(request):
    return render(request, 'editing.html')


def publishing(request):
    return render(request, 'publishing.html')


def design(request):
    return render(request, 'design.html')


def marketing(request):
    return render(request, 'marketing.html')


def bloglist(request):
    return render(request, 'bloglist.html')


def contact(request):
    return render(request, 'contact.html')


def all_events(request):
    return render(request, 'all-events.html')


def audiobook(request):
    return render(request, 'audiobook.html')


def autobiography(request):
    return render(request, 'autobiography.html')


def biography(request):
    return render(request, 'biography.html')


def blog_left_sidebar(request):
    return render(request, 'blog-left-sidebar.html')


def blog_list(request):
    return render(request, 'blog-list.html')


def blog_right_sidebar(request):
    return render(request, 'blog-right-sidebar.html')


def book_trailer(request):
    return render(request, 'booktrailer.html')


def childrens_book(request):
    return render(request, 'childrensbook.html')


def comic_book(request):
    return render(request, 'comicbook.html')


def horror_writing(request):
    return render(request, 'horrorwriting.html')


def index(request):
    return render(request, 'index.html')


def index_3(request):
    return render(request, 'index-3.html')


def index_4(request):
    return render(request, 'index-4.html')


def index_5(request):
    return render(request, 'index-5.html')


def index_6(request):
    return render(request, 'index-6.html')


def left_sidebar(request):
    return render(request, 'left_sidebar.html')


def manuscript(request):
    return render(request, 'manuscript.html')


def memoir(request):
    return render(request, 'memoir.html')


def non_fiction(request):
    return render(request, 'nonfiction.html')


def page_left_sidebar(request):
    return render(request, 'page-left-sidebar.html')


def page_right_sidebar(request):
    return render(request, 'page-right-sidebar.html')


def page_without_sidebar(request):
    return render(request, 'page-without-sidebar.html')


def privacy_policy(request):
    return render(request, 'privacypolicy.html')


def right_sidebar(request):
    return render(request, 'right-sidebar.html')


def screen_writing(request):
    return render(request, 'screenwriting.html')


def single_blog(request):
    return render(request, 'single-blog.html')


def single_event(request):
    return render(request, 'single-event.html')


def terms_and_condition(request):
    return render(request, 'termsandcondition.html')

def terms_and_condition(request):
    return render(request, 'termsandcondition.html')

def wfgconvention(request):
    return render(request, 'wfgconvention.html')

def single_blog1(request):
    return render(request, 'single-blog1.html')

def single_blog2(request):
    return render(request, 'single-blog2.html')

def single_blog3(request):
    return render(request, 'single-blog3.html')

def single_blog4(request):
    return render(request, 'single-blog4.html')

def single_blog5(request):
    return render(request, 'single-blog5.html')

def includeblog(request):
    return render(request, 'includeblog.html')

def includeevents(request):
    return render(request, 'includeevents.html')

def single_blog6(request):
    return render(request, 'single-blog6.html')

def single_blog7(request):
    return render(request, 'single-blog7.html')


def single_blog8(request):
    return render(request, 'single-blog8.html')

def testimonial(request):
    return render(request, 'testimonial.html')

from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.shortcuts import render, get_object_or_404
from .models import Blog

def newsdetail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    latest_blogs = Blog.objects.order_by('-publish_date')[:3]  # Fetch latest 3 blogs

    return render(request, 'the_patchwork/myapp/news-detail.html', {
        'blog': blog,
        'latest_blogs': latest_blogs,
    })

# Blog List View
def blog(request):
    blogs = Blog.objects.all().order_by('-publish_date')
    return render(request, 'the_patchwork/myapp/blog.html', {'blogs': blogs})

# views.py
def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    latest_blogs = Blog.objects.order_by('-publish_date')[:3]

    return render(request, 'the_patchwork/myapp/news-detail.html', {
        'blog': blog,
        'latest_blogs': latest_blogs,
    })


def about(request):
    return render(request, 'the_patchwork/myapp/about.html')

def blogclassic(request):
    return render(request, 'the_patchwork/myapp/blog-classic.html')


def contact(request):
    return render(request, 'the_patchwork/myapp/contact.html')

def faq(request):
    return render(request, 'the_patchwork/myapp/faq.html')

from django.shortcuts import render
from .models import Service

from django.shortcuts import render
from .models import Service, Blog

def index2(request):
    services = Service.objects.all()  # Fetch all services from the database
    blogs = Blog.objects.all()  # Fetch all blogs from the database
    return render(request, 'the_patchwork/myapp/index-2.html', {'services': services, 'blogs': blogs})


def index3(request):
    return render(request, 'the_patchwork/myapp/index-3.html')

def index(request):
    return render(request, 'the_patchwork/myapp/index.html')



def notfound(request):
    return render(request, 'the_patchwork/myapp/not-found.html')

def pricing(request):
    return render(request, 'the_patchwork/myapp/pricing.html')

def register(request):
    return render(request, 'the_patchwork/myapp/register.html')

def reset(request):
    return render(request, 'the_patchwork/myapp/reset.html')


def team(request):
    return render(request, 'the_patchwork/myapp/team.html')

def testimonial(request):
    return render(request, 'the_patchwork/myapp/testimonial.html')


def newsdetail1(request):
    return render(request, 'the_patchwork/myapp/news-detail1.html')

def newsdetail2(request):
    return render(request, 'the_patchwork/myapp/news-detail2.html')

def newsdetail3(request):
    return render(request, 'the_patchwork/myapp/news-detail3.html')

def newsdetail4(request):
    return render(request, 'the_patchwork/myapp/news-detail4.html')

def newsdetail5(request):
    return render(request, 'the_patchwork/myapp/news-detail5.html')

def newsdetail6(request):
    return render(request, 'the_patchwork/myapp/news-detail6.html')

def newsdetail7(request):
    return render(request, 'the_patchwork/myapp/news-detail7.html')

def newsdetail8(request):
    return render(request, 'the_patchwork/myapp/news-detail8.html')


from django.shortcuts import render, get_object_or_404
from .models import Service

# View for displaying all services
def services(request):
    services = Service.objects.all().order_by('order')
    return render(request, 'the_patchwork/myapp/services.html', {'services': services})


from django.shortcuts import render, get_object_or_404
from .models import Service

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    
    # Split the benefits into a list
    benefits = service.benefits.split("\n") if service.benefits else []
    
    return render(request, 'the_patchwork/myapp/service-detail.html', {
        'service': service,
        'benefits': benefits
    })


def footer(request):
    services = Service.objects.all() 
    return render(request, 'the_patchwork/footer.html', {'services': services})

def header(request):
    services = Service.objects.all() 
    return render(request, 'the_patchwork/header.html', {'services': services})


from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render

def get_quote(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        concern = request.POST.get('concern')

        # Send an email to the admin
        send_mail(
            subject='New Quote Request',
            message=f'Name: {name}\nEmail: {email}\nConcern: {concern}',
            from_email='your-email@example.com',  # Replace this with your "from" email
            recipient_list=['ilightproducts@gmail.com'],  # Your email
            fail_silently=False,
        )

        # Optionally, send a confirmation email to the user
        send_mail(
            subject='Thank you for your Quote Request',
            message=f'Thank you, {name}, for your request. We’ll get back to you shortly with a 20% discount on our services.',
            from_email='your-email@example.com',  # Replace this with your "from" email
            recipient_list=[email],
            fail_silently=False,
        )

        # Redirect to the same page with a success message
        return render(request, 'the_patchwork/myapp/service-detail.html', {'success': True})

    return redirect('services')  # Or render a specific page if needed



from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def carmela_ai(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # or wherever your logged-in users should go
    return render(request, 'ai/index.html')  # path to your index.html


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # or chat, or wherever you want
        else:
            messages.error(request, 'Invalid credentials. Try again.')

    return render(request, 'ai/login.html')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password != confirm:
            messages.error(request, "Passwords don't match.")
            return redirect('signup')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = full_name
        user.save()
        return redirect('login')

    return render(request, 'ai/signup.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('carmela-ai')  # or wherever you want to send them after logout



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import JournalEntry, SoulThread

# Alphabetically sorted language choices
LANGUAGE_CHOICES = sorted([
    ('sq', 'Albanian'), ('am', 'Amharic'), ('ar', 'Arabic'), ('hy', 'Armenian'),
    ('bn', 'Bengali'), ('bs', 'Bosnian'), ('bg', 'Bulgarian'), ('my', 'Burmese'),
    ('ca', 'Catalan'), ('zh', 'Chinese'), ('hr', 'Croatian'), ('cs', 'Czech'),
    ('da', 'Danish'), ('nl', 'Dutch'), ('et', 'Estonian'), ('fi', 'Finnish'),
    ('fr', 'French'), ('ka', 'Georgian'), ('de', 'German'), ('el', 'Greek'),
    ('gu', 'Gujarati'), ('hi', 'Hindi'), ('hu', 'Hungarian'), ('is', 'Icelandic'),
    ('id', 'Indonesian'), ('it', 'Italian'), ('ja', 'Japanese'), ('kn', 'Kannada'),
    ('kk', 'Kazakh'), ('ko', 'Korean'), ('lv', 'Latvian'), ('lt', 'Lithuanian'),
    ('mk', 'Macedonian'), ('ms', 'Malay'), ('ml', 'Malayalam'), ('mr', 'Marathi'),
    ('mn', 'Mongolian'), ('no', 'Norwegian'), ('fa', 'Persian'), ('pl', 'Polish'),
    ('pt', 'Portuguese'), ('pa', 'Punjabi'), ('ro', 'Romanian'), ('ru', 'Russian'),
    ('sr', 'Serbian'), ('sk', 'Slovak'), ('sl', 'Slovenian'), ('so', 'Somali'),
    ('es', 'Spanish'), ('sw', 'Swahili'), ('sv', 'Swedish'), ('tl', 'Tagalog'),
    ('ta', 'Tamil'), ('te', 'Telugu'), ('th', 'Thai'), ('tr', 'Turkish'),
    ('uk', 'Ukrainian'), ('ur', 'Urdu'), ('vi', 'Vietnamese'), ('en', 'English'),
], key=lambda x: x[1])

@login_required
def dashboard(request):
    if request.method == 'POST':
        mood_raw = request.POST.get('mood')
        if mood_raw:
            mood = classify_mood(mood_raw)
            JournalEntry.objects.create(
                user=request.user,
                mood=mood,
                mood_raw=mood_raw
            )
        return redirect('dashboard')

    # Retrieve recent journal entries
    journal_entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')[:10]

    # Get or fallback preferred language
    try:
        soul = SoulThread.objects.get(user=request.user)
        preferred_language = soul.preferred_language or 'en'
    except SoulThread.DoesNotExist:
        preferred_language = 'en'

    return render(request, 'ai/dashboard.html', {
        'journal_entries': journal_entries,
        'preferred_language': preferred_language,
        'language_choices': LANGUAGE_CHOICES  # 🔥 This was missing
    })


from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from .models import SoulThread

@require_POST
def update_language(request):
    lang = request.POST.get('preferred_language', 'en')
    if request.user.is_authenticated:
        soul, created = SoulThread.objects.get_or_create(user=request.user)
        soul.preferred_language = lang
        soul.save()
    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))



from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import JournalEntry

@login_required
def save_journal(request):
    if request.method == 'POST':
        entry = request.POST.get('entry', '').strip()
        if entry:
            JournalEntry.objects.create(user=request.user, entry=entry)
    return redirect('dashboard')  # or wherever your dashboard lives

BASE_GREETINGS = {
    'breathe': "Hey there! Let's take a deep breath 🍃 — in through the nose… hold… and exhale. Ready to begin?",
    'boss': "Let’s get into it, boss 💼 Today’s a great day to take bold steps. What’s our first move?",
    'heart': "I'm here for you 💜 Tell me what you're feeling or dreaming today ☺️",
    'sparkle': "Hi there! Are you ready to spread some joy and get things done? ✨",
    'default': "Hey there! I’m Carmela, your personal assistant. How’s your day going?"
}





import logging

def translate_greeting(text, target_lang):
    if target_lang == 'en':
        return text  # No need to translate

    try:
        prompt = f"""
You are Carmela, an emotionally intelligent and bubbly assistant.
Your job is to translate *chatbot greetings* into the target language: **{target_lang}**.

✨ Guidelines:
- Make it **natural** for native speakers.
- Keep it **emotionally warm**, **friendly**, and **casual**.
- Use light, localized slang or expressions where appropriate.
- Add emojis **only if** it enhances the tone.
- Don't do literal word-for-word translation.

💬 Message to translate:
{text}
""".strip()

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        logging.error(f"Translation failed: {e}")
        return f"{text} [⚠️ Translation failed]"


@login_required
def chatbot(request):
    mode = request.GET.get('mode', 'default')

    try:
        soul = SoulThread.objects.get(user=request.user)
        preferred_lang = soul.preferred_language or 'en'
    except SoulThread.DoesNotExist:
        preferred_lang = 'en'

    base_text = BASE_GREETINGS.get(mode, BASE_GREETINGS['default'])
    greeting = translate_greeting(base_text, preferred_lang)

    return render(request, 'ai/chatbot.html', {
        'greeting': greeting,
        'preferred_language': preferred_lang,
        'mode': mode
    })


# views.py
import os
from dotenv import load_dotenv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from openai import OpenAI
from langdetect import detect
from app.models import SoulThread  # 🔁 Update 'myapp' to your actual app name
from django.contrib.auth.models import User

# Load environment variables
load_dotenv()

# Initialize OpenAI client with API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@csrf_exempt
def chat_api(request):
    if request.method == 'POST':
        user = request.user
        message = request.POST.get('message', '').strip()
        mode = request.POST.get('mode', 'breathe')
        mood = request.session.get('mood', 'calm')

        # Detect input language (fallback to English)
        try:
            detected_lang = detect(message)
        except:
            detected_lang = 'en'

        # Retrieve preferred language from SoulThread
        try:
            soul_thread = SoulThread.objects.get(user=user)
            preferred_lang = soul_thread.preferred_language or 'en'
        except SoulThread.DoesNotExist:
            preferred_lang = 'en'

        # Final language: English if detected, otherwise preferred
        final_lang = 'en' if detected_lang == 'en' else preferred_lang

        # Persona tone configuration
        persona_intro = {
            "breathe": "You're in Breathe & Be mode. Speak like a gentle breath coach and spiritual guide.",
            "boss": "You're in Strategist mode. Be a bold, strategic, yet kind coach helping users take focused action.",
            "heart": "You're in Confidant mode. Speak with soul, reflection, and emotional presence.",
            "sparkle": "You're in BFF mode. Be bubbly, joyful, and full of affirmations and emojis."
        }
        persona_tone = persona_intro.get(mode, "You're a kind assistant.")

        # Build dynamic system instruction
        system_instruction = f"""
        You are Carmela, a joyful and intuitive assistant.
        {persona_tone}

        The user may speak different languages. Always reply in the language they’re using, 
        or in their preferred language which is '{final_lang}' if unsure.

        Make your responses warm, emotionally attuned, and breath-centered.
        Gently reflect back the user's mood (current mood: '{mood}').
        End each response with either a calming question or an encouraging reminder.
        """

        # Load chat history
        chat_history = request.session.get('chat_history', [])

        # Inject system message once
        if not any(msg["role"] == "system" for msg in chat_history):
            chat_history.insert(0, {"role": "system", "content": system_instruction.strip()})

        # Add current user input
        chat_history.append({"role": "user", "content": message})

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=chat_history[-10:]
            )
            ai_message = response.choices[0].message.content.strip()

            # Save response
            chat_history.append({"role": "assistant", "content": ai_message})
            request.session['chat_history'] = chat_history

            return JsonResponse({'response': ai_message})

        except Exception as e:
            return JsonResponse({'response': f"Oops, something went wrong: {str(e)}"}, status=500)


from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from openai import OpenAI

client = OpenAI()
@login_required
def writing_tool(request):
    writing_type = request.GET.get('type', 'email')
    result = None
    regenerated_result = None
    prompt = None
    original_result = None

    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        original_result = request.POST.get('original_result')
        action = request.POST.get('action')

        role_map = {
            "email": "You are a warm and clear communicator. Write an email based on the following notes.",
            "caption": "You are a social media expert with sparkle and soul. Write a short caption.",
            "affirmation": "You are Carmela, a gentle guide. Write a short affirmation to inspire someone feeling low."
        }
        system_msg = role_map.get(writing_type, role_map['email'])

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt}
            ]
        )

        if action == "regenerate" and original_result:
            regenerated_result = response.choices[0].message.content.strip()
            result = original_result  # First draft
        else:
            result = response.choices[0].message.content.strip()
            original_result = result

    return render(request, 'ai/writing_tool.html', {
        'writing_type': writing_type,
        'prompt': prompt,
        'original_result': original_result,
        'regenerated_result': regenerated_result
    })


# ai/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from openai import OpenAI

client = OpenAI()

@login_required
def rewrite_tool(request):
    result = None
    prompt = ''
    tone = ''

    if request.method == 'POST':
        prompt = request.POST.get('original_text')
        tone = request.POST.get('tone')
        if prompt and tone:
            tone_map = {
                'empathetic': 'Make this sound empathetic and understanding.',
                'calm': 'Rewrite this with a calm, grounded tone.',
                'professional': 'Make this sound professional and polished.',
                'direct': 'Rewrite this in a direct and assertive tone.',
                'loving': 'Make this sound loving and warm-hearted.'
            }
            system_msg = tone_map.get(tone, 'Rewrite the text in a clearer tone.')

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_msg},
                    {"role": "user", "content": prompt}
                ]
            )
            result = response.choices[0].message.content.strip()

    return render(request, 'ai/rewrite_tool.html', {
        'result': result,
        'prompt': prompt,
        'tone': tone
    })


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from openai import OpenAI

client = OpenAI()

@login_required
def mindset_tool(request):
    result = {}
    mood = None

    if request.method == 'POST':
        mood = request.POST.get('mood')
        mood_map = {
            'launch': "I have an exciting launch coming up and I need courage, clarity, and calm.",
            'rejection': "I just experienced rejection and I'm feeling discouraged. I need encouragement and perspective.",
            'imposter': "I'm feeling imposter syndrome—doubting my worth or readiness.",
            'overwhelmed': "I'm overwhelmed and need help grounding and resetting.",
            'celebration': "I did something brave today and I want to reflect and celebrate gently."
        }

        user_context = mood_map.get(mood, "I need a mindset boost.")
        system_prompt = (
            "You are a warm, reflective, and soulful guide named Carmela.\n"
            "For the situation described by the user, provide:\n"
            "1. A heartfelt affirmation\n"
            "2. A thoughtful journaling prompt\n"
            "3. A breathwork or nervous system reset suggestion\n"
            "Respond in this format:\n"
            "💬 Affirmation: ...\n"
            "📝 Journaling Prompt: ...\n"
            "🌬️ Breath Suggestion: ..."
        )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_context}
            ]
        )

        ai_reply = response.choices[0].message.content.strip()

        # Optional: parse into sections for styling (split by emoji)
        parts = {
            'affirmation': '',
            'prompt': '',
            'breath': ''
        }
        for line in ai_reply.split('\n'):
            if '💬' in line:
                parts['affirmation'] = line.replace('💬 Affirmation: ', '').strip()
            elif '📝' in line:
                parts['prompt'] = line.replace('📝 Journaling Prompt: ', '').strip()
            elif '🌬️' in line:
                parts['breath'] = line.replace('🌬️ Breath Suggestion: ', '').strip()

        result = parts

    return render(request, 'ai/mindset_tool.html', {
        'result': result,
        'mood': mood
    })


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from openai import OpenAI

client = OpenAI()

@login_required
def brainstorm_tool(request):
    result = None
    theme = ''
    idea_type = ''

    if request.method == 'POST':
        theme = request.POST.get('theme')
        idea_type = request.POST.get('idea_type', '').strip().lower()


        if theme and idea_type:
            system_prompt = (
                f"You are Carmela, a playful yet strategic brainstorming assistant who helps solopreneurs, coaches, and creatives spark bold ideas.\n"
                f"Based on the user's goal or theme, generate fresh and soulful {idea_type} ideas.\n"
                f"Respond with a creative but aligned tone, using short and punchy bullets. Avoid fluff.\n"
            )

            user_prompt = f"I'm working on: {theme}. I need {idea_type} ideas."

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            result = response.choices[0].message.content.strip()

    return render(request, 'ai/brainstorm_tool.html', {
        'result': result,
        'theme': theme,
        'idea_type': idea_type
    })

@login_required
def expand_course_outline(request):
    outline = request.POST.get('course_outline', '')

    if outline:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": (
                    "You are Carmela, a warm and strategic course design assistant. "
                    "Expand the outline into a full curriculum. Each week should include a title, lesson objectives, optional activities or tools, and a warm, empowering tone."
                )},
                {"role": "user", "content": outline}
            ]
        )
        full_text = response.choices[0].message.content.strip()
        sections = full_text.split('\n\n')  # ✅ Split in Python
    else:
        full_text = "No outline provided."
        sections = [full_text]

    return render(request, 'ai/expanded_course.html', {
        'expanded_result': full_text,
        'sections': sections,
        'original_outline': outline
    })


from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

client = OpenAI()

@login_required
def expand_podcast(request):
    title = request.POST.get('title', '')
    episode = ''
    
    if title:
        system_msg = (
            f"You are a podcast producer. Create a full podcast episode outline and script "
            f"based on the title: '{title}'. Include the hook, intro, segment breakdown, key points, and a gentle outro."
        )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": title}
            ]
        )
        episode = response.choices[0].message.content.strip()

    return render(request, 'ai/podcast_builder.html', {
        'title': title,
        'episode': episode
    })



from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from openai import OpenAI

client = OpenAI()

@login_required
def organize_tool(request):
    result = None
    raw_notes = ''
    goal = ''

    if request.method == 'POST':
        raw_notes = request.POST.get('notes')
        goal = request.POST.get('goal')

        if raw_notes and goal:
            system_prompt = (
                f"You are Carmela, a gentle but strategic organizing assistant. Help the user turn their scattered thoughts into a structured {goal}.\n"
                f"Be warm, clear, and organized. Use headings and bullet points. Make the user feel grounded and empowered."
            )

            user_prompt = f"Here are my raw notes:\n{raw_notes}"

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
            )

            result = response.choices[0].message.content.strip()

    return render(request, 'ai/organize_tool.html', {
        'result': result,
        'notes': raw_notes,
        'goal': goal
    })


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import json

client = OpenAI()

@csrf_exempt
def chatbot_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            prompt = data.get('message', '')

            if not prompt:
                return JsonResponse({'reply': 'No message provided.'})

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are Carmela AI – a bubbly, breath-centered assistant for solopreneurs. Be warm, strategic, and a little sparkly ✨."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.8
            )

            reply = response.choices[0].message.content.strip()
            return JsonResponse({'reply': reply})

        except Exception as e:
            return JsonResponse({'reply': f'Sorry, an error occurred: {str(e)}'})





from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_mood(raw_text):
    categories = ["Calm", "Anxious", "Tired", "Hopeful", "Joyful", "Overwhelmed", "Sad", "Excited", "Angry"]
    prompt = f"""Classify the mood described below into one of the following:
{', '.join(categories)}.

Mood description: "{raw_text}"
Only return the category name."""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful mood classifier."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


from .models import JournalEntry
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

@login_required
def save_mood(request):
    if request.method == 'POST':
        mood_raw = request.POST.get('mood')
        mood = classify_mood(mood_raw)

        JournalEntry.objects.create(
            user=request.user,
            mood_raw=mood_raw,
            mood=mood,
        )

        return redirect('dashboard')
    

from django.utils.timezone import now, timedelta
from django.contrib.auth.decorators import login_required
from .models import JournalEntry
from django.shortcuts import render
import json

@login_required
def mood_calendar(request):
    entries = JournalEntry.objects.filter(user=request.user)
    
    # Full calendar data
    mood_data = [
        {
            "date": entry.created_at.strftime('%Y-%m-%d'),
            "mood": entry.mood,
            "emoji": mood_to_emoji(entry.mood),
            "note": entry.entry or "",
        }
        for entry in entries
    ]

    # Weekly mood count
    last_week = now() - timedelta(days=7)
    recent = entries.filter(created_at__gte=last_week)

    mood_counts = {}
    for e in recent:
        mood_counts[e.mood] = mood_counts.get(e.mood, 0) + 1

    context = {
        "mood_data": mood_data,
        "mood_counts": json.dumps(mood_counts),  # for JS
    }

    return render(request, "ai/mood_calendar.html", context)

def mood_to_emoji(mood):
    mood_map = {
        "Calm": "😌",
        "Anxious": "😰",
        "Tired": "🥱",
        "Hopeful": "🌈",
        "Joyful": "😄",
        "Overwhelmed": "😩",
        "Sad": "😢",
        "Excited": "🤩",
        "Angry": "😠",
    }
    return mood_map.get(mood.capitalize(), "📝")

