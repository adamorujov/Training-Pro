from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, TrainingForm, CertificateInfo, Certificate, SocialMedia, MyCertificate,
    ForeignEduBanner, ForeignEduService, ForeignEduStatistics, 
    ForeignEduTestimonial, ForeignEduUniversity, ForeignEduWhyUs, ForeignEduScholarship, ForeignEduForm,
    EventSubCategory, Order
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

# payments/views.py
import os
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.shortcuts import get_object_or_404

from core.models import Order
from .serializers import PaymentInitSerializer, OrderSerializer
from .utils import (
    build_request_sign_body,
    build_callback_sign_body,
    sign_with_private_key_hex,
    verify_with_public_key_hex,
    generate_nonce,
)

# ENV / settings expected:
# settings.MERCHANT_PRIVATE_KEY_PATH
# settings.MPI_PUBLIC_KEY_PATH
# settings.TERMINAL_ID
# settings.MERCHANT_URL
# settings.MERCHANT_NAME
# settings.MERCHANT_EMAIL
# settings.SUCCESS_URL  (MERCH_URL / BACKREF)
# settings.AZERICARD_TEST_URL

TERMINAL_ID = getattr(settings, "TERMINAL_ID", None)
MERCHANT_URL = getattr(settings, "MERCHANT_URL", "")
MERCHANT_NAME = getattr(settings, "MERCHANT_NAME", "")
MERCHANT_EMAIL = getattr(settings, "MERCHANT_EMAIL", "")
MERCHANT_PRIVATE_KEY_PATH = getattr(settings, "MERCHANT_PRIVATE_KEY_PATH", None)
MPI_PUBLIC_KEY_PATH = getattr(settings, "MPI_PUBLIC_KEY_PATH", None)
AZERICARD_TEST_URL = getattr(settings, "AZERICARD_TEST_URL", "https://testmpi.3dsecure.az/cgi-bin/cgi_link")


class InitPaymentAPIView(APIView):
    """
    Build payload for gateway POST (request signing logic exactly as Java).
    """

    def post(self, request):
        serializer = PaymentInitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data["amount"]
        desc = serializer.validated_data.get("description", "")
        customer_name = serializer.validated_data.get("customer_name", "Unknown")
        # Create order record
        # Use your existing Order model; ensure order_id is a string
        order = Order.objects.create(
            order_id=str(serializer.validated_data.get("order_id", None) or Order.objects.count() + 1),
            amount=amount,
            currency="AZN",
            description=desc,
            status="pending",
            # terminal stored if you want
        )

        # Prepare fields exactly like Java:
        timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
        nonce = generate_nonce(16)
        trtype = "1"  # auth

        # Java used amount as String; ensure it's formatted like "10.0" or "0.01" - convert to string
        amount_str = str(amount)

        sign_body = build_request_sign_body(
            amount=amount_str,
            currency="AZN",
            terminal=TERMINAL_ID,
            trtype=trtype,
            timestamp=timestamp,
            nonce=nonce,
            merch_url=MERCHANT_URL,
        )
        # Generate p_sign using merchant private key
        if not MERCHANT_PRIVATE_KEY_PATH:
            return Response({"detail": "Server misconfigured: merchant private key path is missing"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        p_sign = sign_with_private_key_hex(sign_body, MERCHANT_PRIVATE_KEY_PATH)

        payload = {
            "TERMINAL": TERMINAL_ID,
            "ORDER": order.order_id,
            "AMOUNT": amount_str,
            "CURRENCY": "AZN",
            "DESC": desc,
            "MERCH_ID": "TEST",
            "MERCH_NAME": MERCHANT_NAME,
            "MERCH_URL": MERCHANT_URL,
            "EMAIL": MERCHANT_EMAIL,
            "COUNTRY": "AZ",
            "MERCH_GMT": "+4",
            "BACKREF": "https://admin.safarnajafov.com/payment/callback/",
            "TRTYPE": trtype,
            "TIMESTAMP": timestamp,
            "NONCE": nonce,
            "NAME": customer_name,
            "M_INFO": serializer.validated_data.get("extra_info", "Test"),
            "P_SIGN": p_sign,
        }

        return Response({"gateway_url": AZERICARD_TEST_URL, "payload": payload})


class CallbackAPIView(APIView):
    """
    Verify callback P_SIGN from MPI / gateway and update Order.
    Java verify used fields: AMOUNT, TERMINAL, APPROVAL, RRN, INT_REF
    where missing field -> "-" literal. We'll replicate that.
    """
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        data = request.POST.dict() if hasattr(request.POST, "dict") else dict(request.data)
        order_id = data.get("ORDER")
        if not order_id:
            return Response({"detail": "ORDER missing"}, status=status.HTTP_400_BAD_REQUEST)

        order = get_object_or_404(Order, order_id=str(order_id))

        amount = data.get("AMOUNT")
        terminal = data.get("TERMINAL")
        approval = data.get("APPROVAL")
        rrn = data.get("RRN")
        int_ref = data.get("INT_REF")
        p_sign = data.get("P_SIGN", "")

        sign_body = build_callback_sign_body(amount, terminal, approval, rrn, int_ref)

        if not MPI_PUBLIC_KEY_PATH:
            return Response({"detail": "Server misconfigured: MPI public key not provided"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        valid = verify_with_public_key_hex(sign_body, p_sign, MPI_PUBLIC_KEY_PATH)

        if not valid:
            order.status = "failed"
            order.save()
            return Response({"detail": "invalid signature"}, status=status.HTTP_400_BAD_REQUEST)

        # signature valid -> check action / RC to set status
        action = data.get("ACTION")
        rc = data.get("RC")
        if action == "0" or rc in ("00", "0"):
            order.status = "success"
            order.approval_code = approval
            order.rrn = rrn
            order.int_ref = int_ref
            order.card_number = data.get("CARD")
            order.save()
            return Response({"detail": "ok"})
        else:
            order.status = "failed"
            order.save()
            return Response({"detail": "payment failed", "action": action, "rc": rc}, status=status.HTTP_400_BAD_REQUEST)
