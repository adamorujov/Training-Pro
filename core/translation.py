from modeltranslation.translator import register, TranslationOptions
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, Topic, TrainingForm, CertificateInfo, SocialMedia, Certificate, MyCertificate,
    ForeignEduBanner, ForeignEduService, ForeignEduStatistics, ForeignEduTestimonial,
    ForeignEduUniversity, ForeignEduWhyUs, ForeignEduScholarship
)


@register(SiteSettings)
class SiteSettingsTranslationOptions(TranslationOptions):
    fields = (
        'mainpage_title', 'mainpage_content', 'events_title', 'events_content', 'training_title', 'training_content',
        'training_title1', 'training_content1', 'training_title2', 'training_content2', 'slogan', 'aboutme_title', 
        'aboutme_subtitle', 'aboutme_content', 'my_mission', 'my_view', 'my_project_name', 'my_project_content', 
        'advertising_title', 'advertising_content', 'smm_title', 'smm_content', 'smm_form_title', 'smm_form_subtitle', 
        'smm_form_content', 'university_title', 'university_content', 'university_course_content', 'certificate_title', 
        'certificate_content', 'certificate_note', 'university_slogan', 'foreign_edu_title', 'foreign_edu_content', 'foreign_edu_form_title'
        )

@register(EventCategory)
class EventCategoryTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ("title", "content", "author", "text")

@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ("name", "profession", "text")

@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ("title", "content")

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ("title", "content")

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ("title", "content", "why_important")

@register(Include)
class IncludeTranslationOptions(TranslationOptions):
    fields = ("title",)

@register(Package)
class PackageTranslationOptions(TranslationOptions):
    fields = ("title", "content")

@register(Advantage)
class AdvantageTranslationOptions(TranslationOptions):
    fields = ("title",)

@register(Fag)
class FagTranslationOptions(TranslationOptions):
    fields = ("title", "content")

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ("title", "content", "language", "purpose", "trainer", "slogan", "duration")

@register(CourseAdvantage)
class CourseAdvantageTranslationOptions(TranslationOptions):
    fields = ("title",)

@register(Curriculum)
class CurriculumTranslationOptions(TranslationOptions):
    fields = ("title",)

@register(CurriculumItem)
class CurriculumItemTranslationOptions(TranslationOptions):
    fields = ("title", "duration")

@register(Topic)
class TopicTranslationOptions(TranslationOptions):
    fields = ("title",)

@register(CertificateInfo)
class CertificateInfoTranslationOptions(TranslationOptions):
    fields = ("title", "content",)

@register(Certificate)
class CertificateTranslationOptions(TranslationOptions):
    fields = ("name", "agency", "certificate_date", "country")

@register(MyCertificate)
class MyCertificateTranslationOptions(TranslationOptions):
    fields = ("name", "agency", "certificate_date", "country")

@register(ForeignEduService)
class ForeignEduServiceTranslationOptions(TranslationOptions):
    fields = ("name", "content",)

@register(ForeignEduStatistics)
class ForeignEduStatisticsTranslationOptions(TranslationOptions):
    fields = ("name",)

@register(ForeignEduWhyUs)
class ForeignEduWhyUsTranslationOptions(TranslationOptions):
    fields = ("content",)

@register(ForeignEduScholarship)
class ForeignEduScholarshipTranslationOptions(TranslationOptions):
    fields = ("country", "title")

@register(ForeignEduTestimonial)
class ForeignEduTestimonialTranslationOptions(TranslationOptions):
    fields = ("name", "profession", "text")
