#!/usr/bin/env python3

import cv2
import requests
import numpy as np
from flask import Flask, Response

app = Flask(__name__)

# Konfiguration
URL = "http://FULLY_KIOSK_IP:2323/?cmd=getCamshot&password=YOUR_PASSWORD"

###############################################################################
def run_loop():

   while True:
      # Fordere das Bild von der URL an
      response = requests.get(URL)
      if response.status_code == 200:
         # Lese das Bild mit OpenCV ein
         frame = cv2.imdecode(np.frombuffer(response.content, np.uint8), -1)
         # Konvertiere das Frame in ein Byte-Array
         ret, buffer = cv2.imencode('.jpg', frame)
         frame = buffer.tobytes()
         yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

###############################################################################
@app.route('/fullystream')
def video_feed():
   return Response(run_loop(), mimetype='multipart/x-mixed-replace; boundary=frame')

###############################################################################
if __name__ == "__main__":
   app.run(
      host="192.168.0.50",
      port=5000
   )
