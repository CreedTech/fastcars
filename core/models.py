from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from multiselectfield import MultiSelectField
from account.models import User
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class About(models.Model):
    video_image = models.ImageField(upload_to='AboutImages/')
    video = models.URLField()
    title = models.CharField(max_length=150)
    text = models.TextField()
    number = models.CharField(max_length=20)
    author = models.CharField(max_length=50)
    signature = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("About Us")
        verbose_name_plural = ("About Fast Cars")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("About_detail", kwargs={"pk": self.pk})


class ContactDetail(models.Model):
    name = models.CharField(max_length=100, help_text='Sam Smith')
    email = models.EmailField(max_length=254, help_text="SS@gmail.com")
    subject = models.CharField(max_length=100, help_text="Booking")
    message = models.TextField(help_text='My name is...')

    class Meta:
        verbose_name = ("Contact Detail")
        verbose_name_plural = ("Contact Details")

    def __str__(self):
        return f'{self.name} ------------- {self.email}'

    def get_absolute_url(self):
        return reverse("Contactdetails", kwargs={"pk": self.pk})


class ContactInfo(models.Model):
    number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        verbose_name = ("Contact Info")
        verbose_name_plural = ("Contact Information")

    def __str__(self):
        return f'{self.email} ------------- {self.number}'

    def get_absolute_url(self):
        return reverse("ContactInfo_details", kwargs={"pk": self.pk})


class Brand(models.Model):
    brand = models.CharField(max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = ("Brand")
        verbose_name_plural = ("Brands")

    def __str__(self):
        return self.brand

    def save(self, *args, **kwargs):
        slug = self.brand
        self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:product_brand", kwargs={"pk": self.pk})


class Carousel(models.Model):
    car_name = models.CharField(verbose_name='car_title', max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    car_photo = models.ImageField(validators=[FileExtensionValidator(
        ['jpg', 'jpeg'])], upload_to='cars_images')

    def __str__(self):
        return self.car_name


class Car(models.Model):
    state_choice = (
        ('NI', 'Niger'),
        ('BO', 'Borno '),
        ('TA', 'Taraba'),
        ('KD', 'Kaduna'),
        ('BA', 'Bauchi'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
        ('AD', 'Adamawa'),
        ('KW', 'Kwara'),
        ('KE', 'Kebbi'),
        ('BE', 'Benue'),
        ('PL', 'Plateau'),
        ('KO', 'Kogi'),
        ('OY', 'Oyo'),
        ('NA', 'Nasarawa'),
        ('SO', 'Sokoto'),
        ('KT', 'Katsina'),
        ('JI', 'Jigawa'),
        ('CR', 'Cross River'),
        ('KN', 'Kano'),
        ('GO', 'Gombe'),
        ('ED', 'Edo'),
        ('DE', 'Delta'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('RI', 'Rivers'),
        ('BY', 'Bayelsa'),
        ('OS', 'Osun'),
        ('FC', 'Fct'),
        ('EN', 'Enugun'),
        ('AK', 'Akwa Ibom'),
        ('EK', 'Ekit'),
        ('AB', 'Abia'),
        ('EB', 'Ebonyi'),
        ('IM', 'Imo'),
        ('AN', 'Anambra'),
        ('LA', 'Lagos'),
    )

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    car_name = models.CharField(verbose_name='car_title', max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10, choices=state_choice)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('Year'), choices=year_choice)
    condition = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    car_photo = models.ImageField(validators=[FileExtensionValidator(
        ['jpg', 'jpeg'])], upload_to='cars_images')
    car_photo_1 = models.ImageField(validators=[FileExtensionValidator(
        ['jpg', 'jpeg'])], upload_to='cars_images', blank=True)
    car_photo_2 = models.ImageField(validators=[FileExtensionValidator(
        ['jpg', 'jpeg'])], upload_to='cars_images', blank=True)
    body_style = models.CharField(max_length=200)
    miles = models.PositiveIntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.PositiveIntegerField()
    milage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50)
    is_latest = models.BooleanField(default=False)
    is_booked = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True)

    def __str__(self):
        return self.car_name

    def save(self, *args, **kwargs):
        slug = self.brand
        if not self.slug:
            self.slug = slugify(slug, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:product", kwargs={'id': self.id})

    def get_booking_url(self):
        return reverse("core:booking", kwargs={'slug': self.slug})


class Booking(models.Model):
    state_choice = (
        ('NI', 'Niger'),
        ('BO', 'Borno '),
        ('TA', 'Taraba'),
        ('KD', 'Kaduna'),
        ('BA', 'Bauchi'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
        ('AD', 'Adamawa'),
        ('KW', 'Kwara'),
        ('KE', 'Kebbi'),
        ('BE', 'Benue'),
        ('PL', 'Plateau'),
        ('KO', 'Kogi'),
        ('OY', 'Oyo'),
        ('NA', 'Nasarawa'),
        ('SO', 'Sokoto'),
        ('KT', 'Katsina'),
        ('JI', 'Jigawa'),
        ('CR', 'Cross River'),
        ('KN', 'Kano'),
        ('GO', 'Gombe'),
        ('ED', 'Edo'),
        ('DE', 'Delta'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('RI', 'Rivers'),
        ('BY', 'Bayelsa'),
        ('OS', 'Osun'),
        ('FC', 'Fct'),
        ('EN', 'Enugun'),
        ('AK', 'Akwa Ibom'),
        ('EK', 'Ekit'),
        ('AB', 'Abia'),
        ('EB', 'Ebonyi'),
        ('IM', 'Imo'),
        ('AN', 'Anambra'),
        ('LA', 'Lagos'),
    )
    pick_up_location = models.CharField(max_length=10, choices=state_choice)
    drop_off_location = models.CharField(max_length=10, choices=state_choice)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    To_agree = models.BooleanField(default=False, verbose_name='Car is Booked')

    def __str__(self):
        return f"{self.user.first_name} booked {self.car.car_name} from {self.pick_up_location} to {self.drop_off_location}"


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='TestimonialImages/')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Testimonial")
        verbose_name_plural = ("Testimonials")

    def __str__(self):
        return f'{self.name} ----------- {self.location}'

    def get_absolute_url(self):
        return reverse("Testimonial_detail", kwargs={"pk": self.pk})


class Subscriber(models.Model):
    email = models.EmailField(max_length=254)
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Subscriber")
        verbose_name_plural = ("Subscribers")

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse("Subscriber_detail", kwargs={"pk": self.pk})
