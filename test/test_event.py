import os

def test_event_pages_exist():
    expected_files = [
        "2025-01-18-evenement-1.html",
        "2025-02-16-evenement-2.html",
        "2025-03-23-evenement-3.html"
    ]
    for filename in expected_files:
        assert os.path.exists(os.path.join("wwwroot", filename)), f"Expected event page {filename} not found in view/"

def test_event_page_titles():
    with open("wwwroot/2025-01-18-evenement-1.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "Fête des voisins - Samedi 18 janvier 2025" in content, "Expected event title not found in the first event page."

    with open("wwwroot/2025-02-16-evenement-2.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "Atelier de jardinage urbain - Dimanche 16 février 2025" in content, "Expected event title not found in the second event page."


def test_event_images():
    with open("wwwroot/2025-01-18-evenement-1.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "./atelier1/evenement-1.webp" in content, "Expected image reference not found in the first event page."


def test_common_layout_elements_in_event_page():
    with open("wwwroot/2025-03-23-evenement-3.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "./index.html" in content, "Expected link to index.html not found in event page."
    assert "./bureau.html" in content, "Expected link to bureau.html not found in event page."
    assert "<footer>" in content and "</footer>" in content, "Footer element is missing from the event page."
