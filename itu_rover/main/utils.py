def slider_image_upload_to(instance, filename):
    name, extension = filename.split('.')[-2:]
    new_name = instance.title.replace(' ', '_').lower()
    return 'images/slider/%s' % (new_name + "." + extension)
