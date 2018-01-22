from django.core.exceptions import ValidationError


def validate_team_leader(obj):
    """ Validate that there is only one team leader instance """
    model = obj.__class__
    if model.objects.count() > 0 and obj.pk != model.objects.get().pk:
        raise ValidationError("There can't be more than one "
                              "team leader.")
