[![Image](https://i.goopics.net/9jkov2.png)](https://goopics.net/i/9jkov2) 

# Vivre aux Lilas Association Website Generator

This project generates the website for the fictional "Vivre aux Lilas" neighborhood association. It includes a homepage with upcoming events and a bureau page listing the association members. The scripts use Python, Jinja2 for templating, and CSV files for storing member information.

## Contributor name 

Name : Cristelle Almodar  
Name : Tim Moyence

## Stack

- Python
- HTML
- CSS
- Tailwind

## Project Structure

```plaintext

├── atelier1/
│   ├── membres-bureau-association.csv  
│   ├── 2025-01-18-evenement-1.md
│   ├── 2025-02-16-evenement-2.md
│   ├── 2025-03-23-evenement-3.md
│   ├── 2025-04-11-evenement-4.md
│   ├── 2025-05-17-evenement-5.md
│   ├── 2025-06-21-evenement-6.md
│   ├── evenement-1.webp
│   ├── evenement-2.webp
│   ├── evenement-3.webp
│   ├── evenement-4.webp
│   ├── evenement-5.webp
│   ├── evenement-6.webp
│   ├── homepage.png
├── script/                
│   ├── homepage.py               
│   ├── bureau.py               
│   ├── launch_all.py             
│   ├── script.py    
├── templates/                
│   ├── homepage.html         
│   ├── bureau.html
│   ├── event.html           
├── view/                     
│   ├── index.html            
│   ├── bureau.html
│   ├── allEventsName.html
│   ├── ....html
│   ├── style.css
└── README.md                 
```

## Requirements

Ensure you have the following Python packages installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install jinja2 markdown
```

## How to Run the Project

1. **Master Script**: The `script/launch_all.py` script runs all generation scripts in sequence.

### Steps to Run:

1. Run the `script/launch_all.py` script to generate all the necessary pages:

    ```bash
    python3 script/launch_all.py
    ```

2. The output HTML files will be saved in the `view/` directory

3. To run the project run the index.html with Live Server

## CSV File Format

The CSV file (`membres-bureau-association.csv`) must contain the following columns:
- **prénom**: First name of the member.
- **nom**: Last name of the member.
- **email**: Email address of the member.
- **fonction**: Role of the member in the association.

Example CSV content:

```csv
prénom,nom,email,fonction
Alice,Dupont,alice.dupont@example.com,Présidente
Bob,Martin,bob.martin@example.com,Trésorier
```

## Customizing the Templates

You can customize the layout and design of the generated HTML pages by editing the Jinja2 templates located in the `templates/` directory:
- `homepage.html`: Template for the homepage.
- `bureau.html`: Template for the bureau page.
- `event.html`: Template for the events pages.

## License

This project is for educational purposes and is not meant for production use.

