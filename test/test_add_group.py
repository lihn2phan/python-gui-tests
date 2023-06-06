from random import randint


def test_add_group(app):
    group = f"my group{randint(0, 500)}"
    #group = f"my group433"
    old_list = app.groups.get_group_list()
    if group in old_list:
        app.groups.del_group_with_contacts(group)
        old_list.remove(group)
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list) == sorted(new_list)
