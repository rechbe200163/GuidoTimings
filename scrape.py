import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time  # Importiere das time-Modul

# URL der Webseite mit den Bildern
website_url = "https://www.wagenradl.at"  # Ändere dies entsprechend

# Füge einen Benutzer-Agenten-Header hinzu
headers = {
    'User-Agent':
    'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'}

# Hole den HTML-Inhalt der Webseite
response = requests.get(website_url, headers=headers)
response.raise_for_status()

# Verwende BeautifulSoup, um den HTML-Inhalt zu analysieren
soup = BeautifulSoup(response.content, "html.parser")

# Extrahiere alle Bild-Elemente (zum Beispiel <img>) und ihre Quell-URLs
img_elements = soup.find_all("img")
image_urls = [urljoin(website_url, img["src"]) for img in img_elements]

# Download und speichere jedes Bild
for i, url in enumerate(image_urls, 1):
    # Füge eine Pause zwischen den Anfragen ein, um Rate-Limits zu respektieren
    time.sleep(1)  # Hier wartest du 1 Sekunde zwischen den Anfragen

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # Extrahiere den Dateinamen aus der URL und speichere das Bild
    filename = f"picture_{i}.jpg"
    with open(filename, "wb") as file:
        file.write(response.content)

    print(f"Picture {i} downloaded successfully.")
