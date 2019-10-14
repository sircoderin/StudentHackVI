# StudentHackVI
StudentHack VI Repository

## Useful Links:
* [Google drive](https://drive.google.com/drive/folders/1acCDZJ6AFxnoCsqWmlKqErQZlqES01oQ)
* [Flask Spec](http://flask.pocoo.org/docs/0.12/quickstart/)

# Python Environment

I still don't know exactly how `virtualenv` works but _if_ we use Python for our project it should have it own virtual environment because we'll run it on different machines and we want to stay away from version hell.
With this, every binary is installed in `env/bin/`, when you `activate` it all the python packages you run will be the ones from `env/bin/` and we can keep versions in check.

All you have to do is:
1. Install it globally: `pip install virtualenv`
2. Set it up: `virtualenv --no-site-packages --distribute env`
3. Activate it (Your shell will say `env)`): `source env/bin/activate` (`env\Scripts\activate` on Windows)
4. Install the dependencies: `pip install -r requirements.txt`
5. When you want to go back to using your global python and pip instances, just type: `deactivate`

Another nice thing we can do is:
1. Add the following line to every executable: `# env/bin/python3`
2. Add permissions to the file: `chmod +x script.py`
3. Run it like this: `./script.py`

# Flask app

To run a flask app, all you have to do is:
1. Set it up: `export FLASK_APP=app.py`
2. [Optional]: `export FLASK_DEBUG=1`
2. Run it with Flask: `flask run`

Also if you turn on debugging (`export FLASK_DEBUG=1`) before running, the server will reload itself on code changes.
Also when shit goes down the fan, Flask will even show you a console in the browser to help you debug stuff.
