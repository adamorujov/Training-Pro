from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, TrainingForm, CertificateInfo
)
from core.api.serializers import (
    SiteSettingsSerializer, BannerSerializer, EventCategorySerializer, EventSerializer, 
    TestimonialSerializer, BlogSerializer, EducationSerializer, OfferSerializer, PackageSerializer, 
    IncludeSerializer, AdvantageSerializer, FagSerializer, SMMFormSerializer, CourseSerializer, 
    CourseAdvantageSerializer, CurriculumSerializer, CurriculumItemSerializer, TrainingFormSerializer, 
    CertificateInfoSerializer
)

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