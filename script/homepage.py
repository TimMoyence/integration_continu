import markdown
import os
from jinja2 import Environment, FileSystemLoader

# Paths to content and templates
content_dir = "./atelier1"
image_dir = "../atelier1"
template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")
output_file = "./view/index.html"

# Router paths (corresponding HTML pages for each event)
routerDirectory = [
    "2025-01-18-evenement-1.html",
    "2025-02-16-evenement-2.html",
    "2025-03-23-evenement-3.html",
    "2025-04-11-evenement-4.html",
    "2025-05-17-evenement-5.html",
    "2025-06-21-evenement-6.html"
]

# Initialize the Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("homepage.html")

# Helper function to read markdown files, extract the first title, and generate a summary
def read_markdown_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    
    content = []
    event_title = "Titre de l'événement"  # Valeur par défaut si aucun titre n'est trouvé
    in_summary_section = False

    for line in lines:
        # Check if the line starts with '# ' to get the first title as the event title
        if line.startswith("# "):
            event_title = line[2:].strip()  # Remove '# ' and get the rest as title
            in_summary_section = True  # Start collecting summary after the first title
        elif line.startswith("##"):  # Stop collecting at the second title
            break
        elif in_summary_section:
            content.append(line.strip())  # Collect summary lines

    # Convert the collected summary to HTML
    summary = markdown.markdown("\n".join(content), extensions=['extra', 'smarty', 'toc'])
    return event_title, summary

# Parse and sort markdown files, then build the data structure for rendering
events = []

# Sort the markdown files to ensure order matches routerDirectory
markdown_files = sorted([f for f in os.listdir(content_dir) if f.endswith(".md")])

for i, file_name in enumerate(markdown_files):
    # Extract event date from file name
    event_date = "-".join(file_name.split("-")[0:3])
    image_file = f"evenement-{file_name.split('-')[-1].split('.')[0]}.webp"
    
    # Use index `i` to map to the corresponding route in `routerDirectory`
    event_href = routerDirectory[i] if i < len(routerDirectory) else "#"
    
    # Extract the title and a summary of the content for the homepage
    event_title, event_summary = read_markdown_summary(os.path.join(content_dir, file_name))

    # Build the event data dictionary
    event_data = {
        "title": event_title,            # Use extracted title from the markdown file
        "date": event_date,
        "content": event_summary,        # Use summary content
        "image": os.path.join(image_dir, image_file),
        "href": event_href               # Link to the generated event page
    }
    events.append(event_data)

# Render the index.html template with the events data
with open(output_file, "w", encoding="utf-8") as output:
    output.write(template.render(events=events))

print(f"Homepage generated successfully in {output_file}")