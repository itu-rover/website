from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from members.models import TeamLeader


def leader_phone_and_email(request):
    rover_mail = 'ituroverteam@gmail.com'
    try:
        leader_obj = TeamLeader.objects.select_related('member').get()
        phone = leader_obj.member.phone
    except AttributeError:
        phone = ''
    except ObjectDoesNotExist:
        phone = ''
    return {
        'main_phone': phone,
        'main_email': rover_mail,
    }


def current_year():
    return timezone.now().year
