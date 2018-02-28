from django.core.exceptions import ValidationError


def validate_team_leader(obj):
    """ Validate that there is only one team leader instance """
    model = obj.__class__
    if model.objects.count() > 0 and obj.pk != model.objects.get().pk:
        raise ValidationError("There can't be more than one "
                              "team leader.")


def get_upload_path(instance, filename):
    directory = 'images/members'
    name, extension = filename.split('.')
    format_name = lambda s: s.replace(' ', '_').lower()
    new_name = (format_name(instance.first_name) + "-" +
                format_name(instance.last_name))
    return '{0}/{1}.{2}'.format(directory, new_name, extension)
