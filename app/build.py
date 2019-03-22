import yaml
import sqlite3
import os
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
db_template = env.get_template('db.py.j2')
model_template = env.get_template('model.py.j2')

#SQL Templates
create_template = env.get_template('create.sql.j2')

#HTML Templates
index_template = env.get_template('index.html.j2')
form_template = env.get_template('form.html.j2')


app_output = app_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
db_output = db_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
model_output = model_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
create_output = create_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
index_output = index_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])
form_output = form_template.render(Application=config_data["Application"] , Model=config_data["Model"] ,Database=config_data["Database"])

with open("build/app/app.py","w+") as new_file:
    new_file.write(app_output)

with open("build/app/db.py","w+") as new_file:
    new_file.write(db_output)

with open("build/app/model.py","w+") as new_file:
    new_file.write(model_output)

#with open("build/app","") as new_file:
#    new_file.write(create_output)

with open("build/app/templates/index.html","w+") as new_file:
    new_file.write(index_output)

with open("build/app/templates/form.html","w+") as new_file:
    new_file.write(form_output)

#Build DB
try:
    exists = os.path.isfile("build/app/app.db")
    if exists:
        os.remove("build/app/app.db")
    conn = sqlite3.connect("build/app/app.db")
    c = conn.cursor()
    c.execute(create_output)
except Error as e:
    print(e)
