import markdown
import os
from jinja2 import Environment, FileSystemLoader

# Paths to content and templates
content_dir = "./atelier1"
image_dir = "../atelier1"
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")

# Initialize the Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))
event_template = env.get_template("event.html")  # Utiliser le template unique

# Function to read entire markdown content for a full event page
# and extract the first title as the event title
def read_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    content = []
    event_title = "Titre de l'événement"  # Valeur par défaut si aucun titre n'est trouvé

    for line in lines:
        # Check if the line starts with '# ' to get the first title as the event title
        if line.startswith("# "):
            event_title = line[2:].strip()  # Remove '# ' and get the rest as title
        else:
            content.append(line)
    
    # Convert the remaining content (without the first title) to HTML
    event_content = markdown.markdown("".join(content), extensions=['extra', 'smarty', 'toc'])
    
    return event_title, event_content

# Parse markdown files and generate a page for each event
for file_name in os.listdir(content_dir):
    if file_name.endswith(".md"):
        # Extract event details from file names
        event_date = "-".join(file_name.split("-")[0:3])
        image_file = f"evenement-{file_name.split('-')[-1].split('.')[0]}.webp"
        
        # Name of the output file for each event
        event_output_file = f"./view/{file_name.replace('.md', '.html')}"

        # Read the full content of the markdown file and extract the title
        event_title, event_content = read_markdown(os.path.join(content_dir, file_name))

        # Event data dictionary to pass to the template
        event_data = {
            "title": event_title,
            "date": event_date,
            "content": event_content,
            "image": os.path.join(image_dir, image_file)
        }

        # Render the individual event page
        with open(event_output_file, "w", encoding="utf-8") as output:
            output.write(event_template.render(**event_data))

print("Individual event pages generated successfully.")