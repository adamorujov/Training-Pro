from rest_framework import serializers
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, Topic, TrainingForm, CertificateInfo, SocialMedia, Certificate
)

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer()
    class Meta:
        model = Event
        fields = "__all__"

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
    category = EventCategorySerializer()
    popup_type = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_popup_type(self, obj):
        return "event"