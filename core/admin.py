from django.contrib import admin
from django.contrib.auth.models import Group
from core.models import (
    SiteSettings, Banner, EventCategory, Event, Testimonial, Blog, Education,
    Offer, Package, Include, Advantage, Fag, SMMForm, Course, CourseAdvantage,
    Curriculum, CurriculumItem, TrainingForm, CertificateInfo, SocialMedia, Certificate
)

admin.site.register(SiteSettings)
admin.site.register(Banner)
admin.site.register(EventCategory)
admin.site.register(Event)
admin.site.register(Testimonial)
admin.site.register(Blog)
admin.site.register(Education)
admin.site.register(Offer)
admin.site.register(Package)
admin.site.register(Include)
admin.site.register(Advantage)
admin.site.register(Fag)
admin.site.register(SMMForm)
admin.site.register(Course)
admin.site.register(CourseAdvantage)
admin.site.register(Curriculum)
admin.site.register(CurriculumItem)
admin.site.register(TrainingForm)
admin.site.register(CertificateInfo)
admin.site.register(SocialMedia)
admin.site.register(Certificate)
admin.site.unregister(Group)