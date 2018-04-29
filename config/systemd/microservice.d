# Here's where you'd put the microservice Systemd script
[Unit]
Description=MicroserviceName

[Service]
Type=forking
ExecStart=python /Path/To/Service/Implementation.py
PIDFile=/var/run/microservice_name
Restart=on-failure