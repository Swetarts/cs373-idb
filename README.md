# Environment
To get your application up and running you need a couple of things:
* [npm](https://www.npmjs.com/)
* [Bower](http://bower.io)
* Python 3.4

After you get bower installed, run this command inside of the **root** project directory (cs373-idb)
```bash
$ bower install
```

This will create the directory `www/bower_components` and install all of our front end assets such as Angular and Bootstrap there.

After that create a python virtual environment with
```bash
$ pyvenv-3.4 venv
```

This will create a directory called venv. 

To activate your virtual envrionment run:
```bash
$ source venv/bin/activate
```

Note: You may receive an error while attempting to create the virtual environment in Ubuntu 14.04. Apparently Ubuntu 14.04 was shipped with a broken pyvenv. Do the following. This will create the venv without pip. Get pip in the environment afterwards.

```bash
$ pyvenv-3.4 --without-pip venv
```

Now you can install all of the packages for our flask app and everything *should* work. To do this run
```bash
pip3 install -r requirements.txt
```

# Running the application
* `$ python server.py`
* visit localhost:5000/index.html

# Server Information
The Server lives at `104.239.165.88`

To log in run
```bash
ssh -i .ssh/id_rsa.pub swetard@104.239.165.88
```
Yes, the username is `swetard`. Please get your ssh keys to me **ASAP** so that I can add them to the `authorized_keys` file. K thks
