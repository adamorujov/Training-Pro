from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, TrainingForm, CertificateInfo, Certificate, SocialMedia, MyCertificate,
    ForeignEduBanner, ForeignEduService, ForeignEduStatistics, 
    ForeignEduTestimonial, ForeignEduUniversity, ForeignEduWhyUs, ForeignEduScholarship, ForeignEduForm,
    EventSubCategory, Order, Payment
)
from core.api.serializers import (
    SiteSettingsSerializer, BannerSerializer, EventCategorySerializer, EventSerializer, 
    TestimonialSerializer, BlogSerializer, EducationSerializer, OfferSerializer, PackageSerializer, 
    IncludeSerializer, AdvantageSerializer, FagSerializer, SMMFormSerializer, CourseSerializer, 
    CourseAdvantageSerializer, CurriculumSerializer, CurriculumItemSerializer, TrainingFormSerializer, 
    CertificateInfoSerializer, CertificateSerializer, SocialMediaSerializer,
    CoursePopUpSerializer, EventPopUpSerializer, MyCertificateSerializer, CategoryEventSerializer,
    ForeignEduBannerSerializer, ForeignEduServiceSerializer, ForeignEduStatisticsSerializer, 
    ForeignEduTestimonialSerializer, ForeignEduUniversitySerializer, ForeignEduWhyUsSerializer, 
    ForeignEduScholarshipSerializer, ForeignEduFormSerializer, EventSubCategorySerializer
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

class MyCerificateListAPIView(ListAPIView):
    queryset = MyCertificate.objects.all()
    serializer_class = MyCertificateSerializer

class MyCerificateRetrieveAPIView(RetrieveAPIView):
    queryset = MyCertificate.objects.all()
    serializer_class = MyCertificateSerializer
    lookup_field = "id"

class PopUpAPIView(APIView):
    def get(self, request):
        courses = Course.objects.filter(is_popup=True)
        events = Event.objects.filter(is_popup=True)

        courses_data = CoursePopUpSerializer(courses, many=True, context={'request': request}).data
        events_data = EventPopUpSerializer(events, many=True, context={'request': request}).data

        popup_data = courses_data + events_data

        return Response(popup_data, status=status.HTTP_200_OK)
    

#-------------------- New APIs -----------------------
class ShortCategoryEventListAPIView(ListAPIView):
    serializer_class = CategoryEventSerializer

    def get_queryset(self):
        return EventCategory.objects.order_by("order_number").all()
    
class CategoryEventListAPIView(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("id")
        return Event.objects.filter(eventsubcategories__eventcategory__id=category_id).distinct()
    
class SubCategoryListAPIView(ListAPIView):
    serializer_class = EventSubCategorySerializer
    
    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return EventSubCategory.objects.filter(eventcategory__id=category_id)
    
class ForeignEduBannerListAPIView(ListAPIView):
    queryset = ForeignEduBanner.objects.all()
    serializer_class = ForeignEduBannerSerializer

class ForeignEduServiceListAPIView(ListAPIView):
    queryset = ForeignEduService.objects.all()
    serializer_class = ForeignEduServiceSerializer

class ForeignEduStatisticsListAPIView(ListAPIView):
    queryset = ForeignEduStatistics.objects.all()
    serializer_class = ForeignEduStatisticsSerializer

class ForeignEduTestimonialListAPIView(ListAPIView):
    queryset = ForeignEduTestimonial.objects.all()
    serializer_class = ForeignEduTestimonialSerializer

class ForeignEduUniversityListAPIView(ListAPIView):
    queryset = ForeignEduUniversity.objects.all()
    serializer_class = ForeignEduUniversitySerializer

class ForeignEduWhyUsListAPIView(ListAPIView):
    queryset = ForeignEduWhyUs.objects.all()
    serializer_class = ForeignEduWhyUsSerializer

class ForeignEduScholarshipListAPIView(ListAPIView):
    queryset = ForeignEduScholarship.objects.all()
    serializer_class = ForeignEduScholarshipSerializer

class ForeignEduFormCreateAPIView(CreateAPIView):
    queryset = ForeignEduForm.objects.all()
    serializer_class = ForeignEduFormSerializer


#---------------- PAYMENT APIS -----------------

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .utils import generate_psign, verify_psign, generate_nonce, get_timestamp

MERCHANT_ID = "test_merchant_id"
TERMINAL_ID = "test_terminal_id"
PRIVATE_KEY = "private.pem"
PUBLIC_KEY = "public.pem"

# --- hansı fieldlər imzalanır (sənin dokumentasiya əsasında dəqiq siyahını yazmalısan) ---
SIGN_FIELDS = [
    "AMOUNT",
    "CURRENCY",
    "TERMINAL",
    "TRTYPE",
    "ORDER",
    "MERCH_NAME",
    "MERCH_URL",
    "MERCHANT",
    "EMAIL",
    "TIMESTAMP",
    "NONCE",
    "BACKREF",
]


class PaymentStartView(APIView):
    def post(self, request):
        amount = request.data.get("amount")
        order_id = request.data.get("order_id")

        data = {
            "AMOUNT": amount,
            "CURRENCY": "944",  # 944 = AZN
            "TERMINAL": TERMINAL_ID,
            "TRTYPE": "1",  # Authorization
            "ORDER": order_id,
            "MERCH_NAME": "Your Shop",
            "MERCH_URL": "https://admin.safarnajafov.com",
            "MERCHANT": MERCHANT_ID,
            "EMAIL": "support@safarnajafov.com",
            "TIMESTAMP": get_timestamp(),
            "NONCE": generate_nonce(),
            "BACKREF": "https://admin.safarnajafov.com/api/core/payment/callback/",
        }

        data["P_SIGN"] = generate_psign(PRIVATE_KEY, SIGN_FIELDS, data)

        return Response(data)

SIGN_FIELDS_CALLBACK = [
    "ORDER",
    "AMOUNT",
    "CURRENCY",
    "TERMINAL",
    "TRTYPE",
    "RESULT",
    "RC",
    "RCTEXT",
    "AUTHCODE",
    "RRN",
    "INT_REF",
    "TIMESTAMP",
    "NONCE",
]

class PaymentCallbackView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = request.data.copy()

        # Imza yoxlaması
        is_valid = verify_psign(PUBLIC_KEY, SIGN_FIELDS_CALLBACK, data.copy())
        if not is_valid:
            return Response({"error": "Invalid signature"}, status=status.HTTP_400_BAD_REQUEST)

        order_id = data.get("ORDER")
        result = data.get("RESULT")
        rc = data.get("RC")

        # DB-də order varsa update et, yoxsa sadəcə logla
        try:
            order = Order.objects.get(order_id=order_id)
        except Order.DoesNotExist:
            order = None

        # Payment obyektini tap və ya yarat (order yoxdursa yalnız raw saxla)
        payment, created = Payment.objects.get_or_create(
            order=order,
            defaults={
                "amount": order.total_amount if order else None,
                "currency": order.currency if order else None,
                "status": "PENDING",
                "raw_response": data
            }
        )

        # Həmişə raw məlumatı saxla
        payment.raw_response = data

        # Statusu yenilə yalnız order varsa
        if order:
            if result == "OK" and rc == "00":
                payment.status = "PAID"
                order.status = "PAID"
            else:
                payment.status = "FAILED"
                order.status = "FAILED"
            order.save()
        else:
            # Test callback üçün status "UNKNOWN"
            payment.status = "UNKNOWN"

        payment.save()

        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class PaymentCaptureView(APIView):
    def post(self, request):
        """
        Pre-Authorization edilmiş ödənişi təsdiqləmək (TRTYPE=21)
        """
        order_id = request.data.get("order_id")
        rrn = request.data.get("rrn")
        int_ref = request.data.get("int_ref")

        data = {
            "ORDER": order_id,
            "RRN": rrn,
            "INT_REF": int_ref,
            "TERMINAL": TERMINAL_ID,
            "TIMESTAMP": get_timestamp(),
            "NONCE": generate_nonce(),
            "TRTYPE": "21",
        }

        data["P_SIGN"] = generate_psign(PRIVATE_KEY, SIGN_FIELDS, data)
        return Response(data)


class PaymentRefundView(APIView):
    def post(self, request):
        """
        Ödənişi geri qaytarmaq (TRTYPE=22 və ya 24)
        """
        order_id = request.data.get("order_id")
        rrn = request.data.get("rrn")
        int_ref = request.data.get("int_ref")

        data = {
            "ORDER": order_id,
            "RRN": rrn,
            "INT_REF": int_ref,
            "TERMINAL": TERMINAL_ID,
            "TIMESTAMP": get_timestamp(),
            "NONCE": generate_nonce(),
            "TRTYPE": "22",  # 24 də ola bilər
        }

        data["P_SIGN"] = generate_psign(PRIVATE_KEY, SIGN_FIELDS, data)
        return Response(data)
