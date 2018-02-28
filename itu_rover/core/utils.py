from members.models import TeamLeader


def leader_phone_and_email(request):
    try:
        leader_obj = TeamLeader.objects.select_related('leader').get()
        return {
            'phone': leader_obj.leader.phone,
            'email': leader_obj.leader.email,
        }
    except AttributeError:
        return {'phone': '', 'email': 'ituroverteam@gmail.com'}
