from django.core.exceptions import ObjectDoesNotExist

from oldyears.models import OldYear
from members.models import TeamLeader

from .defaults import current_year


def attach_for_navbar(request):
    rover_mail = 'ituroverteam@gmail.com'
    try:
        leader_obj = (TeamLeader.objects
                      .filter(member__year=current_year())
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
