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
