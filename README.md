Converts the images from the fully kiosk browser camera into readable format for synology surveillance station.
You have to replace the IP and PW with the IP of your fully kiosk browser device and its password.

## Fully Kiosk Browser Settings:

Web Content Settings:
-> Enable Webcam Access (PLUS) = ON

Motion Detection (PLUS)
-> Enable Visual Motion Detection = ON

Remote Administration (PLUS)
-> Enable Camshot on Remote Admin = ON


## Running fullystream.py as service

1. copy fullystream.service to /etc/systemd/system/
2. copy fullystream.py to /home/pi/
3. reload daemon: sudo systemctl daemon-reload
4. enable service: sudo systemctl enable fullystream.service
5. start service: sudo systemctl start fullystream.service
6. check if service is running: sudo systemctl status fullystream.service

## Retrieve stream:

http://192.168.0.50:5000/fullystream

    
