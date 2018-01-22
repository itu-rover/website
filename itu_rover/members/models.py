from django.db import models

from .utils import validate_team_leader


class Person(models.Model):
    """ Abstract base class representing a person """
    first_name = models.CharField(
        max_length=25,
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

    def __str__(self):
        return self.first_name + " " + self.last_name


class Member(Person):
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


class SubTeam(models.Model):
    """
    A subteam represents a group of people who work for the same
    specific domain of the project. For instance; mechanical subteam.
    """
    name = models.CharField(
        max_length=50,
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
        validate_team_leader(self)

    def __str__(self):
        return str(self.leader)


class TeamAdvisor(Person):
    description = models.CharField(
        max_length=75,
        verbose_name='description (e.g. department)',
    )
