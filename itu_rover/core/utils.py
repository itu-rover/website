from django.core.exceptions import ObjectDoesNotExist

from oldyears.models import OldYear
from members.models import TeamLeader


def attach_for_navbar(request):
    rover_mail = 'ituroverteam@gmail.com'
    try:
        leader_obj = (TeamLeader.objects
                      .select_related('member').get())
        phone = leader_obj.member.phone
    except AttributeError:
        phone = ''
    except ObjectDoesNotExist:
        phone = ''
    return {
        'main_phone': phone,
        'main_email': rover_mail,
        'old_years': OldYear.objects.all(),
    }
