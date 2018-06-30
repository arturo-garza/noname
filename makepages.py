from jinja2 import Environment, PackageLoader, select_autoescape
import os

env = Environment(
    loader=PackageLoader('noname', 'templates')
)


output_dir = os.path.join(os.path.dirname(__file__), "out")

if not os.path.isdir(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, "example1.html"), "w") as file:
    file.write(env.get_template('example1.html').render())

