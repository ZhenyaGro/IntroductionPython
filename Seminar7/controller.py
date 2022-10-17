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
        model.create_contact(
            contact_info[0], contact_info[1], contact_info[2], contact_info[3])
        view.show_contacts(model.contacts_list)
    if menu_point == 2:
        view.show_contacts(model.read_file())
    if menu_point == 3:
        # Import contact
        pass
    if menu_point == 4:
        # Export contact
        pass
    if menu_point == -1:
        sleep(1)
        launch_app()
