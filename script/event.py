import markdown
import os
from jinja2 import Environment, FileSystemLoader

# 
content_dir = "./atelier1"
image_dir = "../atelier1"
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")


env = Environment(loader=FileSystemLoader(template_dir))
event_template = env.get_template("event.html")  



def read_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    content = []
    event_title = "Titre de l'événement"  

    for line in lines:
        
        if line.startswith("# "):
            event_title = line[2:].strip()  # 
        else:
            content.append(line)
    
    
    event_content = markdown.markdown("".join(content), extensions=['extra', 'smarty', 'toc'])
    
    return event_title, event_content


for file_name in os.listdir(content_dir):
    if file_name.endswith(".md"):
        
        event_date = "-".join(file_name.split("-")[0:3])
        image_file = f"evenement-{file_name.split('-')[-1].split('.')[0]}.webp"
        
        
        event_output_file = f"./view/{file_name.replace('.md', '.html')}"

        
        event_title, event_content = read_markdown(os.path.join(content_dir, file_name))

        
        event_data = {
            "title": event_title,
            "date": event_date,
            "content": event_content,
            "image": os.path.join(image_dir, image_file)
        }

        
        with open(event_output_file, "w", encoding="utf-8") as output:
            output.write(event_template.render(**event_data))

print("Individual event pages generated successfully.")