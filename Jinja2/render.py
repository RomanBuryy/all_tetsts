from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import datetime

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

page_template = env.get_template('website.html')

print(page_template.render(today=datetime.now()))
