from pool.models import Cinema, Showing, VoteMovie, VoteShowing, Sales
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

#
# Group of users that are cinema's owners
#
cinema_grp, created = Group.objects.get_or_create(name='cinema_grp')

# Authorized to add a new cinema
ct = ContentType.objects.get_for_model(Cinema)
permission = Permission.objects.create(codename='can_create_cinema',
                                       name='Can create cinema',
                                       content_type=ct)
cinema_grp.permissions.add(permission)

# Authorized to create a new showing
ct = ContentType.objects.get_for_model(Showing)
permission = Permission.objects.create(codename='can_create_showing',
                                       name='Can create showing',
                                       content_type=ct)
cinema_grp.permissions.add(permission)
