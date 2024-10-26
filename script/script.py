import markdown
import os

# Helper function to convert Markdown to HTML
def convert_md_to_html(input_file, output_file):
    if not input_file.endswith(".md"):
        print(f"{input_file} n'est pas un fichier Markdown.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            text = md_file.read()

        html = markdown.markdown(text)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html)

        print(f"The file : {output_file} has been converted successfully.")
    except FileNotFoundError:
        print(f"File {input_file} not found.")

def process_event(input_md, output_html):
    convert_md_to_html(input_md, output_html)

# Convert files
if __name__ == "__main__":
    events = [
        ("./atelier1/2025-01-18-evenement-1.md", "./view/2025-01-18-evenement-1.html"),
        ("./atelier1/2025-02-16-evenement-2.md", "./view/2025-02-16-evenement-2.html"),
        ("./atelier1/2025-03-23-evenement-3.md", "./view/2025-03-23-evenement-3.html"),
        ("./atelier1/2025-04-11-evenement-4.md", "./view/2025-04-11-evenement-4.html"),
        ("./atelier1/2025-05-17-evenement-5.md", "./view/2025-05-17-evenement-5.html"),
        ("./atelier1/2025-06-21-evenement-6.md", "./view/2025-06-21-evenement-6.html")
    ]

    for input_md, output_html in events:
        process_event(input_md, output_html)