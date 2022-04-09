# import os
# from dotenv import load_dotenv
# from flask import Flask, render_template, request, abort

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)