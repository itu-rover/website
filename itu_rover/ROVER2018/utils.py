from django.core.exceptions import ValidationError


def validate_one_object(obj):
    """ Validate that there is only one instance from a model """
    model = obj.__class__
    if model.objects.count() > 0 and obj.pk != model.objects.get().pk:
        raise ValidationError("There can't be more than one object"
                              "of this type.")


def get_upload_path(instance, filename):
    directory = 'images/members'
    name, extension = filename.split('.')

    def format_name(s): return s.replace(' ', '_').lower()

    new_name = (format_name(instance.first_name) + "-" +
                format_name(instance.last_name))
    return '{0}/{1}.{2}'.format(directory, new_name, extension)
