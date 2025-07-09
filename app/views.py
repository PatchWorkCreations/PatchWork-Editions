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
    'breathe': {
       'sq': "Hej, përshëndetje! Le të marrim një frymë të thellë 🍃 — nga hunda… mbaje… dhe nxirre ngadalë. Gati për të filluar?",
'am': "ሰላም! እንደገና ዕረፍት እንንበል 🍃 — በአፍንጫ ስትወስድ… አቁም… እና ቀስ በቀስ አስተንፈስ። ለመጀመር ዝግጅት አለ?",
'ar': "مرحباً! لنأخذ نفساً عميقاً 🍃 — من الأنف... احتفظ به... وزفر ببطء. جاهز نبدأ؟",
'hy': "Ողջույն։ Եկե՛ք խոր շունչ քաշենք 🍃 — քթով ներշնչել… պահել… և արտաշնչել։ Պատրա՞ստ ես սկսելու։",
'bn': "হেই! চলো একটা গভীর শ্বাস নেই 🍃 — নাক দিয়ে নিই… ধরে রাখি… আর ধীরে ধীরে ছেড়ে দিই। শুরু করার জন্য প্রস্তুত?",
'bs': "Hej! Udahnimo duboko 🍃 — na nos… zadrži… i izdahni. Spreman/na za početak?",
'bg': "Здрасти! Хайде да поемем дълбоко въздух 🍃 — през носа… задръж… и издишай. Готов/а ли си да започнем?",
'my': "မင်္ဂလာပါ။ လေရှည်ရှည်ရှူကြပါစို့ 🍃 — နှာခေါင်းကနေပင်… တချို့ထိန်းထားပြီး… ပြန်ထုတ်ပါ။ စရအောင်နော်?",
'ca': "Hola! Fem una respiració profunda 🍃 — pel nas… mantén… i exhala. Llest/a per començar?",
'zh': "嘿，你好！我们一起深呼吸一下 🍃 —— 用鼻子吸气…停留…然后呼气。准备好开始了吗？",
'hr': "Hej! Udahnimo duboko 🍃 — kroz nos… zadrži… i izdahni. Spreman/na za početak?",
'cs': "Ahoj! Pojďme se zhluboka nadechnout 🍃 — nosem… zadržet… a vydechnout. Připraven/a začít?",
'da': "Hej der! Lad os tage en dyb indånding 🍃 — ind gennem næsen… hold… og pust ud. Klar til at gå i gang?",
'nl': "Hoi daar! Laten we diep ademhalen 🍃 — in door je neus… vasthouden… en uitademen. Klaar om te beginnen?",
'et': "Hei! Teeme ühe sügava hingetõmbe 🍃 — läbi nina… hoia kinni… ja välja. Valmis alustama?",
'fi': "Hei siellä! Otetaanpa syvä hengitys 🍃 — nenän kautta sisään… pidä… ja ulos. Valmis aloittamaan?",
'fr': "Coucou ! On prend une grande inspiration 🍃 — par le nez… on bloque… et on expire. Prêt(e) à commencer ?",
'ka': "გამარჯობა! მოდი ღრმად ამოვისუნთქოთ 🍃 — ცხვირით ჩასუნთქე… შეაჩერე… და ამოისუნთქე. მზად ხარ დასაწყებად?",
'de': "Hey du! Lass uns tief durchatmen 🍃 — durch die Nase… halten… und ausatmen. Bereit loszulegen?",
'el': "Γεια σου! Πάμε να πάρουμε μια βαθιά ανάσα 🍃 — από τη μύτη… κράτα… και εκπνοή. Έτοιμος/η να ξεκινήσουμε;",
'gu': "હાય! ચાલો ઊંડી શ્વાસ લઈએ 🍃 — નાકથી લો… રોકો… અને શાંત રીતે છોડો. શરૂ કરવા તૈયાર છો?",
'hi': "हाय! चलो एक गहरी सांस लेते हैं 🍃 — नाक से अंदर… रोकें… और धीरे-धीरे बाहर छोड़ें। शुरू करें?",
'hu': "Szia! Vegyünk egy mély levegőt 🍃 — orron be… tartsd… és fújd ki. Készen állsz kezdeni?",
'is': "Hæ! Tökum djúpan andardrátt 🍃 — inn um nefið… haltu… og andaðu út. Tilbúin(n) að byrja?",
'id': "Hai! Yuk tarik napas dalam 🍃 — lewat hidung… tahan sebentar… dan hembuskan. Siap mulai?",
'it': "Ehi! Facciamo un bel respiro profondo 🍃 — dal naso… trattieni… ed espira. Prontə per iniziare?",
'ja': "やあ！深呼吸しよう 🍃 — 鼻から吸って…止めて…吐いて。始める準備できた？",
'kn': "ಹಾಯ್! ಒಂದು ಆಳವಾದ ಉಸಿರಾಟ ತೆಗೆದುಕೊಳ್ಳೋಣ 🍃 — ಮೂಗಿನ ಮೂಲಕ ಉಸಿರೆಳೆ… ಹಿಡಿಸು… ಮತ್ತು ಬಿಟ್ಟುಬಿಡು. ಆರಂಭಿಸೋಣವೇ?",
'kk': "Сәлем! Терең дем алайық 🍃 — мұрынмен ішке… ұстап тұр… және шығарыңыз. Бастауға дайынсың ба?",
'ko': "안녕하세요! 깊이 숨을 쉬어볼까요 🍃 — 코로 들이마시고… 멈추고… 내쉬어요. 시작할 준비됐나요?",
'lv': "Sveiks! Ieelposim dziļi 🍃 — caur degunu… turi… un izelpo. Gatavs sākt?",
'lt': "Sveikas! Giliai įkvėpkime 🍃 — pro nosį… sulaikyk… ir iškvėpk. Pasiruošęs pradėti?",
'mk': "Здраво! Ајде да земеме длабок здив 🍃 — преку нос… задржи… и издиши. Подготвен/а за почеток?",
'ms': "Hai! Mari tarik nafas dalam-dalam 🍃 — melalui hidung… tahan… dan hembus perlahan. Sedia nak mula?",
'ml': "ഹായ്! നാം ഒരു ആഴമുള്ള ശ്വാസം എടുക്കാം 🍃 — മൂക്കിലൂടെ എടുത്ത്… നിർത്തി… പുറത്തിറക്കൂ. തുടങ്ങാനൊരുങ്ങിയോ?",
'mr': "हाय! चला एक खोल श्वास घेऊया 🍃 — नाकातून घ्या… थांबा… आणि बाहेर सोडा. सुरुवात करूया?",
'mn': "Сайн уу! Гүнзгий амьсгалцгаая 🍃 — хамраар амьсгалаа аваад… бариад… гаргаарай. Эхлэхэд бэлэн үү?",
'no': "Hei der! La oss ta et dypt pust 🍃 — inn gjennom nesen… hold… og pust ut. Klar til å begynne?",
'fa': "سلام! بیا یک نفس عمیق بکشیم 🍃 — از بینی... نگه دار... و بیرون بده. آماده‌ای شروع کنیم؟",
'pl': "Hej! Weźmy głęboki oddech 🍃 — przez nos… przytrzymaj… i wypuść. Gotowy/a, by zacząć?",
'pt': "Olá! Vamos respirar fundo 🍃 — pelo nariz… segura… e solta. Prontx para começar?",
'pa': "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਚਲੋ ਇੱਕ ਡੂੰਘੀ ਸਾਹ ਲਈਏ 🍃 — ਨੱਕ ਰਾਹੀਂ… ਰੋਕੋ… ਅਤੇ ਬਾਹਰ ਛੱਡੋ। ਸ਼ੁਰੂ ਕਰਨ ਲਈ ਤਿਆਰ ਹੋ?",
'ro': "Hei! Hai să inspirăm adânc 🍃 — pe nas… ține… și expiră. Ești gata să începem?",
'ru': "Привет! Давай глубоко вдохнём 🍃 — через нос… задержи… и выдохни. Готов(а) начать?",
'sr': "Ćao! Udahnimo duboko 🍃 — kroz nos… zadrži… i izdahni. Spreman/na za početak?",
'sk': "Ahoj! Nadýchajme sa zhlboka 🍃 — nosom… podrž… a vydýchni. Pripravený/á začať?",
'sl': "Živjo! Vdihnimo globoko 🍃 — skozi nos… zadrži… in izdihni. Pripravljen/a za začetek?",
'so': "Haye! Aan neefsano si qoto dheer 🍃 — sanka ku neefso… hayso… oo sii daa. Diyaar ma tahay?",
'es': "¡Hola! Tomemos una respiración profunda 🍃 — por la nariz… aguanta… y exhala. ¿Listo/a para comenzar?",
'sw': "Hujambo! Tupumue kwa kina 🍃 — kupitia puani… shikilia… na toa pumzi. Tayari kuanza?",
'sv': "Hej där! Ta ett djupt andetag 🍃 — in genom näsan… håll… och andas ut. Redo att börja?",
'tl': "Huy! Huminga tayo nang malalim 🍃 — sa ilong… pigilan… at huminga palabas. Game ka na ba?",
'ta': "வணக்கம்! ஒரு ஆழ்ந்த மூச்சு வாங்கலாம் 🍃 — மூக்கில் ஊதிக்கொண்டு… நிறுத்து… விடு. தொடங்க தயாரா?",
'te': "హాయ్! ఒక లోతైన ఊపిరి పీల్చుకుందాం 🍃 — ముక్కు ద్వారా… ఆపు… మరియు ఊపిరి విడిచిపెట్టు. ప్రారంభించడానికి సిద్ధంగా ఉన్నారా?",
'th': "สวัสดี! มาหายใจเข้าลึกๆ กัน 🍃 — ทางจมูก… กลั้นไว้… แล้วหายใจออก. พร้อมจะเริ่มยัง?",
'tr': "Selam! Derin bir nefes alalım 🍃 — burundan içeri… tut… ve ver. Başlamaya hazır mısın?",
'uk': "Привіт! Зробімо глибокий вдих 🍃 — через ніс… затримай… і видихни. Готовий/а починати?",
'ur': "ہیلو! ایک گہری سانس لیتے ہیں 🍃 — ناک سے اندر… روکیں… اور آہستہ چھوڑیں۔ شروع کرنے کے لیے تیار؟",
'vi': "Chào bạn! Hãy hít một hơi thật sâu 🍃 — qua mũi… giữ lại… rồi thở ra. Sẵn sàng bắt đầu chưa?",
'en': "Hey there! Let's take a deep breath 🍃 — in through the nose… hold… and exhale. Ready to begin?",

    },
    'boss': {
       
'sq': "Le të fillojmë, shef 💼 Sot është një ditë perfekte për hapa të guximshëm. Cili është lëvizja jonë e parë?",
'am': "እንግዲኛ እንጀምር, አለቃ 💼 ዛሬ በትክክል ቀን ነው የታላቅ እርምጃ ለመውሰድ። የመጀመሪያ እርምጃችን ምንድነው?",
'ar': "لنبدأ يا زعيم 💼 اليوم يوم رائع لاتخاذ خطوات جريئة. ما هي أول خطوة؟",
'hy': "Գործի անցնենք, շե՛ֆ 💼 Այսօր հիանալի օր է համարձակ քայլերի համար։ Ո՞րն է մեր առաջին քայլը։",
'bn': "চলুন শুরু করি, বস 💼 আজ সাহসী পদক্ষেপ নেওয়ার জন্য দারুণ দিন। আমাদের প্রথম পদক্ষেপ কী?",
'bs': "Krenimo, šefe 💼 Danas je sjajan dan za hrabre poteze. Koji je naš prvi korak?",
'bg': "Да действаме, шефе 💼 Днес е страхотен ден за смели стъпки. Каква е първата ни стъпка?",
'my': "စလော့မယ်နော်, ဥက္ကဌရေ 💼 ယနေ့ဟာ တော်တော်မိုက်တဲ့ တက်ကြွမှုအတွက် နေ့တစ်နေ့ပါ။ ပထမအဆင့်ကဘာလဲ?",
'ca': "Som-hi, cap 💼 Avui és un gran dia per fer passos valents. Quina és la nostra primera jugada?",
'zh': "开干吧，老板 💼 今天是迈出大胆一步的好日子。我们第一步是什么？",
'hr': "Idemo u akciju, šefe 💼 Danas je sjajan dan za hrabre korake. Koji je naš prvi potez?",
'cs': "Pojďme na to, šéfe 💼 Dnes je skvělý den pro odvážné kroky. Jaký bude náš první tah?",
'da': "Lad os komme i gang, boss 💼 I dag er perfekt til at tage modige skridt. Hvad er vores første træk?",
'nl': "Aan de slag, baas 💼 Vandaag is een topdag voor gedurfde stappen. Wat wordt onze eerste zet?",
'et': "Hakkame pihta, boss 💼 Täna on suurepärane päev julgeteks sammudeks. Mis on meie esimene käik?",
'fi': "Mennään asiaan, pomo 💼 Tänään on loistava päivä rohkeille askeleille. Mikä on meidän ensimmäinen siirto?",
'fr': "C’est parti, boss 💼 Aujourd’hui est une super journée pour oser. Quelle est notre première action ?",
'ka': "დავიწყოთ, ბოსო 💼 დღეს შესანიშნავი დღეა მამაც ნაბიჯებისთვის. რა იქნება პირველი ნაბიჯი?",
'de': "Los geht’s, Boss 💼 Heute ist ein großartiger Tag für mutige Schritte. Was ist unser erster Move?",
'el': "Πάμε, αφεντικό 💼 Σήμερα είναι ιδανική μέρα για τολμηρές κινήσεις. Ποιο είναι το πρώτο μας βήμα;",
'gu': "ચાલો શરૂ કરીએ, બોસ 💼 આજે সাহસિક પગલાં ભરવા માટે એક ઉત્તમ દિવસ છે. પ્રથમ પગલું શું છે?",
'hi': "चलिए शुरू करते हैं, बॉस 💼 आज बड़े फैसले लेने का शानदार दिन है। हमारी पहली चाल क्या होगी?",
'hu': "Vágjunk bele, főnök 💼 Ma remek nap a merész lépésekhez. Mi legyen az első lépésünk?",
'is': "Förum í þetta, yfirmaður 💼 Í dag er frábær dagur til að taka djarfar skref. Hver er fyrsta hreyfingin okkar?",
'id': "Yuk mulai, bos 💼 Hari ini hari yang tepat untuk ambil langkah berani. Langkah pertama kita apa?",
'it': "Diamoci dentro, capo 💼 Oggi è il giorno giusto per fare passi audaci. Qual è la nostra prima mossa?",
'ja': "さあ行きましょう、ボス 💼 今日は大胆な一歩を踏み出すのに最高の日です。最初のステップは何にしますか？",
'kn': "ಶುರುಮಾಡೋಣ ಬಾಸ್ 💼 ಇಂದು ಧೈರ್ಯದ ಹೆಜ್ಜೆಗೆ ಸೂಕ್ತವಾದ ದಿನ. ನಮ್ಮ ಮೊದಲ ಹೆಜ್ಜೆ ಏನು?",
'kk': "Бастайық, бастық 💼 Бүгін батыл қадамдар үшін керемет күн. Алғашқы қадамымыз қандай?",
'ko': "시작해봅시다, 보스 💼 오늘은 대담한 한 걸음을 내딛기 좋은 날이에요. 첫 번째 행동은 뭐죠?",
'lv': "Sāksim, priekšniek 💼 Šodien ir lieliska diena drosmīgiem soļiem. Kāds ir pirmais solis?",
'lt': "Pradėkime, bosas 💼 Šiandien puiki diena drąsiems žingsniams. Koks mūsų pirmas žingsnis?",
'mk': "Ајде да почнеме, шефе 💼 Денес е одличен ден за храбри потези. Кој е нашиот прв чекор?",
'ms': "Jom mula, bos 💼 Hari ini hari terbaik untuk buat langkah berani. Apa langkah pertama kita?",
'ml': "തുടങ്ങാം ബോസ് 💼 ഇന്ന് ധൈര്യമായ നടപടികൾക്ക് നല്ലൊരു ദിവസം. ആദ്യ നീക്കം എന്താണ്?",
'mr': "चला सुरुवात करूया, बॉस 💼 आज धाडसी निर्णय घेण्यासाठी उत्तम दिवस आहे. आपली पहिली चाल काय आहे?",
'mn': "За босс оо, эхэлье 💼 Өнөөдөр зоримог алхам хийхэд хамгийн тохиромжтой өдөр. Эхний алхам юу байх вэ?",
'no': "La oss sette i gang, sjef 💼 I dag er en flott dag for modige steg. Hva er vårt første trekk?",
'fa': "بزن بریم رئیس 💼 امروز یه روز عالیه برای برداشتن قدم‌های جسورانه. اولین قدممون چیه؟",
'pl': "Zaczynajmy, szefie 💼 Dziś świetny dzień na odważne kroki. Jaki będzie nasz pierwszy ruch?",
'pt': "Vamos nessa, chefe 💼 Hoje é um ótimo dia para passos ousados. Qual é o nosso primeiro passo?",
'pa': "ਆਓ ਸ਼ੁਰੂ ਕਰੀਏ, ਬੌਸ 💼 ਅੱਜ ਬੇਖ਼ੌਫ਼ ਕਦਮ ਚੁੱਕਣ ਲਈ ਵਧੀਆ ਦਿਨ ਹੈ। ਸਾਡਾ ਪਹਿਲਾ ਕਦਮ ਕੀ ਹੈ?",
'ro': "Hai să începem, șefule 💼 Azi e o zi perfectă pentru pași curajoși. Care e primul nostru pas?",
'ru': "Давайте начнем, босс 💼 Сегодня отличный день для смелых шагов. С чего начнем?",
'sr': "Krenimo, šefe 💼 Danas je sjajan dan za hrabre poteze. Koji je naš prvi korak?",
'sk': "Poďme na to, šéfe 💼 Dnes je skvelý deň na odvážne kroky. Aký bude náš prvý krok?",
'sl': "Začnimo, šef 💼 Danes je odličen dan za pogumne korake. Kaj je naša prva poteza?",
'so': "Aan bilowno, madax 💼 Maanta waa maalin ku habboon talaabooyin geesinimo leh. Tallaabada koowaad waa maxay?",
'es': "¡Vamos allá, jefe 💼 Hoy es un gran día para dar pasos valientes! ¿Cuál es nuestro primer movimiento?",
'sw': "Twende kazi, bosi 💼 Leo ni siku nzuri ya kuchukua hatua za ujasiri. Hatua yetu ya kwanza ni ipi?",
'sv': "Nu kör vi, chefen 💼 Idag är en perfekt dag för modiga steg. Vad är vårt första drag?",
'tl': "Tara na, boss 💼 Ngayon ang perfect day para sumubok ng matatapang na hakbang. Ano'ng unang galaw natin?",
'ta': "வாங்க ஆரம்பிக்கலாம், தலைவர் 💼 இன்று தைரியமான ஒரு அடி எடுப்பதற்கு சிறந்த நாள். முதல் நகர்வு என்ன?",
'te': "బాస్, మొదలుపెడ్దాం 💼 నేడు ధైర్యవంతమైన అడుగులు వేయడానికి గొప్ప రోజు. మన మొదటి అడుగు ఏమిటి?",
'th': "มาเริ่มกันเลย บอส 💼 วันนี้เหมาะมากกับการก้าวอย่างกล้าหาญ ก้าวแรกของเราคืออะไร?",
'tr': "Hadi başlayalım patron 💼 Bugün cesur adımlar atmak için harika bir gün. İlk adımımız ne olacak?",
'uk': "Почнімо, босе 💼 Сьогодні чудовий день для сміливих кроків. Який наш перший крок?",
'ur': "چلیں شروع کریں، باس 💼 آج بہادر قدم اٹھانے کا زبردست دن ہے۔ ہمارا پہلا قدم کیا ہوگا؟",
'vi': "Bắt đầu thôi sếp 💼 Hôm nay là ngày tuyệt vời để bước đi táo bạo. Bước đầu tiên của ta là gì?",

    },
	'heart': {
        
'sq': "Jam këtu për ty 💜 Më trego çfarë ndjen ose ëndërron sot ☺️",
'am': "እኔ ከአንተ ጋር ነኝ 💜 ዛሬ ምን ስሜት አለህ/ሽ ወይም ምን እትም እትማለህ/ሽ? ☺️",
'ar': "أنا هنا من أجلك 💜 أخبرني بما تشعر أو تحلم به اليوم ☺️",
'hy': "Ես այստեղ եմ քեզ համար 💜 Ասա ինձ՝ այսօր ինչ ես զգում կամ ինչի մասին ես երազում ☺️",
'bn': "আমি তোমার পাশে আছি 💜 আজ তুমি কী অনুভব করছো বা কী স্বপ্ন দেখছো বলো ☺️",
'bs': "Tu sam za tebe 💜 Reci mi kako se danas osjećaš ili o čemu sanjaš ☺️",
'bg': "Аз съм тук за теб 💜 Кажи ми какво чувстваш или за какво мечтаеш днес ☺️",
'my': "ငါနင်အတွက်ရှိနေပါတယ် 💜 ဒီနေ့ဘယ်လိုခံစားနေတာလဲ၊ မို့လားအိပ်မက်တွေနဲ့လား ပြောပါ ☺️",
'ca': "Soc aquí per tu 💜 Explica’m què sents o què somies avui ☺️",
'zh': "我在这里陪着你 💜 今天你在感觉什么，或在做什么梦呢？☺️",
'hr': "Tu sam za tebe 💜 Reci mi kako se osjećaš ili o čemu sanjaš danas ☺️",
'cs': "Jsem tu pro tebe 💜 Řekni mi, co dnes cítíš nebo o čem sníš ☺️",
'da': "Jeg er her for dig 💜 Fortæl mig, hvad du føler eller drømmer om i dag ☺️",
'nl': "Ik ben er voor je 💜 Vertel me wat je vandaag voelt of waar je over droomt ☺️",
'et': "Ma olen sinu jaoks olemas 💜 Räägi mulle, mida sa täna tunned või millest unistad ☺️",
'fi': "Olen täällä sinua varten 💜 Kerro, mitä tunnet tai mistä unelmoit tänään ☺️",
'fr': "Je suis là pour toi 💜 Dis-moi ce que tu ressens ou ce dont tu rêves aujourd’hui ☺️",
'ka': "აქ ვარ შენთვის 💜 მითხარი, რას გრძნობ ან რას ოცნებობ დღეს ☺️",
'de': "Ich bin für dich da 💜 Erzähl mir, was du heute fühlst oder wovon du träumst ☺️",
'el': "Είμαι εδώ για σένα 💜 Πες μου πώς νιώθεις ή τι ονειρεύεσαι σήμερα ☺️",
'gu': "હું તારી સાથે છું 💜 આજે તું શું અનુભવી રહ્યો છે કે શું સપના જોઈ રહ્યો છે મને કહો ☺️",
'hi': "मैं तुम्हारे साथ हूँ 💜 आज तुम क्या महसूस कर रहे हो या क्या सपना देख रहे हो, बताओ ☺️",
'hu': "Itt vagyok neked 💜 Mondd el, mit érzel vagy miről álmodsz ma ☺️",
'is': "Ég er hér fyrir þig 💜 Segðu mér hvað þú ert að finna eða dreyma um í dag ☺️",
'id': "Aku di sini untukmu 💜 Ceritakan apa yang kamu rasakan atau impikan hari ini ☺️",
'it': "Sono qui per te 💜 Dimmi cosa provi o cosa sogni oggi ☺️",
'ja': "私はあなたの味方だよ 💜 今日はどんな気持ち？どんな夢を見てる？☺️",
'kn': "ನಾನು ನಿನ್ನ ಜೊತೆ ಇದ್ದೀನಿ 💜 ಇಂದು ನಿನಗೆ ಏನು ಅನಿಸುತಿದೆ ಅಥವಾ ಯಾವ ಕನಸು ಕಾಣುತ್ತಿದ್ದೀಯೋ ಹೇಳು ☺️",
'kk': "Мен сен үшін осындамын 💜 Бүгін не сезіп тұрсың немесе не армандадың? ☺️",
'ko': "내가 여기 있어요 💜 오늘 어떤 기분이 드나요, 혹은 무슨 꿈을 꾸고 있나요? ☺️",
'lv': "Es esmu šeit tev 💜 Pastāsti man, ko tu jūti vai par ko sapņo šodien ☺️",
'lt': "Esu čia dėl tavęs 💜 Papasakok, ką jauti ar apie ką svajoji šiandien ☺️",
'mk': "Тука сум за тебе 💜 Кажи ми што чувствуваш или за што сонуваш денес ☺️",
'ms': "Saya ada di sini untuk awak 💜 Ceritakan apa yang awak rasa atau impikan hari ini ☺️",
'ml': "ഞാൻ നിന്നോടൊപ്പം ഇരിക്കുകയാണ് 💜 ഇന്ന് നീ എന്താണ് അനുഭവിക്കുന്നത് അല്ലെങ്കിൽ സ്വപ്നം കാണുന്നത് ☺️",
'mr': "मी तुझ्यासाठी इथे आहे 💜 आज तुला काय वाटतंय किंवा तू काय स्वप्न पाहतो आहेस ते सांग ☺️",
'mn': "Би чамд туслах гэж энд байна 💜 Өнөөдөр юу мэдэрч байгаа эсвэл юунд мөрөөдөн байна вэ? ☺️",
'no': "Jeg er her for deg 💜 Fortell meg hva du føler eller drømmer om i dag ☺️",
'fa': "من اینجام برای تو 💜 بهم بگو امروز چه حسی داری یا چه رویایی در سر داری ☺️",
'pl': "Jestem tu dla Ciebie 💜 Powiedz mi, co dziś czujesz albo o czym marzysz ☺️",
'pt': "Estou aqui por você 💜 Me conta o que você está sentindo ou sonhando hoje ☺️",
'pa': "ਮੈਂ ਤੇਰੇ ਲਈ ਇੱਥੇ ਹਾਂ 💜 ਅੱਜ ਤੂੰ ਕੀ ਮਹਿਸੂਸ ਕਰ ਰਿਹਾ/ਰਹੀ ਹੈਂ ਜਾਂ ਕੀ ਸੁਪਨਾ ਦੇਖ ਰਿਹਾ/ਰਹੀ ਹੈਂ, ਦੱਸ ☺️",
'ro': "Sunt aici pentru tine 💜 Spune-mi ce simți sau ce visezi azi ☺️",
'ru': "Я рядом с тобой 💜 Расскажи, что ты чувствуешь или о чём мечтаешь сегодня ☺️",
'sr': "Tu sam za tebe 💜 Reci mi šta osećaš ili o čemu sanjaš danas ☺️",
'sk': "Som tu pre teba 💜 Povedz mi, čo cítiš alebo o čom dnes snívaš ☺️",
'sl': "Tukaj sem zate 💜 Povej mi, kaj danes čutiš ali sanjaš ☺️",
'so': "Waxaan kuu joogaa 💜 Ii sheeg waxaad dareemeyso ama ku riyoonayso maanta ☺️",
'es': "Estoy aquí para ti 💜 Cuéntame qué sientes o qué sueñas hoy ☺️",
'sw': "Niko hapa kwa ajili yako 💜 Niambie unajisikiaje au unaota ndoto gani leo ☺️",
'sv': "Jag är här för dig 💜 Berätta vad du känner eller drömmer om idag ☺️",
'tl': "Nandito ako para sa’yo 💜 Sabihin mo sa’kin kung ano ang nararamdaman mo o pinapangarap ngayon ☺️",
'ta': "நான் உனக்காக இங்கே இருக்கிறேன் 💜 இன்று நீ என்ன உணர்கிறாய் அல்லது கனவு காண்கிறாய் என்பதை சொல் ☺️",
'te': "నేను నిన్ను కోసమే ఇక్కడ ఉన్నాను 💜 నీవు ఈరోజు ఏమి అనుభవిస్తున్నావో లేదా కలగంటున్నావో చెప్పు ☺️",
'th': "ฉันอยู่ตรงนี้เพื่อคุณ 💜 บอกฉันสิว่าวันนี้คุณรู้สึกหรือฝันถึงอะไร ☺️",
'tr': "Senin için buradayım 💜 Bugün ne hissediyor ya da ne hayal ediyorsun, bana anlat ☺️",
'uk': "Я поруч із тобою 💜 Розкажи, що ти відчуваєш або про що мрієш сьогодні ☺️",
'ur': "میں تمہارے لیے یہاں ہوں 💜 مجھے بتاؤ آج تم کیا محسوس کر رہے ہو یا کیا خواب دیکھ رہے ہو ☺️",
'vi': "Mình ở đây vì bạn 💜 Hãy nói mình biết hôm nay bạn cảm thấy thế nào hoặc đang mơ điều gì nhé ☺️",

    },
'sparkle': {

'sq': "Hej! Je gati të shpërndash pak gëzim dhe të bësh punë fantastike? ✨",
'am': "ሰላም ልጅ! ደስታ ማበርበርና ሥራዎችን ማጠናቀቅ ዝግጁ/ዝግጅት ነዎት? ✨",
'ar': "مرحباً! هل أنت مستعد لنشر الفرح وإنجاز المهام؟ ✨",
'hy': "Ողջույն։ Պատրա՞ստ ես տարածել ուրախություն ու անել բաներ ✨",
'bn': "হেলো! তুমি কি আনন্দ ছড়াতে ও কিছু দারুণ কাজ করতে প্রস্তুত? ✨",
'bs': "Ćao! Jesi li spreman/na širiti radost i završiti stvari? ✨",
'bg': "Здравей! Готов/а ли си да разпръснеш радост и да свършиш нещата? ✨",
'my': "ဟယ်လို! ပျော်ရွှင်မှုမျှဝေရန်နဲ့ တကယ်ပြီးမြောက်အောင်လုပ်ဖို့ ပြင်ဆင်ပြီးပြီလား? ✨",
'ca': "Hola! Estàs a punt per repartir alegria i fer que les coses passin? ✨",
'zh': "嗨，你好！准备好传播快乐、完成任务了吗？✨",
'hr': "Bok! Jesi li spreman/na širiti veselje i obaviti stvari? ✨",
'cs': "Ahoj! Jsi připraven/a šířit radost a něco dokončit? ✨",
'da': "Hej! Klar til at sprede glæde og få tingene gjort? ✨",
'nl': "Hoi daar! Ben je klaar om wat vreugde te verspreiden en dingen gedaan te krijgen? ✨",
'et': "Tere! Kas oled valmis levitama rõõmu ja asjad ära tegema? ✨",
'fi': "Moikka! Oletko valmis levittämään iloa ja saamaan asioita aikaan? ✨",
'fr': "Coucou ! Prêt(e) à semer de la joie et passer à l’action ? ✨",
'ka': "გამარჯობა! მზად ხარ სიხარული გაავრცელო და საქმეები მოაგვარო? ✨",
'de': "Hallo du! Bereit, ein bisschen Freude zu verbreiten und was zu schaffen? ✨",
'el': "Γεια σου! Είσαι έτοιμος/η να μοιράσεις χαρά και να κάνεις πράγματα; ✨",
'gu': "હાય! શું તમે ખુશી ફેલાવવા અને કામ પૂરું કરવા માટે તૈયાર છો? ✨",
'hi': "हाय! क्या तुम थोड़ी खुशियाँ बाँटने और काम पूरे करने के लिए तैयार हो? ✨",
'hu': "Helló! Készen állsz egy kis örömöt hozni és dolgokat elvégezni? ✨",
'is': "Hæ! Ertu tilbúin/n að dreifa gleði og klára verkefni? ✨",
'id': "Hai! Siap untuk sebarkan kebahagiaan dan selesaikan hal-hal? ✨",
'it': "Ciao! Sei prontə a diffondere un po’ di gioia e portare a termine le cose? ✨",
'ja': "やっほー！ワクワクを広げて、やること片付ける準備できてる？✨",
'kn': "ಹಾಯ್! ನಗು ಹಂಚಲು ಮತ್ತು ಕೆಲಸಗಳನ್ನು ಮುಗಿಸಲು ಸಿದ್ಧವಿದ್ದೀಯಾ? ✨",
'kk': "Сәлем! Қуаныш таратуға және істерді бітіруге дайынсың ба? ✨",
'ko': "안녕! 기쁨을 퍼뜨리고 할 일 끝낼 준비 됐어? ✨",
'lv': "Sveiks! Vai esi gatavs dalīties priekā un paveikt lietas? ✨",
'lt': "Labas! Pasiruošęs skleisti džiaugsmą ir atlikti darbus? ✨",
'mk': "Здраво! Подготвен/а си да шириш радост и да завршиш некои работи? ✨",
'ms': "Hai! Dah bersedia nak sebarkan kegembiraan dan selesaikan kerja? ✨",
'ml': "ഹായ്! സന്തോഷം പകർന്നുകൊണ്ട് കാര്യങ്ങൾ പൂര്‍ത്തിയാക്കാൻ തയാറാണോ? ✨",
'mr': "हाय! आनंद पसरवण्यासाठी आणि काहीतरी कामं पूर्ण करण्यासाठी तयार आहेस का? ✨",
'mn': "Сайн уу! Жаахан баяр хөөр түгээж, хийх ажлаа амжуулахад бэлэн үү? ✨",
'no': "Hei! Klar for å spre litt glede og få ting gjort? ✨",
'fa': "سلام! آماده‌ای شادی پخش کنی و کارهات رو انجام بدی؟ ✨",
'pl': "Cześć! Gotowy/a, żeby szerzyć radość i załatwić sprawy? ✨",
'pt': "Oi! Prontx para espalhar alegria e fazer acontecer? ✨",
'pa': "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਤਿਆਰ ਹੋ ਖੁਸ਼ੀ ਫੈਲਾਉਣ ਅਤੇ ਕੰਮ ਮੁਕੰਮਲ ਕਰਨ ਲਈ? ✨",
'ro': "Salut! Ești gata să răspândești bucurie și să trecem la treabă? ✨",
'ru': "Приветик! Готов(а) распространять радость и сделать что-то крутое? ✨",
'sr': "Ćao! Spreman/na da širiš radost i obaviš stvari? ✨",
'sk': "Ahoj! Si pripravený/á šíriť radosť a niečo urobiť? ✨",
'sl': "Živjo! Si pripravljen/a širiti veselje in opraviti stvari? ✨",
'so': "Salaan! Ma diyaar baad u tahay inaad farxad faafiso oo hawlaha qabato? ✨",
'es': "¡Hola! ¿Listo/a para repartir alegría y lograr cosas geniales? ✨",
'sw': "Hujambo! Uko tayari kusambaza furaha na kukamilisha mambo? ✨",
'sv': "Hej där! Är du redo att sprida glädje och få saker gjorda? ✨",
'tl': "Hiii! Ready ka na bang magkalat ng good vibes at tapusin ang mga gawain? ✨",
'ta': "வணக்கம்! சந்தோஷத்தை பகிர்ந்து சில காரியங்களை முடிக்க தயாரா? ✨",
'te': "హాయ్! ఆనందాన్ని పంచేందుకు మరియు పనులు పూర్తి చేయడానికి సిద్ధంగా ఉన్నావా? ✨",
'th': "สวัสดี! พร้อมจะส่งต่อความสุขและทำสิ่งต่างๆ ให้สำเร็จไหม? ✨",
'tr': "Selam! Neşeni yaymaya ve işleri halletmeye hazır mısın? ✨",
'uk': "Привіт! Готовий/а дарувати радість і діяти? ✨",
'ur': "ہیلو! کیا آپ خوشیاں پھیلانے اور کام مکمل کرنے کے لیے تیار ہیں؟ ✨",
'vi': "Chào bạn! Sẵn sàng lan tỏa niềm vui và hoàn thành mọi việc chưa? ✨",

    },
'default': {
       
'sq': "Hej! Unë jam Carmela, asistentja jote personale. Si po të shkon dita?",
'am': "ሰላም! እኔ ካርሜላ ነኝ፣ የአንተ የግል ረዳት። ቀኑ እንዴት ነው?",
'ar': "مرحباً! أنا كارميلا، مساعدتك الشخصية. كيف يسير يومك؟",
'hy': "Ողջույն։ Ես Կարմելան եմ՝ քո անձնական օգնականը։ Ինչպես է անցնում օրըդ?",
'bn': "হেই! আমি কারমেলা, তোমার পার্সোনাল অ্যাসিস্ট্যান্ট। আজকের দিন কেমন যাচ্ছে?",
'bs': "Hej! Ja sam Carmela, tvoja lična asistentkinja. Kako ti ide dan?",
'bg': "Здрасти! Аз съм Кармела, твоята лична асистентка. Как върви денят ти?",
'my': "ဟေး! ကျွန်မက Carmela ပါ၊ မင်းရဲ့ကိုယ်ပိုင်အကူအညီပေးသူ။ မင်းရဲ့နေ့က ဘယ်လိုဖြတ်သွားနေလဲ?",
'ca': "Hola! Sóc la Carmela, la teva assistent personal. Com va el teu dia?",
'zh': "嗨！我是 Carmela，你的个人助手。今天过得怎么样？",
'hr': "Hej! Ja sam Carmela, tvoja osobna asistentica. Kako ti ide dan?",
'cs': "Ahoj! Jsem Carmela, tvoje osobní asistentka. Jak se máš dnes?",
'da': "Hej der! Jeg er Carmela, din personlige assistent. Hvordan går din dag?",
'nl': "Hoi daar! Ik ben Carmela, jouw persoonlijke assistente. Hoe gaat je dag?",
'et': "Tere! Mina olen Carmela, sinu isiklik assistent. Kuidas su päev läheb?",
'fi': "Moikka! Olen Carmela, sinun henkilökohtainen avustajasi. Miten päiväsi sujuu?",
'fr': "Coucou ! Je suis Carmela, ton assistante personnelle. Comment se passe ta journée ?",
'ka': "გამარჯობა! მე ვარ კარმელა, შენი პერსონალური ასისტენტი. როგორ მიდის შენი დღე?",
'de': "Hallo! Ich bin Carmela, deine persönliche Assistentin. Wie läuft dein Tag?",
'el': "Γεια σου! Είμαι η Καρμέλα, η προσωπική σου βοηθός. Πώς πάει η μέρα σου;",
'gu': "હાય! હું કાર્મેલા છું, તારી વ્યક્તિગત સહાયક. તારો દિવસ કેમ ચાલી રહ્યો છે?",
'hi': "हाय! मैं कार्मेला हूँ, तुम्हारी पर्सनल असिस्टेंट। आज तुम्हारा दिन कैसा जा रहा है?",
'hu': "Szia! Carmela vagyok, a személyes asszisztensed. Hogy telik a napod?",
'is': "Hæ! Ég er Carmela, aðstoðarmaðurinn þinn. Hvernig gengur dagurinn þinn?",
'id': "Hai! Aku Carmela, asisten pribadimu. Gimana harimu sejauh ini?",
'it': "Ciao! Sono Carmela, la tua assistente personale. Come sta andando la tua giornata?",
'ja': "やあ！私はカーメラ、あなたのパーソナルアシスタントだよ。今日一日どう？",
'kn': "ಹಾಯ್! ನಾನು ಕರ್ಮೆಲಾ, ನಿನ್ನ ವೈಯಕ್ತಿಕ ಸಹಾಯಕರಾಗಿದ್ದೇನೆ. ನಿನ್ನ ದಿನ ಹೇಗಿದೆ?",
'kk': "Сәлем! Мен Кармела, сенің жеке көмекшіңмін. Күнің қалай өтіп жатыр?",
'ko': "안녕하세요! 저는 카르멜라예요, 당신의 개인 비서입니다. 오늘 하루 어때요?",
'lv': "Sveiks! Esmu Carmela, tava personīgā asistente. Kā tev klājas šodien?",
'lt': "Labas! Aš esu Carmela, tavo asmeninė asistentė. Kaip sekasi šiandien?",
'mk': "Здраво! Јас сум Кармела, твојата лична асистентка. Како ти поминува денот?",
'ms': "Hai! Saya Carmela, pembantu peribadi anda. Bagaimana hari anda?",
'ml': "ഹായ്! ഞാൻ കർമേലാ, നിന്റെ വ്യക്തിഗത സഹായിയായി. നിന്റെ ദിവസം എങ്ങിനെയാണ് പോകുന്നത്?",
'mr': "हाय! मी कार्मेला, तुझी वैयक्तिक सहाय्यक आहे. तुझा दिवस कसा चाललाय?",
'mn': "Сайн уу! Би Кармела, чиний хувийн туслагч. Өнөөдөр ямар байна?",
'no': "Hei der! Jeg er Carmela, din personlige assistent. Hvordan går dagen din?",
'fa': "سلام! من کارملا هستم، دستیار شخصی شما. روزت چطور پیش می‌ره؟",
'pl': "Hej! Jestem Carmela, twoja osobista asystentka. Jak mija twój dzień?",
'pt': "Oi! Eu sou a Carmela, sua assistente pessoal. Como está seu dia?",
'pa': "ਸਤ ਸ੍ਰੀ ਅਕਾਲ! ਮੈਂ ਕਾਰਮੇਲਾ ਹਾਂ, ਤੇਰੀ ਨਿੱਜੀ ਮਦਦਗਾਰ। ਤੇਰਾ ਦਿਨ ਕਿਵੇਂ ਜਾ ਰਿਹਾ ਹੈ?",
'ro': "Salut! Sunt Carmela, asistenta ta personală. Cum merge ziua ta?",
'ru': "Привет! Я Кармела, твоя личная помощница. Как проходит твой день?",
'sr': "Ćao! Ja sam Carmela, tvoja lična asistentkinja. Kako ti prolazi dan?",
'sk': "Ahoj! Ja som Carmela, tvoja osobná asistentka. Ako ide tvoj deň?",
'sl': "Živjo! Sem Carmela, tvoja osebna pomočnica. Kako ti gre danes?",
'so': "Salaan! Waxaan ahay Carmela, kaaliyahaaga shakhsiga ah. Sidee maalintaadu u socotaa?",
'es': "¡Hola! Soy Carmela, tu asistente personal. ¿Cómo va tu día?",
'sw': "Hujambo! Mimi ni Carmela, msaidizi wako binafsi. Siku yako inaendaje?",
'sv': "Hej där! Jag är Carmela, din personliga assistent. Hur går din dag?",
'tl': "Hello! Ako si Carmela, ang personal assistant mo. Kumusta ang araw mo?",
'ta': "வணக்கம்! நான் கம்ரேலா, உங்களின் தனிப்பட்ட உதவியாளர். உங்கள் நாள் எப்படி செல்கிறது?",
'te': "హాయ్! నేనే కార్మెలా, నీ పర్సనల్ అసిస్టెంట్. నేడు ఎలా ఉంది నీ రోజు?",
'th': "สวัสดี! ฉันชื่อคาร์เมล่า ผู้ช่วยส่วนตัวของคุณ วันนี้เป็นยังไงบ้าง?",
'tr': "Selam! Ben Carmela, senin kişisel asistanınım. Günün nasıl geçiyor?",
'uk': "Привіт! Я Кармела, твоя особиста помічниця. Як проходить твій день?",
'ur': "ہیلو! میں کارمیلا ہوں، آپ کی ذاتی معاون۔ آپ کا دن کیسا جا رہا ہے؟",
'vi': "Chào bạn! Mình là Carmela, trợ lý cá nhân của bạn. Hôm nay của bạn thế nào rồi?",

    },
}





@login_required
def chatbot(request):
    mode = request.GET.get('mode', 'default')
    try:
        soul = SoulThread.objects.get(user=request.user)
        preferred_lang = soul.preferred_language or 'en'
    except SoulThread.DoesNotExist:
        preferred_lang = 'en'

    base_text = BASE_GREETINGS.get(mode, BASE_GREETINGS['default'])
    
    # ✅ Only pass the selected language string
    greeting = base_text.get(preferred_lang, base_text.get('en', "Hello there!"))

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
            model="gpt-3.5-turbo",
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
            model="gpt-3.5-turbo",
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

def get_prompt_for_goal(goal):
    if goal == 'content calendar':
        return (
            "You are a content strategist. Organize the input into a clear content calendar:\n"
            "- Use week headers (e.g., Week 1: July 1–5)\n"
            "- Dates as subheadings (e.g., July 1)\n"
            "- Bullet points for tasks\n"
            "- Use → for extra notes\n"
            "- Do NOT format using markdown, emojis, or HTML"
        )
    elif goal == 'blog post':
        return (
            "You're a professional blog editor. Turn the notes into a clean outline:\n"
            "- Suggest a title\n"
            "- Write a 1–2 line intro\n"
            "- Add 3–6 section headings with 2–3 bullets each\n"
            "- Conclude with a takeaway idea\n"
            "- No markdown, no formatting syntax"
        )
    elif goal == 'launch plan':
        return (
            "You’re a launch strategist. Create a phased launch plan:\n"
            "- Break into sections like Pre-launch, Launch Week, Post-launch\n"
            "- Use bullet points for each phase\n"
            "- Include notes using → when needed"
        )
    elif goal == 'course roadmap':
        return (
            "You’re an instructional designer. Create a course roadmap:\n"
            "- Suggest a course title\n"
            "- Break into weeks or modules\n"
            "- List 2–3 lessons per module\n"
            "- Use → for optional notes"
        )
    elif goal == 'email sequence':
        return (
            "You're an email strategist. Build a 3–5 step email sequence:\n"
            "- Email 1, Email 2, etc.\n"
            "- Subject lines + short summaries\n"
            "- Keep tone warm and helpful"
        )
    elif goal == 'goal breakdown':
        return (
            "You're a clarity coach. Break the big goal into steps:\n"
            "- Start with the goal rephrased clearly\n"
            "- List 3–5 key steps\n"
            "- Add subtasks with → when needed"
        )
    else:
        return (
            "Organize this content into a clear, logical structure using bullet points and simple headings. No formatting syntax."
        )

@login_required
def organize_tool(request):
    result = None
    raw_notes = ''
    goal = ''

    if request.method == 'POST':
        raw_notes = request.POST.get('notes', '').strip()
        goal = request.POST.get('goal', '').strip()

        if raw_notes and goal:
            system_prompt = get_prompt_for_goal(goal)

            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": raw_notes}
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

