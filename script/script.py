import markdown
import os

def convert_md_to_html(input_file, output_file):
    # Vérifier si le fichier d'entrée est un fichier Markdown
    if not input_file.endswith(".md"):
        print(f"{input_file} n'est pas un fichier Markdown.")
        return

    try:
        # Lire le fichier Markdown
        with open(input_file, 'r', encoding='utf-8') as md_file:
            text = md_file.read()

        # Convertir le texte Markdown en HTML
        html = markdown.markdown(text)

        # Écrire le résultat dans un fichier HTML
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html)

        print(f"Conversion réussie : {output_file}")
    except FileNotFoundError:
        print(f"Le fichier {input_file} n'a pas été trouvé.")

if __name__ == "__main__":
    # Exemple d'utilisation
    input_md = "./atelier1/2025-01-18-evenement-1.md"
    output_html = "./view/index.html"

    convert_md_to_html(input_md, output_html)