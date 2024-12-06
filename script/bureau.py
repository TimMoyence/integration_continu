import csv
import os
from jinja2 import Environment, FileSystemLoader

csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../atelier1/membres-bureau-association.csv")
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")
output_file = "./view/bureau.html"

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("bureau.html")

members = []
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        member_data = {
            "prenom": row['prénom'],
            "nom": row['nom'],
            "email": row['email'],
            "fonction": row['fonction']
        }
        members.append(member_data)

with open(output_file, "w", encoding="utf-8") as output:
    output.write(template.render(members=members))

print(f"Bureau page generated successfully in {output_file}")