from django.urls import path
from core.api import views

urlpatterns = [
    path("settings/", views.SiteSettingsRetrieveAPIView.as_view()),
    path("banner-list/", views.BannerListAPIView.as_view()),
    path("event-list/", views.EventListAPIView.as_view()),
    path("event-retrieve/", views.EventRetrieveAPIView.as_view()),
    path("testimonial-list/", views.TestimonialListAPIView.as_view()),
    path("blog-list/", views.BlogListAPIView.as_view()),
    path("education-list/", views.EducationListAPIView.as_view()),
    path("offer-list/", views.OfferListAPIView.as_view()),
    path("package-list/", views.PackageListAPIView.as_view()),
    path("advantage-list/", views.AdvantageListAPIView.as_view()),
    path("fag-list/", views.FagListAPIView.as_view()),
    path("smmform-create/", views.SMMFormCreateAPIView.as_view()),
    path("course-list/", views.CourseListAPIView.as_view()),
    path("course-retrieve/<int:id>/", views.CourseRetrieveAPIView.as_view()),
    path("trainingform-create/", views.TrainingFormCreateAPIView.as_view()),
    path("certificationinfo-list/", views.CertificateInfoListAPIView.as_view()),
    path('cerificate-list/', views.CerificateListAPIView.as_view()),
    path('certificate-retrieve/<int:id>/', views.CerificateRetrieveAPIView.as_view()),
    path('socialmedia-list/', views.SocialMediaListAPIView.as_view()),
    path('popup-list/', views.PopUpAPIView.as_view())
]