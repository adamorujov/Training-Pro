from django.db import models
from tinymce.models import HTMLField

class SiteSettings(models.Model):
    logo = models.TextField("Loqo", blank=True, null=True)
    favicon = models.TextField("Favikon", blank=True, null=True)
    contact_number = models.CharField("Əlaqə nömrəsi", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)

    mainpage_title = models.TextField("Başlıq", blank=True, null=True)
    mainpage_content = models.TextField("Kontent", blank=True, null=True)

    events_title = models.TextField("Başlıq", blank=True, null=True)
    events_content = models.TextField("Kontent", blank=True, null=True)

    training_title = models.TextField("Əsas başlıq", blank=True, null=True)
    training_content = models.TextField("Əsas kontent", blank=True, null=True)

    training_title1 = models.TextField("Başlıq 1", blank=True, null=True)
    training_content1 = models.TextField("Kontent 1", blank=True, null=True)

    training_title2 = models.TextField("Başlıq 2", blank=True, null=True)
    training_content2 = models.TextField("Kontent 2", blank=True, null=True)

    training_image1_az = models.ImageField("Şəkil 1 [az]", upload_to="site_imgs/", blank=True, null=True)
    training_image1_en = models.ImageField("Şəkil 1 [en]", upload_to="site_imgs/", blank=True, null=True)
    training_image2_az = models.ImageField("Şəkil 2 [az]", upload_to="site_imgs/", blank=True, null=True)
    training_image2_en = models.ImageField("Şəkil 2 [en]", upload_to="site_imgs/", blank=True, null=True)

    slogan = models.TextField("Sloqan", blank=True, null=True)

    aboutme_title = models.TextField("Başlıq", blank=True, null=True)
    aboutme_subtitle = models.TextField("Alt başlıq", blank=True, null=True)
    aboutme_content = models.TextField("Kontent", blank=True, null=True)
    aboutme_image_az = models.ImageField("Şəkil [az]", upload_to="site_imgs/", blank=True, null=True)
    aboutme_image_en = models.ImageField("Şəkil [en]", upload_to="site_imgs/", blank=True, null=True)

    my_mission = models.TextField("Missiyam", blank=True, null=True)
    my_view = models.TextField("Görüşüm", blank=True, null=True)

    my_project_name = models.TextField("Başlıq", blank=True, null=True)
    my_project_content = models.TextField("Kontent", blank=True, null=True)
    my_project_image_az = models.ImageField("Şəkil [az]", upload_to="site_imgs/", blank=True, null=True)
    my_project_image_en = models.ImageField("Şəkil [en]", upload_to="site_imgs/", blank=True, null=True)

    advertising_title = models.TextField("Başlıq", blank=True, null=True)
    advertising_content = models.TextField("Kontent", blank=True, null=True)
    advertising_image_az = models.ImageField("Şəkil [az]", upload_to="site_imgs/", blank=True, null=True)
    advertising_image_en = models.ImageField("Şəkil [en]", upload_to="site_imgs/", blank=True, null=True)

    smm_title = models.TextField("Başlıq", blank=True, null=True)
    smm_content = models.TextField("Kontent", blank=True, null=True)
    smm_image1_az = models.ImageField("Şəkil 1 [az]", upload_to="site_imgs/", blank=True, null=True)
    smm_image1_en = models.ImageField("Şəkil 1 [en]", upload_to="site_imgs/", blank=True, null=True)
    smm_image2_az = models.ImageField("Şəkil 2 [az]", upload_to="site_imgs/", blank=True, null=True)
    smm_image2_en = models.ImageField("Şəkil 2 [en]", upload_to="site_imgs/", blank=True, null=True)
    smm_image3_az = models.ImageField("Şəkil 3 [az]", upload_to="site_imgs/", blank=True, null=True)
    smm_image3_en = models.ImageField("Şəkil 3 [en]", upload_to="site_imgs/", blank=True, null=True)
    smm_image4_az = models.ImageField("Şəkil 4 [az]", upload_to="site_imgs/", blank=True, null=True)
    smm_image4_en = models.ImageField("Şəkil 4 [en]", upload_to="site_imgs/", blank=True, null=True)

    smm_form_title = models.TextField("Başlıq", blank=True, null=True)
    smm_form_subtitle = models.TextField("Alt başlıq", blank=True, null=True)
    smm_form_content = models.TextField("Kontent", blank=True, null=True)

    university_title = models.TextField("Universitet başlıq", blank=True, null=True)
    university_content = models.TextField("Universitet kontent", blank=True, null=True)
    university_logo_az = models.ImageField("Universitet loqo [az]", upload_to="site_imgs/", blank=True, null=True)
    university_logo_en = models.ImageField("Universitet loqo [en]", upload_to="site_imgs/", blank=True, null=True)
    university_image_az = models.ImageField("Universitet şəkil [az]", upload_to="site_imgs/", blank=True, null=True)
    university_image_en = models.ImageField("Universitet şəkil [en]", upload_to="site_imgs/", blank=True, null=True)
    university_course_content = models.TextField("Universitet kurs kontent", blank=True, null=True)

    certificate_title = models.TextField("Sertifikat başlıq", blank=True, null=True)
    certificate_content = models.TextField("Sertifikat kontent", blank=True, null=True)
    certificate_image_az = models.ImageField("Sertifikat şəkil [az]", upload_to="site_imgs/", blank=True, null=True)
    certificate_image_en = models.ImageField("Sertifikat şəkil [en]", upload_to="site_imgs/", blank=True, null=True)
    certificate_note = models.TextField("Sertifikat qeyd", blank=True, null=True)

    university_slogan = models.TextField("Universitet sloqan", blank=True, null=True)

    events_image_az = models.ImageField("Cari hadisələr şəkil [az]", upload_to="site_imgs/", blank=True, null=True)
    events_image_en = models.ImageField("Cari hadisələr şəkil [en]", upload_to="site_imgs/", blank=True, null=True)

    foreign_edu_title = models.TextField("Xaricdə təhsil başlıq", blank=True, null=True)
    foreign_edu_content = models.TextField("Xaricdə təhsil kontent", blank=True, null=True)
    foreign_edu_form_title = models.TextField("Xaricdə təhsil form başlığı", blank=True, null=True)

    class Meta:
        verbose_name = "parametr"
        verbose_name_plural = "Parametrlər"

    def __str__(self):
        return "Parametrlər"
    
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            return None
        return super(SiteSettings, self).save(*args, **kwargs)
    
class Banner(models.Model):
    image_az = models.ImageField("Şəkil [az]", upload_to="banner_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="banner_imgs/")

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "Bannerlər"
        ordering = ("-id",)

    def __str__(self):
        return self.image_az.url
    
class EventCategory(models.Model):
    name = models.CharField("Ad", max_length=100)
    icon = models.TextField("İkon", blank=True, null=True)
    order_number = models.IntegerField("Sıra nömrəsi", default=0)

    class Meta:
        verbose_name = "tədbir kateqoriyası"
        verbose_name_plural = "Tədbir Kateqoriyaları"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class EventSubCategory(models.Model):
    name = models.CharField("Ad", max_length=150)
    eventcategory = models.ForeignKey(EventCategory, verbose_name="Kateqoriya", on_delete=models.CASCADE, related_name="subcategories")

    class Meta:
        verbose_name = "tədbir alt kateqoriyası"
        verbose_name_plural = "Tədbir Alt Kateqoriyaları"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.name} ({self.eventcategory.name})"

class Event(models.Model):
    title = models.CharField("Başlıq", max_length=200)
    content = models.TextField("Kontent")
    image_az = models.ImageField("Şəkil [az]", upload_to="event_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="event_imgs/")
    eventsubcategories = models.ManyToManyField(EventSubCategory, verbose_name="Kateqoriyalar", related_name="events")
    is_popup = models.BooleanField("Popup aktivdir.", default=False)
    date = models.DateField("Tarix", blank=True, null=True)
    author = models.CharField("Müəllif", max_length=200, blank=True, null=True)
    text = HTMLField("Mətn", blank=True, null=True)

    class Meta:
        verbose_name = "tədbir"
        verbose_name_plural = "Tədbirlər"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField("Ad", max_length=50)
    profession = models.CharField("Peşə", max_length=100)
    link = models.TextField("Link")
    text = models.TextField("Rəy")

    class Meta:
        verbose_name = "rəy və uğur hekayəsi"
        verbose_name_plural = "Rəy və Uğur Hekayələri"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.TextField("Başlıq")
    content = models.TextField("Kontent")
    image_az = models.ImageField("Şəkil [az]", upload_to="blog_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="blog_imgs/")
    highlighted = models.BooleanField("Önə çıxarılan", default=False)

    class Meta:
        verbose_name = "bloq"
        verbose_name_plural = "Bloqlar"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Education(models.Model):
    title = models.CharField("Başlıq", max_length=100)
    content = models.TextField("Kontent")
    icon = models.TextField("İkon")
    has_button = models.BooleanField("Buton mövcuddur.", default=False)
    pdf_file = models.FileField("PDF", blank=True, null=True)

    class Meta:
        verbose_name = "təhsil və diplom"
        verbose_name_plural = "Təhsil və Diplomlar"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Offer(models.Model):
    title = models.CharField("Başlıq", max_length=200)
    content = models.TextField("Kontent")
    why_important = models.TextField("Niyə vacib")
    icon = models.TextField("İkon")
    image_az = models.ImageField("Şəkil [az]", upload_to="offer_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="offer_imgs/")

    class Meta:
        verbose_name = "təklif"
        verbose_name_plural = "Təkliflər"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Package(models.Model):
    PAYMENT_TYPES = (
        ('a', 'aylıq'),
        ('i', 'illik')
    )
    title = models.CharField("Başlıq", max_length=50)
    icon = models.TextField("İkon")
    price = models.FloatField("Qiymət")
    discount_price = models.FloatField("Endirimli qiymət", blank=True, null=True)
    payment_type = models.CharField("Ödəniş növü", choices=PAYMENT_TYPES, max_length=1)
    content = models.TextField("Kontent")
    color = models.CharField("Rəng", max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = "paket"
        verbose_name_plural = "Paketlər"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Include(models.Model):
    package = models.ForeignKey(Package, verbose_name="Şəkil", on_delete=models.CASCADE, related_name="includes")
    title = models.CharField("Başlıq", max_length=250)
    is_included = models.BooleanField("Daxildir", default=True)

    class Meta:
        verbose_name = "daxil olan"
        verbose_name_plural = "Paketə daxil olanlar"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Advantage(models.Model):
    title = models.TextField("Başlıq")

    class Meta:
        verbose_name = "üstünlük"
        verbose_name_plural = "Üstünlüklər"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Fag(models.Model):
    CATEGORIES = (
        ('Smm', 'SMM'),
        ('Neo', 'Neo ticarət universiteti'),
        ('Xaric', 'Xaricdə təhsil')
    )
    category = models.CharField("Kateqoriya", choices=CATEGORIES, max_length=5)
    title = models.TextField("Başlıq")
    content = models.TextField("Kontent")

    class Meta:
        verbose_name = "tez-tez verilən sual"
        verbose_name_plural = "Tez-tez verilən suallar"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class SMMForm(models.Model):
    name = models.CharField("Ad, Soyad", max_length=50)
    phone_number = models.CharField("Telefon nömrəsi", max_length=20)
    email = models.EmailField("Email", max_length=256)
    brand = models.CharField("Brend və ya şirkət", max_length=100)
    # link = models.TextField("Link")
    service = models.CharField("Xidmət", max_length=100)

    class Meta:
        verbose_name = "SMM müraciəti"
        verbose_name_plural = "SMM Müraciətləri"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class CourseCategory(models.Model):
    name = models.CharField("Ad", max_length=100)

    class Meta:
        verbose_name = "kurs kateqoriyası"
        verbose_name_plural = "Kurs Kateqoriyaları"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField("Başlıq", max_length=250)
    category = models.ForeignKey(CourseCategory, verbose_name="Kateqoriya", on_delete=models.SET_NULL, related_name="courses",blank=True, null=True)
    content = models.TextField("Kontent")
    image_az = models.ImageField("Şəkil [az]", upload_to="course_imgs/", blank=True, null=True)
    image_en = models.ImageField("Şəkil [en]", upload_to="course_imgs/", blank=True, null=True)
    price = models.FloatField("Qiymət")
    discount_price = models.FloatField("Endirimli qiymət", blank=True, null=True)
    language = models.CharField("Tədris dili", max_length=10)
    purpose = models.TextField("Məqsəd")
    trainer = models.CharField("Təlimçi", max_length=50)
    slogan = models.TextField("Sloqan", blank=True, null=True)
    duration = models.CharField("Müddət", blank=True, null=True)
    is_popup = models.BooleanField("Popup aktivdir.", default=False)

    class Meta:
        verbose_name = "kurs"
        verbose_name_plural = "Kurslar"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class CourseAdvantage(models.Model):
    title = models.TextField("Başlıq")
    course = models.ForeignKey(Course, verbose_name="Kurs", on_delete=models.CASCADE, related_name="advantages")

    class Meta:
        verbose_name = "kurs üstünlüyü"
        verbose_name_plural = "Kurs Üstünlükləri"
        ordering = ("-id",)

    def __str__(self):
        return self.title + " | " + self.course.title
    
class Curriculum(models.Model):
    title = models.TextField("Başlıq")
    course = models.ForeignKey(Course, verbose_name="Kurs", on_delete=models.CASCADE, related_name="curriculums")

    class Meta:
        verbose_name = "tədris planı"
        verbose_name_plural = "Tədris planları"
        ordering = ("-id",)

    def __str__(self):
        return self.title + " | " + self.course.title
    
class CurriculumItem(models.Model):
    curriculum = models.ForeignKey(Curriculum, verbose_name="Tədris planı", on_delete=models.CASCADE, related_name="items")
    title = models.TextField("Başlıq")
    duration = models.CharField("Müddət", max_length=20)

    class Meta:
        verbose_name = "tədris mövzusu"
        verbose_name_plural = "Tədris mövzuları"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class Topic(models.Model):
    curriculum_item = models.ForeignKey(CurriculumItem, verbose_name="Əsas mövzu", on_delete=models.CASCADE, related_name="topics")
    title = models.TextField("Başlıq")

    class Meta:
        verbose_name = "alt mövzu"
        verbose_name_plural = "Alt mövzular"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class TrainingForm(models.Model):
    name = models.CharField("Ad və Soyad", max_length=50)
    email = models.EmailField("Email", max_length=256)
    phone_number = models.CharField("Telefon nömrəsi (Whatsapp aktiv)", max_length=20)
    city = models.CharField("Şəhər/Ölkə", max_length=100)
    # your_work = models.CharField("Məşğul olduğu iş", max_length=150)
    # difficult_area = models.CharField("Çətinlik çəkdiyi sahə", max_length=150)
    # important_degree = models.CharField("Sertifikatın önəmi", max_length=20)
    # how_found = models.CharField("Universiteti təlimlərinə harda rast gəlib", max_length=30)

    # expectation = models.TextField("Təlimdən gözləntilər")
    is_agree_for_foto = models.BooleanField("Şəkil və videolarda iştirakıma razıyam")
    is_agree_for_personal = models.BooleanField("Şəxsi məlumatların işlənməsi və saxlanmasına razıyam")

    # note = models.TextField("Əlavə qeyd", blank=True, null=True)

    class Meta:
        verbose_name = "təlim müraciəti"
        verbose_name_plural = "Təlim müraciətləri"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class CertificateInfo(models.Model):
    title = models.CharField("Başlıq", max_length=250)
    icon = models.TextField("İkon", blank=True, null=True)
    content = models.TextField("Kontent")

    class Meta:
        verbose_name = "sertifikat məlumatı"
        verbose_name_plural = "Sertifikat məlumatları"
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    icon = models.TextField("İkon")
    link = models.URLField("Link", max_length=256)

    class Meta:
        verbose_name = "sosial media hesabı"
        verbose_name_plural = "Sosial media hesabları"
        ordering = ("-id",)

    def __str__(self):
        return self.link

class Certificate(models.Model):
    certificate_id = models.CharField("Sertifikat ID", max_length=50)
    name = models.CharField("Ad, Soyad", max_length=50)
    image_az = models.ImageField("Şəkil [az]", upload_to="certificate_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="certificate_imgs/")
    training_date = models.DateField("Təlim tarixi", blank=True, null=True)
    agency = models.CharField("Qurum", blank=True, null=True)
    certificate_date = models.CharField("Sertifikatın verilmə tarixi", blank=True, null=True)
    country = models.CharField("Sertifikatın alındığı ölkə", blank=True, null=True)
    pdf_file = models.FileField("Serrtifikatın PDF faylı", blank=True, null=True)

    class Meta:
        verbose_name = "sertifikat"
        verbose_name_plural = "Sertifikatlar"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class MyCertificate(models.Model):
    certificate_id = models.CharField("Sertifikat ID", max_length=50)
    name = models.CharField("Ad, Soyad", max_length=50)
    image_az = models.ImageField("Şəkil [az]", upload_to="certificate_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="certificate_imgs/")
    training_date = models.DateField("Təlim tarixi", blank=True, null=True)
    agency = models.CharField("Qurum", blank=True, null=True)
    certificate_date = models.CharField("Sertifikatın verilmə tarixi", blank=True, null=True)
    country = models.CharField("Sertifikatın alındığı ölkə", blank=True, null=True)
    pdf_file = models.FileField("Serrtifikatın PDF faylı", blank=True, null=True)

    class Meta:
        verbose_name = "mənim sertifikatım"
        verbose_name_plural = "Mənim Sertifikatlarım"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class ForeignEduBanner(models.Model):
    image_az = models.ImageField("Şəkil [az]", upload_to="f_banner_imgs/")
    image_en = models.ImageField("Şəkil [en]", upload_to="f_banner_imgs/")

    class Meta:
        verbose_name = "xaricdə təhsil banner"
        verbose_name_plural = "Xaricdə Təhsil Bannerlər"
        ordering = ("-id",)

    def __str__(self):
        return self.image_az.url
    
class ForeignEduService(models.Model):
    name = models.CharField("Ad", max_length=250)
    image_az = models.ImageField("Şəkil [az]", upload_to="f_services/")
    image_en = models.ImageField("Şəkil [en]", upload_to="f_services/")
    content = models.TextField("Kontent", blank=True, null=True)

    class Meta:
        verbose_name = "xaricdə təhsil xidməti"
        verbose_name_plural = "Xaricdə Təhsil Xidmətlər"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class ForeignEduStatistics(models.Model):
    name = models.CharField("Ad", max_length=250)
    value = models.IntegerField("Nəticə")

    class Meta:
        verbose_name = "xaricdə təhsil statistikası"
        verbose_name_plural = "Xaricdə Təhsil Statistikalar"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class ForeignEduWhyUs(models.Model):
    icon = models.TextField("İkon")
    content = models.TextField("Kontent")

    class Meta:
        verbose_name = "xaricdə təhsil - niyə biz"
        verbose_name_plural = "Xaricdə Təhsil - Niyə biz?"
        ordering = ("-id",)

    def __str__(self):
        return self.content
    
class ForeignEduUniversity(models.Model):
    logo_az = models.ImageField("Loqo [az]", upload_to="f_logos/")
    logo_en = models.ImageField("Loqo [en]", upload_to="f_logos/")
    link = models.TextField("Link")

    class Meta:
        verbose_name = "xaricdə təhsil tərəfdaş universitet"
        verbose_name_plural = "Xaricdə Təhsil Tərəfdaş Universitetlər"
        ordering = ("-id",)

    def __str__(self):
        return self.link
    
class ForeignEduScholarshipCurrency(models.Model):
    name = models.CharField("Ad", max_length=20)

    class Meta:
        verbose_name = "valyuta"
        verbose_name_plural = "Təqaüd Haqqı Valyutaları"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class ForeignEduScholarship(models.Model):
    country = models.CharField("Ölkə", max_length=100)
    icon = models.TextField("Bayraq ikonu")
    title = models.CharField("Başlıq", max_length=250)
    edu_fee = models.FloatField("Təhsil haqqı (İllik minimumdan başlayan)")
    living_fee = models.FloatField("Yaşam xərci (Aylıq minimumdan başlayan)")
    currency = models.ForeignKey(ForeignEduScholarshipCurrency, verbose_name="Valyuta", on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = "dünyada təhsil"
        verbose_name_plural = "Dünyada Təhsil"
        ordering = ("-id",)

    def __str__(self):
        return self.title

class ForeignEduTestimonial(models.Model):
    name = models.CharField("Ad", max_length=50)
    image_az = models.ImageField("Şəkil [az]", upload_to="f_testimonials/", blank=True, null=True)
    image_en = models.ImageField("Şəkil [en]", upload_to="f_testimonials/", blank=True, null=True)
    profession = models.CharField("Peşə", max_length=100)
    link = models.TextField("Link", blank=True, null=True)
    text = models.TextField("Rəy")

    class Meta:
        verbose_name = "xaricdə təhsil rəy və uğur hekayəsi"
        verbose_name_plural = "Xaricdə Təhsil Rəy və Uğur Hekayələri"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class ForeignEduForm(models.Model):
    name = models.CharField("Ad, soyad", max_length=100)
    email = models.EmailField("Email", max_length=256)
    phone_number = models.CharField("Telefon nömrəsi", max_length=20)
    interest = models.TextField("Təhsil maraq sahəsi")

    class Meta:
        verbose_name = "xaricdə təhsil müraciət"
        verbose_name_plural = "Xaricdə Təhsil Müraciətlər"
        ordering = ("-id",)

    def __str__(self):
        return self.name


#-------------- Payment Models ------------------

from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("success", "Success"),
        ("failed", "Failed"),
    ]

    order_id = models.CharField(max_length=64, unique=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default="AZN")
    description = models.CharField(max_length=255, blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    approval_code = models.CharField(max_length=16, blank=True, null=True)
    rrn = models.CharField(max_length=32, blank=True, null=True)
    int_ref = models.CharField(max_length=32, blank=True, null=True)
    card_number = models.CharField(max_length=32, blank=True, null=True)
    token = models.CharField(max_length=64, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.amount} {self.currency}"


