from random import randint
import random
from model.group import Group
def test_del_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) < 2:
        #group = f"my group{randint(0, 500)}"
        group = f"my group 2"
        app.groups.add_new_group(group)
        old_list = app.groups.get_group_list()

    group = random.choice(old_list)
    app.groups.del_group_with_contacts(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list) == sorted(new_list)