from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
from flask import Flask,render_template,Response
import cv2

views = Blueprint('views', __name__)
camera=cv2.VideoCapture(0)

#@views.route('/', methods=['GET', 'POST'])
@login_required


def generate_frames():
    while True:
            
        ## read the camera frame
        success,frame=camera.read()
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()

        yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
@views.route('/')
def home():
    
    return render_template("home.html", user=current_user)

@views.route('/video')
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@views.route('/account')
@login_required
def account():
    return render_template("account.html", user=current_user)

@views.route('/iot')
@login_required
def iot():
    return render_template("iot.html", user=current_user)

@views.route('/log')
@login_required
def log():
    return render_template("log.html", user=current_user)

@views.route('/map')
@login_required
def map():
    return render_template("map.html", user=current_user)    