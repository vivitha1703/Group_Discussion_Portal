from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static
from firebase_admin import auth


urlpatterns = [
    path('', views.landing_view, name='landing-page'),
    path('login/', views.login_view, name='login'),  
    path('login_view/', views.login_view, name='login_view'),     
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_events/',views.admin_events, name='admin_events'),
    path('admin_evaluation/',views.admin_evaluation, name='admin_evaluation'),
    path('admin_group/', views.admin_group, name='admin_group'),
    path('admin_mock/', views.admin_mock, name='admin_mock'),
    path('admin_self/', views.admin_self, name='admin_self'),
    path('user_events/', views.user_events, name='user_events'),
    path('user_booking/', views.user_booking, name='user_booking'),
    path('get-students-count/', views.get_students_count, name='get_students_count'),
    path('slot-page/', views.slot_page, name='slot_page'),
    path('event-selfintro/', views.save_self_intro, name='save_self_intro'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)