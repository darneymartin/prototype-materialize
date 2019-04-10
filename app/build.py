import yaml
import sqlite3
import os
import sys
from jinja2 import Template, Environment, FileSystemLoader

config_data = None
with open("config.yml", 'r') as config_file:
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
