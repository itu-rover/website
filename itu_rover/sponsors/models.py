from django.db import models


class Sponsor(models.Model):
    """ Represents organizations supporting the project """
    image = models.ImageField()
    display_width = models.PositiveSmallIntegerField()
    name = models.CharField(
        max_length=50,
        verbose_name='name',
    )
    website = models.URLField(verbose_name='website')
    sponsorship_type = models.ForeignKey(
        "SponsorshipType",
        on_delete=models.SET_NULL,
        null=True,
        related_name='sponsors',
        verbose_name='type of sponsorship',
    )
    is_name_on_display = models.BooleanField(
        default=False,
        verbose_name='put name under the image on display?',
    )
    is_old = models.BooleanField(
        default=False,
        verbose_name='is sponsor old?',
    )

    def __str__(self):
        return self.name


class SponsorshipType(models.Model):
    """ Represents kinds of sponsorships """
    name = models.CharField(
        max_length=30,
        verbose_name='type name',
    )
    priority = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('priority', )

    def __str__(self):
        return self.name
