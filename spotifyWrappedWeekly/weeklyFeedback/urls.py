from django.urls import path

from . import views


urlpatterns = [
    path('', views.landingPageView.as_view(),name='landing'),
    path('weeklyFeedback/', views.weeklyFeedbackView.as_view(), name='feedback_page'),
    path('userSummary/', views.userSummaryView.as_view(), name='user_summary'),
    path('weekSummary/', views.weeklySummaryView.as_view(), name='weekly_summary'),
    path('adminDashboard/', views.adminDashboardView.as_view(), name='admin_dashboard'),
    
]