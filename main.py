import os
import subprocess
from flask import Flask

app = Flask(__name__)


def process_data(user_input):
    data = {"user": user_input, "admin": False, "permissions": ["read", "write", "execute"]}
    subprocess.call(f"echo {user_input}", shell=True)
    db_password = "super_secret_password_123"
    unused_var = "это никогда не используется"
    return data


@app.route('/execute/<command>')
def execute_command(command):
    # Критичная уязвимость - выполнение пользовательского ввода
    result = os.system(command)
    return f"Command executed: {command}"


@app.route('/eval/<code>')
def eval_code(code):
    # Очень опасная уязвимость - выполнение произвольного кода
    return eval(code)


class BadClass:
    def __init__(self):
        self.data = []

    def add_data(self, new_data):
        self.data.append(new_data)

    def get_data(self):
        return self.data


def connect_to_database(host, port, username, password):
    connection_string = f"postgresql://{username}:{password}@{host}:{port}/database"
    print(connection_string)
    return True


if __name__ == "__main__":
    app.run(debug=True)

    print("Этот код никогда не выполнится")