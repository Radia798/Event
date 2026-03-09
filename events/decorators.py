from django.contrib.auth.decorators import user_passes_test

def role_required(role_name):
    def check_role(user):
        return user.groups.filter(name=role_name).exists() or user.is_superuser
    return user_passes_test(check_role)