from django.db import models

from core.models import TimeStampedModel
from .utils import validate_one_object, get_upload_path


class Person(models.Model):
    """ Abstract base class representing a person """
    first_name = models.CharField(
        max_length=25,
        db_index=True,
        verbose_name='first name',
    )
    last_name = models.CharField(
        max_length=25,
        verbose_name='last name',
    )
    email = models.EmailField(
        blank=True,
        verbose_name='email address'
    )
    photo = models.ImageField(
        upload_to=get_upload_path,
        verbose_name='photo'
    )
    phone = models.CharField(
        max_length=13,
        blank=True,
        verbose_name='phone number',
    )
    is_retired = models.BooleanField(
        default=False,
        verbose_name='is member retired?',
    )

    class Meta:
        abstract = True
        ordering = ('first_name', 'last_name')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_photo_url(self):
        if not self.photo:
            return "default/photo.url"
        return self.photo.url

    def __str__(self):
        return self.get_full_name()


class Member(Person, TimeStampedModel):
    """ Team member model, a member is a person. """
    subteam = models.ForeignKey(
        "SubTeam",
        on_delete=models.SET_NULL,
        related_name='members',
        blank=True,
        null=True,
        verbose_name='subteam of member',
    )
    description = models.CharField(
        max_length=75,
        blank=True,
        verbose_name='description (e.g. department)',
    )

    def role(self):
        subteam_str = str(self.subteam)
        is_old = " Eski" if self.is_retired else ""
        if self.subteam.leader == self:
            return subteam_str + " Lideri"
        return subteam_str + is_old + " Üyesi"


class SubTeam(models.Model):
    """
    A subteam represents a group of people who work for the same
    specific domain of the project. For instance; mechanical subteam.
    """
    name = models.CharField(
        max_length=50,
        db_index=True,
        verbose_name='subteam name',
    )
    leader = models.OneToOneField(
        'Member',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='leader_of',
        verbose_name='subteam leader',
    )

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class TeamLeader(models.Model):
    """ Leader of the whole team """
    leader = models.OneToOneField(
        'Member',
        on_delete=models.SET_NULL,
        null=True,
        related_name='member',
        verbose_name='team leader',
    )

    class Meta:
        verbose_name = "team leader"
        verbose_name_plural = verbose_name

    def clean(self):
        validate_one_object(self)

    def __str__(self):
        return str(self.leader)

    def role(self):
        return "Takım Lideri"


class TeamAdvisor(Person, TimeStampedModel):
    description = models.CharField(
        max_length=75,
        verbose_name='description (e.g. department)',
    )

    def role(self):
        return "Takım Danışmanı"


class MembersPage(models.Model):
    proposal = models.FileField(upload_to='documents/team')

    def clean(self):
        validate_one_object(self)

    def __str__(self):
        return "members page"

    class Meta:
        verbose_name = "members page"
        verbose_name_plural = verbose_name
