from django.urls import path
from .views import *

urlpatterns = [

    path('', home_page, name='home'),
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
    path('exclusiveoffer/',exclusiveoffer, name='exclusiveoffer'),



]



