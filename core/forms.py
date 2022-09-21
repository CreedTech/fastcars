from django import forms
from .models import Brand, Booking, ContactDetail, Subscriber, Testimonial
from django.core.mail import send_mail
from django.conf import settings


class BrandForm(forms.ModelForm):
    brand = forms.CharField(max_length=250)

    class Meta:
        model = Brand
        fields = ('brand',)


class BookingForm(forms.ModelForm):
    class Meta():
        model = Booking
        field = ['pick_up_location', 'drop_off_location', ]
        exclude = ['booking_date', 'user', 'car', ]


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ['created_at']


class SubscriberForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = ['sent_at']

    def get_info(self):

        # Cleaned data
        cl_data = super().clean()

        from_email = cl_data.get('email')
        subject = cl_data.get('email')

        msg = f'{from_email} subscribed to your newsletter'

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetail
        fields = '__all__'

    def get_info(self):

        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        subject = cl_data.get('subject')

        msg = f'{name} with email {from_email} said:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('message')

        return subject, msg

    def send(self):

        subject, msg = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
