from flask import Flask, request, render_template
import requests
import random
import argparse

Q = []

with open("q.txt") as f:
    for q in f:
        Q.append(q.strip())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get():
    return random.choice(Q)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=20180, type=int)
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    app.debug = args.debug
    app.run('0.0.0.0', args.port)


if __name__ == '__main__':
    main()
