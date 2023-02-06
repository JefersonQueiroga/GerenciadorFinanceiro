from rolepermissions.roles import AbstractUserRole

# comando python manage.py sync_roles


class Administrador(AbstractUserRole):
    available_permission = {}


class Funcionario(AbstractUserRole):
    available_permissions = {}
