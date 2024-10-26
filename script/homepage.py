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

# Helper function to read markdown files and extract summary content
def read_markdown_summary(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()
    
    # Variables to store extracted summary content
    collected_content = []
    in_summary_section = False

    # Collect lines until the second title (##) as a summary
    for line in content:
        if line.startswith("##"):  # Stop at the second title
            break
        if line.startswith("# "):  # Start collecting after the first title
            in_summary_section = True
            continue
        if in_summary_section:
            collected_content.append(line.strip())  # Collect summary lines

    # Join the collected lines and convert them to HTML
    summary = "\n".join(collected_content).strip()
    return markdown.markdown(summary)

# Parse and sort markdown files, then build the data structure for rendering
events = []

# Sort the markdown files to ensure order matches routerDirectory
markdown_files = sorted([f for f in os.listdir(content_dir) if f.endswith(".md")])

for i, file_name in enumerate(markdown_files):
    # Extract event details from file names and markdown content
    event_date = file_name.split("-")[0:3]  # Extract date
    event_title = file_name.split("-")[3].replace("_", " ").title()
    image_file = f"evenement-{file_name.split('-')[-1].split('.')[0]}.webp"
    
    # Use index `i` to map to the corresponding route in `routerDirectory`
    event_href = routerDirectory[i] if i < len(routerDirectory) else "#"
    
    # Extract a summary of the content for the homepage
    event_summary = read_markdown_summary(os.path.join(content_dir, file_name))

    # Build the event data dictionary
    event_data = {
        "title": event_title,
        "date": "-".join(event_date),
        "content": event_summary,  # Use summary content
        "image": os.path.join(image_dir, image_file),
        "href": event_href  # Link to the generated event page
    }
    events.append(event_data)

# Render the index.html template with the events data
with open(output_file, "w", encoding="utf-8") as output:
    output.write(template.render(events=events))

print(f"Homepage generated successfully in {output_file}")