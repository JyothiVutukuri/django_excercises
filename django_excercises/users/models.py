from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.formfields import PhoneNumberField

from django.db import models


class User(AbstractUser):
    """
    One Account = One User
    """
    # override the email from abstract user
    email = models.EmailField(verbose_name=_("Email Address"), max_length=50, unique=True)
    first_name = models.CharField(_('first name'), default='', max_length=30)
    last_name = models.CharField(_('last name'), default='', max_length=30)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.username = self.email = self.email.lower()
        return super().save(*args, **kwargs)


class Profile(models.Model):
    GENDERS = (
        ("MALE", _("Male")),
        ("FEMALE", _("Female")),
        ("OTHER", _("Other")),
        ("NOT_SPECIFIED", _("Not Specified")),
    )
    user = models.OneToOneField(User, blank=False, editable=False, on_delete=models.CASCADE, related_name="profile")
    gender = models.CharField(blank=False, choices=GENDERS, max_length=25, verbose_name=_("Gender"))
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    bio = models.TextField(blank=True, default="", null=False, verbose_name=_("Bio"))
    nationality = CountryField(verbose_name=_("Nationality"))


