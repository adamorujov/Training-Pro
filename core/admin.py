from django.contrib import admin
from django.contrib.auth.models import Group, User
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, Topic, TrainingForm, CertificateInfo, SocialMedia, Certificate, MyCertificate
)
import nested_admin

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("ƏSAS PARAMETRLƏR", {"fields": ("logo", "favicon", "contact_number", "email", "slogan")}),
        ("ƏSAS SƏHİFƏ BAŞLIQ HİSSƏ", {"fields": ("mainpage_title", "mainpage_content")}),
        ("HADİSƏLƏR", {"fields": ("events_title", "events_content")}),
        ("TƏLİMLƏR", {"fields": ("training_title", "training_content", "training_title1", "training_content1", "training_title2", "training_content2", "training_image1", "training_image2")}),
        ("HAQQIMDA", {"fields": ("aboutme_title", "aboutme_subtitle", "aboutme_content", "aboutme_image", "my_mission", "my_view")}),
        ("LAYİHƏ", {"fields": ("my_project_name", "my_project_content", "my_project_image")}),
        ("REKLAM", {"fields": ("advertising_title", "advertising_content", "advertising_image")}),
        ("SMM", {"fields": ("smm_title", "smm_content", "smm_image1", "smm_image2", "smm_image3", "smm_image4")}),
        ("SMM FORMU", {"fields": ("smm_form_title", "smm_form_subtitle", "smm_form_content")}),
        ("UNİVERSİTET", {"fields": ("university_title", "university_content", "university_logo", "university_image", "university_course_content", "university_slogan")}),
        ("SERTİFİKAT", {"fields": ("certificate_title", "certificate_content", "certificate_image", "certificate_note")}),
    )
admin.site.register(Banner)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Offer)

class IncludeAdmin(admin.TabularInline):
    model = Include
    extra = 1

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    inlines = (IncludeAdmin,)

admin.site.register(Advantage)
admin.site.register(Fag)
admin.site.register(SMMForm)

class CourseAdvantageAdmin(admin.TabularInline):
    model = CourseAdvantage
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = (CourseAdvantageAdmin,)

class TopicInline(nested_admin.NestedTabularInline):
    model = Topic
    extra = 0

class CurriculumItemInline(nested_admin.NestedTabularInline):
    model = CurriculumItem
    extra = 0
    inlines = (TopicInline,)

@admin.register(Curriculum)
class CurriculumAdmin(nested_admin.NestedModelAdmin):
    inlines = (CurriculumItemInline,)

admin.site.register(TrainingForm)
admin.site.register(CertificateInfo)
admin.site.register(SocialMedia)
admin.site.register(Certificate)
admin.site.register(MyCertificate)
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_title = "Safar Najafov Administrasiya"
admin.site.site_header = "Safar Najafov Administrasiya"
admin.site.site_url = "www.safarnajafov.com/"