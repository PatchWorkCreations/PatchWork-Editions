from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',  index2, name='index2'),
    path('iPatchWork-Edition', home_page, name='home'),
    path('about', about, name='about'),
    path('editing', editing, name='editing'),
    path('publishing', publishing, name='publishing'),
    path('design', design, name='design'),
    path('marketing', marketing, name='marketing'),
    path('bloglist', bloglist, name='bloglist'),
    path('contact', contact, name='contact'),
    path('all-events', all_events, name='all-events'),
    path('audiobook', audiobook, name='audiobook'),
    path('autobiography', autobiography, name='autobiography'),
    path('biography', biography, name='biography'),
    path('blog-left-sidebar', blog_left_sidebar, name='blog-left-sidebar'),
    path('blog-list', blog_list, name='blog-list'),
    path('blog-right-sidebar', blog_right_sidebar, name='blog-right-sidebar'),
    path('book-trailer', book_trailer, name='book-trailer'),
    path('childrens-book', childrens_book, name='childrens-book'),
    path('comic-book', comic_book, name='comic-book'),
    path('horror-writing', horror_writing, name='horror-writing'),
    path('index', index, name='index'),
    path('index-3', index_3, name='index-3'),
    path('index-4', index_4, name='index-4'),
    path('index-5', index_5, name='index-5'),
    path('index-6', index_6, name='index-6'),
    path('left-sidebar', left_sidebar, name='left-sidebar'),
    path('manuscript', manuscript, name='manuscript'),
    path('memoir', memoir, name='memoir'),
    path('non-fiction', non_fiction, name='non-fiction'),
    path('page-left-sidebar', page_left_sidebar, name='page-left-sidebar'),
    path('page-right-sidebar', page_right_sidebar, name='page-right-sidebar'),
    path('page-without-sidebar', page_without_sidebar, name='page-without-sidebar'),
    path('privacy-policy', privacy_policy, name='privacy-policy'),
    path('right-sidebar', right_sidebar, name='right-sidebar'),
    path('screen-writing', screen_writing, name='screen-writing'),
    path('single-blog', single_blog, name='single-blog'),
    path('single-event', single_event, name='single-event'),
    path('terms-and-condition', terms_and_condition, name='terms-and-condition'),
    path('wfgconvention', wfgconvention, name='wfgconvention'),
    path('single-blog1', single_blog1, name='single-blog1'),
    path('single-blog2', single_blog2, name='single-blog2'),
    path('single-blog3', single_blog3, name='single-blog3'),
    path('single-blog4', single_blog4, name='single-blog4'),
    path('single-blog5', single_blog5, name='single-blog5'),
    path('includeblog', includeblog, name='includeblog'),
     path('includeevents', includeevents, name='includeevents'),
    path('single-blog6', single_blog6, name='single-blog6'),
    path('single-blog7', single_blog7, name='single-blog7'),
    path('single-blog8', single_blog8, name='single-blog8'),
    path('testimonial', testimonial, name='testimonial'),
    path('about/',  about, name='about'),
    path('blog-classic/',  blogclassic, name='blogclassic'),
    
    path('contact/',  contact, name='contact'),
    path('faq/',  faq, name='faq'),
    
    path('index-3/',  index3, name='index3'),
    
    path('not-found/',  notfound, name='notfound'),
    path('pricing/',  pricing, name='pricing'),
    path('register/',  register, name='register'),
    path('reset/',  reset, name='reset'),
    path('team/',  team, name='team'),
    path('testimonial/',  testimonial, name='testimonial'),
    path('news-detail1/',  newsdetail1, name='newsdetail1'),
    path('news-detail2/',  newsdetail2, name='newsdetail2'),
    path('news-detail3/',  newsdetail3, name='newsdetail3'),
    path('news-detail4/',  newsdetail4, name='newsdetail4'),
    path('news-detail5/',  newsdetail5, name='newsdetail5'),
    path('news-detail6/',  newsdetail6, name='newsdetail6'),
    path('news-detail7/',  newsdetail7, name='newsdetail7'),
    path('news-detail8/',  newsdetail8, name='newsdetail8'),
    path('services/', services, name='services'),
    path('services/<slug:slug>/', service_detail, name='service_detail'),


    path('blog/', blog, name='blog'),
    path('blog/<slug:slug>/', blog_detail, name='blog_detail'),
    path('get-quote/', get_quote, name='get_quote'),


    path('carmela-ai/', carmela_ai, name='carmela-ai'),
    path('chatbot/', chatbot, name='chat'),
    
    path('login/', login_view, name='login'),  # if using custom login
    path('signup/', signup_view, name='signup'),  # same
    path('logout/', logout_view, name='logout'),

    path('dashboard/', dashboard, name='dashboard'),
    path('save-journal/', save_journal, name='save_journal'),
    path('write/', writing_tool, name='writing_tool'),
    path('rewrite/', rewrite_tool, name='rewrite_tool'),



    path('api/chat/', chat_api, name='chat_api'),
    path('chatbot-response/', chatbot_response, name='chatbot_response'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
