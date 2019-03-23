from django.core.exceptions import ValidationError
from django.core.exceptions import ObjectDoesNotExist

import members.models


def leader_phone_and_email(request):
    rover_mail = 'ituroverteam@gmail.com'
    try:
        leader_obj = (members.models.TeamLeader.objects
                      .select_related('member').get())
        phone = leader_obj.member.phone
    except AttributeError:
        phone = ''
    except ObjectDoesNotExist:
        phone = ''
    return {
        'main_phone': phone,
        'main_email': rover_mail,
    }


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
