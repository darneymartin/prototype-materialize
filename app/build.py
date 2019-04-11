import yaml
import sqlite3
import os
import sys
from jinja2 import Template, Environment, FileSystemLoader
import argparse

def main(args):
    # Validations
    if args.config is None:
        print("Error: Please specify a configuration file.")
        exit(1)
    if not os.path.isfile(args.config):
        print("Error: file {} does not exsist.".format(args.config))
        exit(1)

    config_data = None
    with open(args.config ,'r') as config_file:
        try:
            config_data = yaml.safe_load(config_file)
        except yaml.YAMLError as exc:
            print(exc)


    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)

    #Python Templates
    app_template = env.get_template('app.py.j2')
    models_template = env.get_template('models.py.j2')

    #HTML Templates
    index_template = env.get_template('index.html.j2')
    form_template = env.get_template('form.html.j2')

    # Insert Variables
    app_output = app_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
    models_output = models_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
    index_output = index_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
    form_output = form_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])

    # Build Folder Structure
    if not os.path.exists(config_data["Application"]["Location"]):
        os.mkdir(config_data["Application"]["Location"])
    if not os.path.exists(config_data["Application"]["Location"]+"/app"):
        os.mkdir(config_data["Application"]["Location"]+"/app")
    if not os.path.exists(config_data["Application"]["Location"]+"/app/templates"):
        os.mkdir(config_data["Application"]["Location"]+"/app/templates")

    # Write New Files
    with open(config_data["Application"]["Location"]+"/app/app.py","w+") as new_file:
        new_file.write(app_output)

    with open(config_data["Application"]["Location"]+"/app/models.py","w+") as new_file:
        new_file.write(models_output)

    with open(config_data["Application"]["Location"]+"/app/templates/index.html","w+") as new_file:
        new_file.write(index_output)

    with open(config_data["Application"]["Location"]+"/app/templates/form.html","w+") as new_file:
        new_file.write(form_output)

    #Build DB
    sys.path.append(config_data["Application"]["Location"]+"/app")
    from app import db
    db.create_all()

ARG_HELP ="""
                              prototype-materialize
    --------------------------------------------------------------------------------
    This is the build script that converts and deploys the flask application you
    customized. A detailed list of options can be seen below:



    --------------------------------------------------------------------------------
    """
if __name__ == '__main__':
    try:
        args = argparse.ArgumentParser(description=ARG_HELP, formatter_class=argparse.RawTextHelpFormatter, usage=argparse.SUPPRESS)
        args.add_argument('--config','-c', dest='config', type=str, default=None, help="Path to a YAML configuration file to be used for configuring your application.")
        args = args.parse_args()
        # Launch Main
        main(args)
    except KeyboardInterrupt:
        print("\n[!] Key Event Detected...\n\n")
        exit(1)
    exit(0)
