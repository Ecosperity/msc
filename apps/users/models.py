from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, SmallIntegerField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for dreamjob.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    ADMIN = 0
    MANAGER = 1
    STAFF = 2
    EMPLOYEE = 3
    APPLICANT_USER = 4

    ROLE_CHOICES = (
        (ADMIN, 'Super Admin'),
        (MANAGER, 'Manager'),
        (STAFF, 'Staff'),
        (EMPLOYEE, 'Employee'),
        (APPLICANT_USER, 'Applicant User')
    )
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    role = SmallIntegerField(choices=ROLE_CHOICES, default=APPLICANT_USER)


    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
