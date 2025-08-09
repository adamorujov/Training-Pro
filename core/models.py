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

    training_image1 = models.ImageField("Şəkil 1", upload_to="site_imgs/", blank=True, null=True)
    training_image2 = models.ImageField("Şəkil 2", upload_to="site_imgs/", blank=True, null=True)

    slogan = models.TextField("Sloqan", blank=True, null=True)

    aboutme_title = models.TextField("Başlıq", blank=True, null=True)
    aboutme_subtitle = models.TextField("Alt başlıq", blank=True, null=True)
    aboutme_content = models.TextField("Kontent", blank=True, null=True)
    aboutme_image = models.ImageField("Şəkil", upload_to="site_imgs/", blank=True, null=True)

    my_mission = models.TextField("Missiyam", blank=True, null=True)
    my_view = models.TextField("Görüşüm", blank=True, null=True)

    my_project_name = models.TextField("Başlıq", blank=True, null=True)
    my_project_content = models.TextField("Kontent", blank=True, null=True)
    my_project_image = models.ImageField("Şəkil", upload_to="site_imgs/", blank=True, null=True)

    advertising_title = models.TextField("Başlıq", blank=True, null=True)
    advertising_content = models.TextField("Kontent", blank=True, null=True)
    advertising_image = models.ImageField("Şəkil", upload_to="site_imgs/", blank=True, null=True)

    smm_title = models.TextField("Başlıq", blank=True, null=True)
    smm_content = models.TextField("Kontent", blank=True, null=True)
    smm_image1 = models.ImageField("Şəkil 1", upload_to="site_imgs/", blank=True, null=True)
    smm_image2 = models.ImageField("Şəkil 2", upload_to="site_imgs/", blank=True, null=True)
    smm_image3 = models.ImageField("Şəkil 3", upload_to="site_imgs/", blank=True, null=True)
    smm_image4 = models.ImageField("Şəkil 4", upload_to="site_imgs/", blank=True, null=True)

    smm_form_title = models.TextField("Başlıq", blank=True, null=True)
    smm_form_subtitle = models.TextField("Alt başlıq", blank=True, null=True)
    smm_form_content = models.TextField("Kontent", blank=True, null=True)

    university_title = models.TextField("Universitet başlıq", blank=True, null=True)
    university_content = models.TextField("Universitet kontent", blank=True, null=True)
    university_logo = models.ImageField("Universitet loqo", upload_to="site_imgs/", blank=True, null=True)
    university_image = models.ImageField("Universitet şəkil", upload_to="site_imgs/", blank=True, null=True)
    university_course_content = models.TextField("Universitet kurs kontent", blank=True, null=True)

    certificate_title = models.TextField("Sertifikat başlıq", blank=True, null=True)
    certificate_content = models.TextField("Sertifikat kontent", blank=True, null=True)
    certificate_image = models.ImageField("Sertifikat şəkil", upload_to="site_imgs/", blank=True, null=True)
    certificate_note = models.TextField("Sertifikat qeyd", blank=True, null=True)

    university_slogan = models.TextField("Universitet sloqan", blank=True, null=True)

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
    image = models.ImageField("Şəkil", upload_to="banner_imgs/")

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "Bannerlər"
        ordering = ("-id",)

    def __str__(self):
        return self.image.url
    
class EventCategory(models.Model):
    name = models.CharField("Ad", max_length=100)
    icon = models.TextField("İkon", blank=True, null=True)

    class Meta:
        verbose_name = "tədbir kateqoriyası"
        verbose_name_plural = "Tədbir Kateqoriyaları"
        ordering = ("-id",)

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField("Başlıq", max_length=200)
    content = models.TextField("Kontent")
    image = models.ImageField("Şəkil", upload_to="event_imgs/")
    category = models.ForeignKey(EventCategory, verbose_name="Şəkil", on_delete=models.CASCADE, related_name="events")
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
    image = models.ImageField("Şəkil", upload_to="blog_imgs/")
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
    image = models.ImageField("Şəkil", upload_to="offer_imgs/")

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
    email = models.EmailField("Email", max_length=256)
    brand = models.CharField("Brend və ya şirkət", max_length=100)
    link = models.TextField("Link")
    service = models.CharField("Xidmət", max_length=100)

    class Meta:
        verbose_name = "SMM müraciəti"
        verbose_name_plural = "SMM Müraciətləri"
        ordering = ("-id",)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField("Başlıq", max_length=250)
    content = models.TextField("Kontent")
    image = models.ImageField("Şəkil", upload_to="course_imgs/", blank=True, null=True)
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
    name = models.CharField("Ad", max_length=50)
    email = models.EmailField("Email", max_length=256)
    phone_number = models.CharField("Telefon nömrəsi", max_length=20)
    your_work = models.CharField("Məşğul olduğu iş", max_length=150)
    difficult_area = models.CharField("Çətinlik çəkdiyi sahə", max_length=150)
    important_degree = models.CharField("Sertifikatın önəmi", max_length=20)
    how_found = models.CharField("Universiteti təlimlərinə harda rast gəlib", max_length=30)

    expectation = models.TextField("Təlimdən gözləntilər")
    note = models.TextField("Əlavə qeyd", blank=True, null=True)

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
    image = models.ImageField("Şəkil", upload_to="certificate_imgs/")
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