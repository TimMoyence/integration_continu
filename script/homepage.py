import markdown
import os
from jinja2 import Environment, FileSystemLoader

# Path to your content and templates
content_dir = "./atelier1"
image_dir = "./atelier1"
template_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the script's directory
output_file = "./view/index.html"

# Initialize the Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("template.html")

# Helper function to read markdown files
def read_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return markdown.markdown(content)

# Parse markdown files and build the data structure for rendering
events = []
for file_name in os.listdir(content_dir):
    if file_name.endswith(".md"):
        # Extract event details from file names and markdown content
        event_date = file_name.split("-")[0:3]  # Extract date
        event_title = file_name.split("-")[3].split(".")[0].replace("_", " ").title()
        image_file = f"evenement-{file_name.split('-')[2].split('.')[0]}.webp"
        
        event_data = {
            "title": event_title,
            "date": "-".join(event_date),
            "content": read_markdown(os.path.join(content_dir, file_name)),
            "image": os.path.join(image_dir, image_file)
        }
        events.append(event_data)

# Render the index.html template with the events
with open(output_file, "w", encoding="utf-8") as output:
    output.write(template.render(events=events))

print(f"Homepage generated successfully in {output_file}")
