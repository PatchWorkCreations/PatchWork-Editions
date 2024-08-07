from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect

def home_page(request):
    if request.method == 'POST':
        return handle_post_request(request, 'home')
    return render(request, 'iRiseup.html')

def memoir(request):
    if request.method == 'POST':
        return handle_post_request(request, 'memoir')
    return render(request, 'memoir.html')

def biography(request):
    if request.method == 'POST':
        return handle_post_request(request, 'biography')
    return render(request, 'biography.html')

def book_trailer(request):
    if request.method == 'POST':
        return handle_post_request(request, 'booktrailer')
    return render(request, 'booktrailer.html')

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
    if request.method == 'POST':
        return handle_post_request(request, 'book-trailer')
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
    if request.method == 'POST':
        return handle_post_request(request, 'memoir')
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

def handle_post_request(request, redirect_view):
    if request.POST.get('signup'):
        return handle_signup(request, redirect_view)
    elif request.POST.get('lets_start'):
        return handle_lets_start(request, redirect_view)
    elif request.POST.get('subscribe'):
        return handle_subscribe(request, redirect_view)
    elif request.POST.get('reaching_out'):
        return handle_reaching_out(request, redirect_view)
    elif request.POST.get('register'):
        return handle_register(request, redirect_view)
    elif request.POST.get('send_message'):
        return handle_send_message(request, redirect_view)
    return redirect(redirect_view)

def handle_signup(request, redirect_view):
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

    admin_subject = "SIGN UP FORM"
    admin_content = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    admin_email = EmailMessage(admin_subject, admin_content, to=['iriseuppublishing@gmail.com'])
    admin_email.send()

    messages.success(request, 'Submitted successfully!')
    return redirect(redirect_view)

def handle_lets_start(request, redirect_view):
    name = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('number')

    user_subject = "Thank You for Registering with iPatchwork Editions!"
    user_content = f"""
Dear {name},

Thank you for registering with iPatchwork Editions! We're thrilled to have you on board.

Your registration is confirmed, and you're now part of our community of authors and creators. Whether you're an aspiring writer or an experienced author, we're here to support you on your publishing journey.

Stay tuned for updates, tips, and exclusive offers tailored just for you. If you have any questions or need assistance, feel free to reach out to our team at iriseuppublishing@gmail.com .

We look forward to helping you achieve your publishing goals!

Best regards,
iPatchwork Editions Team
    """

    user_email = EmailMessage(user_subject, user_content, to=[email])
    user_email.send()

    admin_subject = "SIGN UP FORM"
    admin_content = f"Name: {name}\nEmail: {email}\nNumber: {number}"
    admin_email = EmailMessage(admin_subject, admin_content, to=['iriseuppublishing@gmail.com'])
    admin_email.send()

    messages.success(request, 'Submitted successfully!')
    return redirect(redirect_view)

def handle_subscribe(request, redirect_view):
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

    admin_subject = "SUBSCRIBE"
    admin_content = f"Email: {email}"
    admin_email = EmailMessage(admin_subject, admin_content, to=['iriseuppublishing@gmail.com'])
    admin_email.send()

    messages.success(request, 'Submitted successfully!')
    return redirect(redirect_view)

def handle_reaching_out(request, redirect_view):
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

    admin_subject = "CONTACT US"
    admin_content = f"Name: {name}\nEmail: {email}\nSubject: {subject_field}\nMessage: {message}"
    admin_email = EmailMessage(admin_subject, admin_content, to=['iriseuppublishing@gmail.com'])
    admin_email.send()

    messages.success(request, 'Submitted successfully!')
    return redirect(redirect_view)

def handle_register(request, redirect_view):
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

    admin_subject = "GET QUOTE"
    admin_content = f"Name: {name}\nEmail: {email}\nNumber: {number}\nMessage: {message}"
    admin_email = EmailMessage(admin_subject, admin_content, to=['iriseuppublishing@gmail.com'])
    admin_email.send()

    messages.success(request, 'Submitted successfully!')
    return redirect(redirect_view)

def handle_send_message(request, redirect_view):
    name = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('phone')
    message = request.POST.get('message')
    project_details = request.POST.get('project_details')

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

    admin_subject = "GET QUOTE"
    admin_content = f"Name: {name}\nEmail: {email}\nNumber: {number}\nMessage: {message}\nProject Details: {project_details}"
    admin_email = EmailMessage(admin_subject, admin_content, to=['iriseuppublishing@gmail.com'])
    admin_email.send()

    messages.success(request, 'Submitted successfully!')
    return redirect(redirect_view)

def csrf_failure(request, reason=""):
    return render(request, 'csrf_failure.html', {"reason": reason})


def exclusiveoffer(request):
    if request.method == 'POST':
        return handle_post_request(request, 'exclusiveoffer')
    return render(request, 'ExclusiveOffer.html')





