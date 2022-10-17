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
        # view.show_contacts(model.read_file())
        pass
    if menu_point == 3:
        # Import contact
        pass
    if menu_point == 4:
        # Export contact
        pass
    if menu_point == -1:
        sleep(1)
        launch_app()
