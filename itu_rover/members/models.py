from django.db import models
from django.db.models import ObjectDoesNotExist

from core.models import TimeStampedModel
from core.defaults import current_year
from .utils import get_upload_path


# Temel insan modelini tanımlar.
# Member, Team Advisor ve Team Leader modelleri Person modeli bazalınarak kurulur.
# Her Member, Team Advisor ve Team Leader birer Person'dır.
# Foreign Key'in ne olduğunun ve hangi amaçla kullanıldığının bilmesi kolaylık sağlayacaktır.
# eng_role fonksiyonu, sayfaya İngilizce Subteam isimleri basması için düzenlenecek.
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
    year = models.PositiveSmallIntegerField(
        verbose_name='active year',
        default=current_year,
    )
    is_retired = models.BooleanField(
        default=False,
        verbose_name='is member retired?',
    )
    did_work = models.BooleanField(
        default=False,
        verbose_name="if True: This person will be shown on 'graduated' page"
                     "with the infos of 'working' and 'eng_working'"
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
    eng_description = models.CharField(
        max_length=75,
        blank=True,
        verbose_name='english description (e.g. department)',
    )
    linkedin_link = models.TextField(
        blank=True,
        null=True,
        verbose_name="Linkedin profile link of this person"
    )
    working = models.TextField(
        blank=True,
        null=True,
        verbose_name='working experiences'
    )
    eng_working = models.TextField(
        blank=True,
        null=True,
        verbose_name='english working experiences'
    )

    class MemberManager(models.Manager):
        def get_queryset(self):
            return (super().get_queryset()
                    .select_related('leader',
                                    'subteam')
                    .prefetch_related('subteam__leaders'))
    objects = MemberManager()

    def role(self):
        subteam_str = str(self.subteam)
        is_old = " Eski" if self.is_retired else ""

        try:
            is_team_leader = bool(self.leader)
        except ObjectDoesNotExist:
            is_team_leader = False

        if self.subteam and self in self.subteam.leaders.all():
            return subteam_str + " Lideri"
        elif is_team_leader:
            return "Takım Lideri"
        elif not self.subteam:
            return "Ekip Üyesi"
        return subteam_str + is_old + " Üyesi"

    def eng_role(self):
        if self.subteam == None:
            subteam_str = "Member of Subteam"
        else:
            subteam_str = str(self.subteam.eng_name)
        is_old = " Old" if self.is_retired else ""

        try:
            is_team_leader = bool(self.leader)
        except ObjectDoesNotExist:
            is_team_leader = False

        if self.subteam and self in self.subteam.leaders.all():
            return " Leader of " + subteam_str
        elif is_team_leader:
            return "Team Leader"
        elif not self.subteam:
            return "Ekip Üyesi"
        return is_old + " Member of " + subteam_str


class SubTeam(models.Model):
    """
    A subteam represents a group of people who work for the same
    specific domain of the project. For instance; mechanical subteam.
    """
    name = models.CharField(
        max_length=50,
        default="name",
        db_index=True,
        verbose_name='subteam name',
    )
    eng_name = models.CharField(
        max_length=50,
        db_index=True,
        default="eng_name",
        verbose_name='subteam eng name',
    )
    leaders = models.ManyToManyField(
        'Member',
        blank=True,
        related_name='leader_of',
        verbose_name='subteam leaders',
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TeamLeader(models.Model):
    """ Leader of the whole team """
    member = models.OneToOneField(
        'Member',
        on_delete=models.SET_NULL,
        null=True,
        related_name='leader',
        verbose_name='team leader',
    )

    class Meta:
        verbose_name = "team leader"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.member)


class TeamAdvisor(Person, TimeStampedModel):
    description = models.CharField(
        max_length=75,
        verbose_name='description (e.g. department)',
    )

    def role(self):
        return "Takım Danışmanı"


class MembersPage(models.Model):
    proposal = models.FileField(
        upload_to='documents/team',
        blank=True,
    )
    team_photo = models.ImageField(
        upload_to='images/members',
        blank=True,
    )
    year = models.PositiveSmallIntegerField(
        verbose_name='team year',
        default=current_year,
        unique=True,
    )

    def __str__(self):
        return "Members Page " + str(self.year)

    class Meta:
        verbose_name = "Members Page"
        verbose_name_plural = verbose_name
