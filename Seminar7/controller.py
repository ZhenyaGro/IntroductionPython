import model

contact_list = {}


def create_contact(last_n, first_n, phone, desc):
    contact_list.update(model.contact(
        last_n, first_n, phone, desc))


def delete_contact(id_contact):
    contact_list.pop(id_contact)


def update_contact(id, last_n, first_n, phone, desc):
    if id in contact_list.keys():
        contact_list.update({f'{id}': id, 'Data': temp})
