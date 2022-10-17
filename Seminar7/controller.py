from audioop import add
from time import sleep
import model
import view


def launch_app():
    menu_point = view.menu()
    if menu_point == 0:
        return
    if menu_point == 1:
        contact_info = view.add_contact()
        contact = model.create_contact(*contact_info)
        view.show_contacts(contact)
    if menu_point == 2:
        contacts_list = model.import_contacts('Seminar7/contacts.csv')
        if contacts_list:
            for i in contacts_list:
                view.show_contacts(i)
    if menu_point == 3:
        # Export contact
        pass
    if menu_point == -1:
        sleep(1)
        launch_app()
