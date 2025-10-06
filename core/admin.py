from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, Topic, TrainingForm, CertificateInfo, SocialMedia,
    Certificate, MyCertificate, ForeignEduBanner, ForeignEduService, ForeignEduStatistics, 
    ForeignEduTestimonial, ForeignEduUniversity, ForeignEduWhyUs, ForeignEduScholarship, EventSubCategory,
    Order, CourseCategory, ForeignEduScholarshipCurrency, ForeignEduForm
)
import nested_admin
from modeltranslation.admin import TranslationAdmin

@admin.register(SiteSettings)
class SiteSettingsAdmin(TranslationAdmin):
    fieldsets = (
        ("ƏSAS PARAMETRLƏR", {"fields": ("logo", "favicon", "contact_number", "email", "slogan")}),
        ("ƏSAS SƏHİFƏ BAŞLIQ HİSSƏ", {"fields": ("mainpage_title", "mainpage_content")}),
        ("HADİSƏLƏR", {"fields": ("events_title", "events_content")}),
        ("TƏLİMLƏR", {"fields": ("training_title", "training_content", "training_title1", "training_content1", "training_title2", "training_content2", "training_image1_az", "training_image1_en", "training_image2_az", "training_image2_en",)}),
        ("HAQQIMDA", {"fields": ("aboutme_title", "aboutme_subtitle", "aboutme_content", "aboutme_image_az", "aboutme_image_en", "my_mission", "my_view")}),
        ("LAYİHƏ", {"fields": ("my_project_name", "my_project_content", "my_project_image_az", "my_project_image_en")}),
        ("REKLAM", {"fields": ("advertising_title", "advertising_content", "advertising_image_az", "advertising_image_en")}),
        ("SMM", {"fields": ("smm_title", "smm_content", "smm_image1_az", "smm_image1_en", "smm_image2_az", "smm_image2_en", "smm_image3_az", "smm_image3_en", "smm_image4_az", "smm_image4_en")}),
        ("SMM FORMU", {"fields": ("smm_form_title", "smm_form_subtitle", "smm_form_content")}),
        ("UNİVERSİTET", {"fields": ("university_title", "university_content", "university_logo_az", "university_logo_en", "university_image_az", "university_image_en", "university_course_content", "university_slogan")}),
        ("SERTİFİKAT", {"fields": ("certificate_title", "certificate_content", "certificate_image_az", "certificate_image_en", "certificate_note")}),
        ("CARİ HADİSƏLƏR", {"fields": ("events_image_az", "events_image_en")}),
        ("XARİCDƏ TƏHSİL", {"fields": ("foreign_edu_title", "foreign_edu_content", "foreign_edu_form_title")}),
    )
admin.site.register(Banner)

class EventSubCategoryInline(admin.TabularInline):
    model = EventSubCategory
    extra = 1
    exclude = ("name",)

@admin.register(EventCategory)
class EventCategoryAdmin(TranslationAdmin):
    inlines = [EventSubCategoryInline]

@admin.register(Event)
class EventAdmin(TranslationAdmin):
    pass

@admin.register(Testimonial)
class TestimonialAdmin(TranslationAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(TranslationAdmin):
    pass

@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    pass

@admin.register(Offer)
class OfferAdmin(TranslationAdmin):
    pass

class IncludeAdmin(admin.TabularInline):
    model = Include
    extra = 1
    exclude = ("title",)

@admin.register(Package)
class PackageAdmin(TranslationAdmin):
    inlines = (IncludeAdmin,)

@admin.register(Advantage)
class AdvantageAdmin(TranslationAdmin):
    pass

@admin.register(Fag)
class FagAdmin(TranslationAdmin):
    pass

admin.site.register(SMMForm)

class CourseAdvantageAdmin(admin.TabularInline):
    model = CourseAdvantage
    extra = 1
    exclude = ("title",)

@admin.register(CourseCategory)
class CourseCategoryAdmin(TranslationAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = (CourseAdvantageAdmin,)

class TopicInline(nested_admin.NestedTabularInline):
    model = Topic
    extra = 0
    exclude = ("title",)


    # fieldsets = (
    #     (None, {
    #         "fields": ("title_az", "title_en"),
    #         "classes": ("compact",),  # öz css class
    #     }),
    # )

class CurriculumItemInline(nested_admin.NestedTabularInline):
    model = CurriculumItem
    extra = 0
    inlines = (TopicInline,)
    exclude = ("title", "duration")

@admin.register(Curriculum)
class CurriculumAdmin(nested_admin.NestedModelAdmin):
    inlines = (CurriculumItemInline,)
    exclude = ("title",)

@admin.register(TrainingForm)
class TraningAdmin(admin.ModelAdmin):
    fieldsets = (
        ("ŞƏXSİ MƏLUMATLAR", {"fields": ("name", "email", "phone_number", "city")}),
        ("İCAZƏLƏR VƏ RAZILIQ", {"fields": ("is_agree_for_foto", "is_agree_for_personal")})
    )
    list_display = ("__str__", "email", "phone_number", "city", "is_agree_for_foto", "is_agree_for_personal")

@admin.register(CertificateInfo)
class CertificateInfoAdmin(TranslationAdmin):
    pass

admin.site.register(SocialMedia)

@admin.register(Certificate)
class CertificateAdmin(TranslationAdmin):
    pass

@admin.register(MyCertificate)
class MyCertificateAdmin(TranslationAdmin):
    pass

admin.site.register(ForeignEduBanner)

@admin.register(ForeignEduService)
class ForeignEduServiceAdmin(TranslationAdmin):
    pass

@admin.register(ForeignEduStatistics)
class ForeignEduStatisticsAdmin(TranslationAdmin):
    pass

@admin.register(ForeignEduWhyUs)
class ForeignEduWhyUsAdmin(TranslationAdmin):
    pass

@admin.register(ForeignEduScholarshipCurrency)
class ForeignEduScholarshipCurrencyAdmin(TranslationAdmin):
    pass

@admin.register(ForeignEduScholarship)
class ForeignEduScholarshipAdmin(TranslationAdmin):
    pass

@admin.register(ForeignEduTestimonial)
class ForeignEduTestimonialAdmin(TranslationAdmin):
    pass

admin.site.register(ForeignEduUniversity)
admin.site.register(ForeignEduForm)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", "amount", "status")
    readonly_fields = ("order_id", "amount", "currency", "description", "status", "approval_code", "rrn", "int_ref", "card_number", "token")


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_title = "Safar Najafov Administrasiya"
admin.site.site_header = "Safar Najafov Administrasiya"
admin.site.site_url = "www.safarnajafov.com/"