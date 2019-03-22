# prototype-materialize

prototype-materialize is a project built to help prototype Python web applications with Flask, SQLite3 and the Materialize CSS Framework.

### Install
The setup.sh script will install all necessary requirements, create cert & key files, and move the working directory to /opt/transportc2:
```
git clone https://github.com/darneymartin/prototype-materialize
cd prototype-materialize
pip3 install -r requirements.txt
```

### Building Your First Prototype
* Modify the config.yml under the app directory to meet your criteria
* Run the `build.py` python script
* Your newly created will be under 'build/app' folder run the `app.py` to start Flask


##### Upcoming Changes
* Refactoring to insure clear code
* Refinement on UI
* Adding support for MySQL
* Adding Flask authentication and user management
* Error handling on Frontend and Backend
* UI build options
