from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, TrainingForm, CertificateInfo, Certificate, SocialMedia
)
from core.api.serializers import (
    SiteSettingsSerializer, BannerSerializer, EventCategorySerializer, EventSerializer, 
    TestimonialSerializer, BlogSerializer, EducationSerializer, OfferSerializer, PackageSerializer, 
    IncludeSerializer, AdvantageSerializer, FagSerializer, SMMFormSerializer, CourseSerializer, 
    CourseAdvantageSerializer, CurriculumSerializer, CurriculumItemSerializer, TrainingFormSerializer, 
    CertificateInfoSerializer, CertificateSerializer, SocialMediaSerializer,
    CoursePopUpSerializer, EventPopUpSerializer
)
from rest_framework.response import Response
from rest_framework import status

class SiteSettingsRetrieveAPIView(RetrieveAPIView):
    def get_object(self):
        return SiteSettings.objects.first()
    serializer_class = SiteSettingsSerializer

class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class EventListAPIView(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveAPIView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    lookup_field = "id"

class TestimonialListAPIView(ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class EducationListAPIView(ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class OfferListAPIView(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

class PackageListAPIView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class AdvantageListAPIView(ListAPIView):
    queryset = Advantage.objects.all()
    serializer_class = AdvantageSerializer

class FagListAPIView(ListAPIView):
    queryset = Fag.objects.all()
    serializer_class = FagSerializer

class SMMFormCreateAPIView(CreateAPIView):
    queryset = SMMForm.objects.all()
    serializer_class = SMMFormSerializer

class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveAPIView(RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = "id"

class TrainingFormCreateAPIView(CreateAPIView):
    queryset = TrainingForm.objects.all()
    serializer_class = TrainingFormSerializer

class CertificateInfoListAPIView(ListAPIView):
    queryset = CertificateInfo.objects.all()
    serializer_class = CertificateInfoSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class CerificateListAPIView(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CerificateRetrieveAPIView(RetrieveAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    lookup_field = "id"

class PopUpAPIView(APIView):
    def get(self, request):
        courses = Course.objects.filter(is_popup=True)
        events = Event.objects.filter(is_popup=True)

        courses_data = CoursePopUpSerializer(courses, many=True, context={'request': request}).data
        events_data = EventPopUpSerializer(events, many=True, context={'request': request}).data

        popup_data = courses_data + events_data

        return Response(popup_data, status=status.HTTP_200_OK)