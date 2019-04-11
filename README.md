# prototype-materialize

prototype-materialize is a project built to help prototype Python web applications with Flask, SQLite3 and the Materialize CSS Framework.

### Install
```
git clone https://github.com/darneymartin/prototype-materialize
cd prototype-materialize
pip3 install -r requirements.txt
```

### Building Your First Prototype
* Modify the `config.yml` under the app directory to meet your criteria
* Run the `build.py` python script by typing ```python3 ./build.py -c config.yml```
* Your newly created will be under the folder you specified to run you new application change to that directory
* Run the `app.py` in your defined custom application directory to start your Flask application


##### Upcoming Changes
* Refactoring to insure clear code
* Refinement on UI
* Adding support for MySQL
* Adding Flask authentication and user management
* Error handling on Frontend and Backend
* UI build options
