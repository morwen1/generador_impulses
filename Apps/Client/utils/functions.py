# Model
from Apps.General.user.models import Telefono


def add_first_phone(value, person_model):
    phone = Telefono()
    phone.numero = value
    phone.save()
    person_model.telefonos.add(phone.pk)
    return None
