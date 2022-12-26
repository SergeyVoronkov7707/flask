from flask import Flask, request
from fileinput import FileInput


app = Flask(__name__)


@app.route('/')
def index():
    with open('count.txt', 'r') as f:
        old_count = f.read()
    new_count = old_count.replace(old_count, str(int(old_count) + 1))
    with open('count.txt', 'w') as f:
        f.write(new_count)
    return f"hello {new_count}"
