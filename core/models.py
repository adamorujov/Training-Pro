from django.db import models

class SiteSettings(models.Model):
    logo = models.TextField("Loqo", blank=True, null=True)
    favicon = models.TextField("Favikon", blank=True, null=True)
    contact_number = models.CharField("Loqo", max_length=20, blank=True, null=True)
    email = models.EmailField("Email", max_length=256, blank=True, null=True)

    mainpage_title = models.TextField("Əsas səhifə başlıq", blank=True, null=True)
    mainpage_content = models.TextField("Əsas səhifə kontent", blank=True, null=True)

    events_title = models.TextField("Tədbirlər başlıq", blank=True, null=True)
    events_content = models.TextField("Tədbirlər kontent", blank=True, null=True)

    training_title = models.TextField("Təlimlər əsas başlıq", blank=True, null=True)
    training_content = models.TextField("Təlimlər əsas kontent", blank=True, null=True)

    training_title1 = models.TextField("Təlimlər başlıq 1", blank=True, null=True)
    training_content1 = models.TextField("Təlimlər kontent 1", blank=True, null=True)

    training_title2 = models.TextField("Təlimlər başlıq 2", blank=True, null=True)
    training_content2 = models.TextField("Təlimlər kontent 2", blank=True, null=True)

    training_image1 = models.ImageField("Təlimlər şəkil 1", upload_to="site_imgs/", blank=True, null=True)
    training_image2 = models.ImageField("Təlimlər şəkil 2", upload_to="site_imgs/", blank=True, null=True)

    slogan = models.TextField("Sloqan", blank=True, null=True)

    aboutme_title = models.TextField("Haqqımda başlıq", blank=True, null=True)
    aboutme_subtitle = models.TextField("Haqqımda alt baslıq", blank=True, null=True)
    aboutme_content = models.TextField("Haqqımda kontent", blank=True, null=True)
    aboutme_image = models.ImageField("Haqqımda şəkil", upload_to="site_imgs/", blank=True, null=True)

    my_mission = models.TextField("Missiyam", blank=True, null=True)
    my_view = models.TextField("Görüşüm", blank=True, null=True)

    my_project_name = models.TextField("Layihə başlıq", blank=True, null=True)
    my_project_content = models.TextField("Layihə kontent", blank=True, null=True)
    my_project_image = models.ImageField("Layihə şəkil", upload_to="site_imgs/", blank=True, null=True)

    advertising_title = models.TextField("Reklam başlıq", blank=True, null=True)
    advertising_content = models.TextField("Reklam kontent", blank=True, null=True)
    advertising_image = models.ImageField("Reklam şəkil", upload_to="site_imgs/", blank=True, null=True)

    smm_title = models.TextField("SMM başlıq", blank=True, null=True)
    smm_content = models.TextField("SMM kontent", blank=True, null=True)
    smm_image1 = models.ImageField("SMM şəkil 1", upload_to="site_imgs/", blank=True, null=True)
    smm_image2 = models.ImageField("SMM şəkil 2", upload_to="site_imgs/", blank=True, null=True)
    smm_image3 = models.ImageField("SMM şəkil 3", upload_to="site_imgs/", blank=True, null=True)
    smm_image4 = models.ImageField("SMM şəkil 4", upload_to="site_imgs/", blank=True, null=True)

    smm_form_title = models.TextField("SMM Form başlıq", blank=True, null=True)
    smm_form_subtitle = models.TextField("SMM Form alt başlıq", blank=True, null=True)
    smm_form_content = models.TextField("SMM Form kontent", blank=True, null=True)

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
    image = models.ImageField(upload_to="banner_imgs/")

    class Meta:
        verbose_name = "banner"
        verbose_name_plural = "Bannerlər"

    def __str__(self):
        return self.image.url
    
class EventCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "tədbir kateqoriyası"
        verbose_name_plural = "Tədbir Kateqoriyaları"

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="event_imgs/")
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name="events")

    class Meta:
        verbose_name = "tədbir"
        verbose_name_plural = "Tədbirlər"

    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    link = models.TextField()
    text = models.TextField()

    class Meta:
        verbose_name = "rəy və uğur hekayəsi"
        verbose_name_plural = "Rəy və Uğur Hekayələri"

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to="blog_imgs/")
    highlighted = models.BooleanField(default=False)

    class Meta:
        verbose_name = "bloq"
        verbose_name_plural = "Bloqlar"

    def __str__(self):
        return self.title
    
class Education(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.TextField()

    class Meta:
        verbose_name = "təhsil və diplom"
        verbose_name_plural = "Təhsil və Diplomlar"

    def __str__(self):
        return self.title
    
class Offer(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    why_important = models.TextField()
    icon = models.TextField()
    image = models.ImageField(upload_to="offer_imgs/")

    class Meta:
        verbose_name = "təklif"
        verbose_name_plural = "Təkliflər"

    def __str__(self):
        return self.title
    
class Package(models.Model):
    PAYMENT_TYPES = (
        ('a', 'aylıq'),
        ('i', 'illik')
    )
    title = models.CharField(max_length=50)
    icon = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    payment_type = models.CharField(choices=PAYMENT_TYPES, max_length=1)
    content = models.TextField()

    class Meta:
        verbose_name = "paket"
        verbose_name_plural = "Paketlər"

    def __str__(self):
        return self.title
    
class Include(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name="includes")
    title = models.CharField(max_length=250)
    is_included = models.BooleanField(default=True)

    class Meta:
        verbose_name = "daxil olan"
        verbose_name_plural = "Paketə daxil olanlar"

    def __str__(self):
        return self.title
    
class Advantage(models.Model):
    title = models.TextField()

    class Meta:
        verbose_name = "üstünlük"
        verbose_name_plural = "Üstünlüklər"

    def __str__(self):
        return self.title
    
class Fag(models.Model):
    title = models.TextField()
    content = models.TextField()

    class Meta:
        verbose_name = "tez-tez verilən sual"
        verbose_name_plural = "Tez-tez verilən suallar"

    def __str__(self):
        return self.title
    
class SMMForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    brand = models.CharField(max_length=100)
    link = models.TextField()
    service = models.CharField(max_length=100)

    class Meta:
        verbose_name = "SMM müraciəti"
        verbose_name_plural = "SMM Müraciətləri"

    def __str__(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    price = models.FloatField()
    discount_price = models.FloatField()
    language = models.CharField(max_length=10) # bunu sorus
    purpose = models.TextField()
    trainer = models.CharField(max_length=50)
    slogan = models.TextField()

    class Meta:
        verbose_name = "kurs"
        verbose_name_plural = "Kurslar"

    def __str__(self):
        return self.title
    
class CourseAdvantage(models.Model):
    title = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="advantages")

    class Meta:
        verbose_name = "kurs üstünlüyü"
        verbose_name_plural = "Kurs Üstünlükləri"

    def __str__(self):
        return self.title
    
class Curriculum(models.Model):
    title = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="curriculums")

    class Meta:
        verbose_name = "tədris planı"
        verbose_name_plural = "Tədris planları"

    def __str__(self):
        return self.title
    
class CurriculumItem(models.Model):
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, related_name="items")
    title = models.TextField()
    duration = models.CharField(max_length=20)

    class Meta:
        verbose_name = "tədris mövzusu"
        verbose_name_plural = "Tədris mövzuları"

    def __str__(self):
        return self.title
    
class TrainingForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=20)
    your_work = models.CharField(max_length=150)
    difficult_area = models.CharField(max_length=150)
    important_degree = models.CharField(max_length=20)
    how_found = models.CharField(max_length=30)

    expectation = models.TextField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "təlim müraciəti"
        verbose_name_plural = "Təlim müraciətləri"

    def __str__(self):
        return self.name
    
class CertificateInfo(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    class Meta:
        verbose_name = "sertifikat məlumatı"
        verbose_name_plural = "Sertifikat məlumatları"

    def __str__(self):
        return self.title
    
class SocialMedia(models.Model):
    icon = models.TextField()
    link = models.URLField(max_length=256)

    class Meta:
        verbose_name = "sosial media hesabı"
        verbose_name_plural = "Sosial media hesabları"

    def __str__(self):
        return self.link

class Certificate(models.Model):
    certificate_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="certificate_imgs/")
    training_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "sertifikat"
        verbose_name_plural = "Sertifikatlar"

    def __str__(self):
        return self.name