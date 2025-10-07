from rest_framework import serializers
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, Topic, TrainingForm, CertificateInfo, SocialMedia, Certificate, MyCertificate,
    ForeignEduBanner, ForeignEduService, ForeignEduStatistics, 
    ForeignEduTestimonial, ForeignEduUniversity, ForeignEduWhyUs, ForeignEduScholarship, ForeignEduForm,
    EventSubCategory, CourseCategory, ForeignEduScholarshipCurrency
)

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class EventSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSubCategory
        fields = "__all__"

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    eventsubcategories = EventSubCategorySerializer(many=True)
    class Meta:
        model = Event
        fields = "__all__"

    def get_category(self, obj):
        if obj.eventsubcategories.exists():
            category = obj.eventsubcategories.first().eventcategory
            return EventCategorySerializer(category).data
        return None

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"

class IncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Include
        fields = "__all__"

class PackageSerializer(serializers.ModelSerializer):
    includes = IncludeSerializer(many=True)
    class Meta:
        model = Package
        fields = "__all__"

class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = "__all__"

class FagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fag
        fields = "__all__"

class SMMFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMMForm
        fields = "__all__"

class CourseAdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAdvantage
        fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class CurriculumItemSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True)
    class Meta:
        model = CurriculumItem
        fields = "__all__"

class CurriculumSerializer(serializers.ModelSerializer):
    items = CurriculumItemSerializer(many=True)
    class Meta:
        model = Curriculum
        fields = "__all__"

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    advantages = CourseAdvantageSerializer(many=True)
    curriculums = CurriculumSerializer(many=True)

    class Meta:
        model = Course
        fields = "__all__"

class TrainingFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingForm
        fields = "__all__"

class CertificateInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateInfo
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"

class MyCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCertificate
        fields = "__all__"


#-------------- POPUP Serializers ---------------

class CoursePopUpSerializer(serializers.ModelSerializer):
    advantages = CourseAdvantageSerializer(many=True)
    popup_type = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_popup_type(self, obj):
        return "course"

class EventPopUpSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    popup_type = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_popup_type(self, obj):
        return "event"
    
    def get_category(self, obj):
        if obj.eventsubcategories.exists():
            category = obj.eventsubcategories.first().eventcategory
            return EventCategorySerializer(category).data
        return None
    

#------------------ New Serializers ------------------
class CategoryEventSerializer(serializers.ModelSerializer):
    events = serializers.SerializerMethodField()

    class Meta:
        model = EventCategory
        fields = ("id", "name", "events")

    def get_events(self, obj):
        events = Event.objects.filter(eventsubcategories__in=obj.subcategories.values_list("id", flat=True)).distinct()[:4]
        return EventSerializer(events, many=True, context=self.context).data
    
class ForeignEduBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduBanner
        fields = "__all__"

class ForeignEduServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduService
        fields = "__all__"

class ForeignEduStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduStatistics
        fields = "__all__"

class ForeignEduTestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduTestimonial
        fields = "__all__"

class ForeignEduUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduUniversity
        fields = "__all__"

class ForeignEduWhyUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduWhyUs
        fields = "__all__"

class ForeignEduScholarshipCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduScholarshipCurrency
        fields = "__all__"

class ForeignEduScholarshipSerializer(serializers.ModelSerializer):
    currency = ForeignEduScholarshipCurrencySerializer()
    class Meta:
        model = ForeignEduScholarship
        fields = "__all__"

class ForeignEduFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForeignEduForm
        fields = "__all__"

#-------------- Payment Serializers ------------------

from rest_framework import serializers
from core.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class PaymentInitSerializer(serializers.Serializer):
    order_id = serializers.CharField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    currency = serializers.CharField(max_length=3, default="AZN")
    description = serializers.CharField(max_length=255, required=False, allow_blank=True)

class ReversePaymentSerializer(serializers.Serializer):
    amount = serializers.CharField()
    currency = serializers.CharField(default="AZN")
    order = serializers.CharField()
    rrn = serializers.CharField()
    int_ref = serializers.CharField()

