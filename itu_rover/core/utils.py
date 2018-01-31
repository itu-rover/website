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


def slider_image_upload_to(instance, filename):
    name, extension = filename.split('.')
    new_name = instance.title.replace(' ', '_').lower()
    return 'slider/%s' % (new_name + extension)
