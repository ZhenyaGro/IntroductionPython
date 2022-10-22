from dotenv import load_dotenv
import os

load_dotenv()

my_login = os.getenv('login')
my_pass = os.getenv('password')

print(f'login = {my_login}\npassword = {my_pass}')
