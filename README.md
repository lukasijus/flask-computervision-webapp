# Digital Oceans Ubunti 20.0 opencv4.3 and tensorflow 2.X configuration 

## Installing pip3, opencv, tensorflow 
Update apt-get
```
apt-get update 
apt-get -y update 
```

Installing pip3 
```
apt-get install -y python3-pip 
```

Installing opencv
```
apt-get install python-opencv 
```
Check opencv version
```
python3 -c "import cv2; print(cv2.__version__)"
```

Installing tensorflow
```
pip3 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow_cpu-2.3.0-cp38-cp38-manylinux2010_x86_64.whl
```
Check tensorflow version
```
python3 -c "import tensorflow as tf; print(tf.__version__)"
```

[Initial server setup with ubuntu](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04)

## Add domain and DNS A records in the DNS configuration panel

[Serving Flask application with uswgi and Nginx](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)

## clone this repo to your machine
```
git clone git@github.com:lukasijus/flask-computervision-webapp.git
```

## Setup environment variables
Install python-decouple
```
sudo pip3 install python-decouple
```
Create .env file 
```
touch .env   # create a new .env fil
nano .env    # open the .env file in the nano text editor
```
Add PORT value
```
PORT='0.0.0.0'
```


 
