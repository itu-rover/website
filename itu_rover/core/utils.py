from django.core.exceptions import ObjectDoesNotExist

from members.models import TeamLeader


def leader_phone_and_email(request):
    rover_mail = 'ituroverteam@gmail.com'
    try:
        leader_obj = TeamLeader.objects.select_related('leader').get()
        phone = leader_obj.leader.phone
    except AttributeError:
        phone = ''
    except ObjectDoesNotExist:
        phone = ''
    return {
        'main_phone': phone,
        'main_email': rover_mail,
    }
