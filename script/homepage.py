import markdown
import os
from jinja2 import Environment, FileSystemLoader

content_dir = "./atelier1"
image_dir = "./atelier1"
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")
output_file = "./view/index.html"

routerDirectory = [
    "2025-01-18-evenement-1.html",
    "2025-02-16-evenement-2.html",
    "2025-03-23-evenement-3.html",
    "2025-04-11-evenement-4.html",
    "2025-05-17-evenement-5.html",
    "2025-06-21-evenement-6.html"
]

env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("homepage.html")

def read_markdown_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    content = []
    event_title = "Titre de l'événement"  
    in_summary_section = False

    for line in lines:
        if line.startswith("# "):
            event_title = line[2:].strip() 
            in_summary_section = True 
        elif line.startswith("##"): 
            break
        elif in_summary_section:
            content.append(line.strip()) 

    summary = markdown.markdown("\n".join(content), extensions=['extra', 'smarty', 'toc'])
    return event_title, summary

events = []
markdown_files = sorted([f for f in os.listdir(content_dir) if f.endswith(".md")])

for i, file_name in enumerate(markdown_files):
    
    event_date = "-".join(file_name.split("-")[0:3])
    image_file = f"evenement-{file_name.split('-')[-1].split('.')[0]}.webp"    
    event_href = routerDirectory[i] if i < len(routerDirectory) else "#"
    event_title, event_summary = read_markdown_summary(os.path.join(content_dir, file_name))

    event_data = {
        "title": event_title,            
        "date": event_date,
        "content": event_summary,        
        "image": os.path.join(image_dir, image_file),
        "href": event_href               
    }
    events.append(event_data)

with open(output_file, "w", encoding="utf-8") as output:
    output.write(template.render(events=events))

print(f"Homepage generated successfully in {output_file}")