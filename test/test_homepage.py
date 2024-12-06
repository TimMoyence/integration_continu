import os

def test_index_html_exists():
    assert os.path.exists("wwwroot/index.html"), "The index.html file was not generated."


def test_index_html_content():
    with open("wwwroot/index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "<title>Association de quartier</title>" in content, "The homepage title is missing."
    assert "Bienvenue sur le site de l'association" in content, "Expected welcome text not found."

def test_event_images_exist():
    with open("wwwroot/index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # Check if the logo is referenced and if it exists
    assert "./atelier1/logo.png" in content, "Logo image reference not found in index.html"
    assert os.path.exists("atelier1/logo.png"), "Logo image file is missing from atelier1 directory"
