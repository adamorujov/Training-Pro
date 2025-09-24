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

import uuid
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from core.models import Order
from .serializers import PaymentInitSerializer, OrderSerializer
from .utils import md5_sign
from .utils import load_public_key, rsa_verify

# AZERICARD_URL = os.getenv("AZERICARD_TEST_URL", "https://testmpi.3dsecure.az/cgi-bin/cgi_link")
# TERMINAL_ID = os.getenv("TERMINAL_ID")
# MERCHANT_ID = os.getenv("MERCHANT_ID", "YOUR_MERCHANT_ID")
# MD5_SECRET = os.getenv("PAYOUT_MD5_KEY")
# MPI_PUBLIC_KEY_PATH = os.getenv("MPI_PUBLIC_KEY_PATH")

# Azericard test integration
TERMINAL_ID="17205084"
MERCHANT_ID="TEST"
AZERICARD_TEST_URL="https://testmpi.3dsecure.az/cgi-bin/cgi_link"

# Secret for md5 signature (will be provided by bank)
PAYOUT_MD5_KEY="098f6bcd4621d373cade4e832627b4f6"

# Path to keys
MERCHANT_PRIVATE_KEY_PATH="private.pem"
MPI_PUBLIC_KEY_PATH="mpi_public.pem"


class InitPaymentAPIView(APIView):
    """
    Create order and send payment init request
    """

    def post(self, request):
        serializer = PaymentInitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order_id = str(uuid.uuid4().hex[:12])
        amount = serializer.validated_data["amount"]
        currency = serializer.validated_data["currency"]

        order = Order.objects.create(
            order_id=order_id,
            amount=amount,
            currency=currency,
            description=serializer.validated_data.get("description", "")
        )

        # MD5 signature for request
        data_to_sign = f"{TERMINAL_ID}{order_id}{amount}{currency}"
        sign = md5_sign(data_to_sign, PAYOUT_MD5_KEY)

        payload = {
            "TERMINAL": TERMINAL_ID,
            "ORDER": order_id,
            "AMOUNT": str(amount),
            "CURRENCY": currency,
            "DESC": order.description,
            "MERCH_ID": MERCHANT_ID,
            "P_SIGN": sign,
            "TRTYPE": "1",  # 1 - Auth, 0 - PreAuth
        }

        return Response({
            "order": OrderSerializer(order).data,
            "gateway_url": AZERICARD_TEST_URL,
            "payload": payload
        })


class PaymentCallbackAPIView(APIView):
    """
    Handle Azericard callback (P_SIGN verification)
    """

    def post(self, request):
        data = request.POST.dict() or request.data
        order_id = data.get("ORDER")
        order = get_object_or_404(Order, order_id=order_id)

        # Build string for P_SIGN verification
        fields = ["AMOUNT", "TERMINAL", "APPROVAL", "RRN", "INT_REF"]
        data_to_verify = "".join([data.get(f, "-") for f in fields])

        mpi_pub = load_public_key(MPI_PUBLIC_KEY_PATH)
        signature = data.get("P_SIGN")

        verified = rsa_verify(mpi_pub, data_to_verify, signature)

        if verified and data.get("RC") == "00":
            order.status = "success"
            order.approval_code = data.get("APPROVAL")
            order.rrn = data.get("RRN")
            order.int_ref = data.get("INT_REF")
            order.card_number = data.get("CARD")
            order.token = data.get("TOKEN")
            order.save()
            return Response({"status": "ok"}, status=status.HTTP_200_OK)

        order.status = "failed"
        order.save()
        return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)
