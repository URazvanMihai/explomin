from rolepermissions.roles import AbstractUserRole

class User(AbstractUserRole):
    available_permissions = {
        'vizualizare_program': True,
    }

class Admin(AbstractUserRole):
    available_permissions = {
        'modificare_program': True,
    }