import requests
from googlesearch import search
from bs4 import BeautifulSoup
import time
import pyfiglet

# User-Agent header for requests
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}

def google_dorking(query):
    print(f"\n[+] Searching Google for: {query}\n")
    try:
        results = list(search(query, num=5))  # fixed: num_results -> num
        for result in results:
            print(f"[+] {result}")
            time.sleep(1)  # prevent rapid-fire requests
        return results
    except Exception as e:
        print(f"[-] Error during Google search: {e}")
        return []

def social_media_lookup(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
    }

    print(f"\n[+] Checking social media for: {username}\n")
    for platform, url in platforms.items():
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code == 200:
                print(f"[+] Possible profile found on {platform}: {url}")
            else:
                print(f"[-] No profile found on {platform} (Status code: {response.status_code})")
        except requests.RequestException as e:
            print(f"[-] Error checking {platform}: {e}")
        time.sleep(1)  # respect rate limits

def reverse_image_search(image_path):
    print("\n[+] Use these links for manual reverse image search:")
    print("Google Images: https://images.google.com")
    print("Yandex: https://yandex.com/images/")
    print("PimEyes: https://pimeyes.com/en")
    print(f"[+] Upload the image ({image_path}) to the above platforms to find matches.")

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("NetStalker")
    print(ascii_banner)
    try:
        person_name = input("Enter the person's name: ")
        google_dorking(f"{person_name} site:linkedin.com")
        google_dorking(f"{person_name} site:instagram.com")

        username = input("Enter a username to check social media: ")
        social_media_lookup(username)

        image_path = input("Enter the path to the image for reverse search (or press Enter to skip): ")
        if image_path.strip():
            reverse_image_search(image_path.strip())
    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user.")
