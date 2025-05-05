# 🕵️ NetStalker

**NetStalker** is a lightweight OSINT (Open Source Intelligence) tool written in Python. It helps you perform simple digital footprinting and reconnaissance by automating Google Dorking and checking for username presence across popular social media platforms.

Built for cybersecurity awareness, CTFs, and investigative learning.

---

#✨ Features

- 🔍 Google Dorking (LinkedIn, Instagram, etc.)
- 📱 Username presence lookup across:
  - Twitter
  - Instagram
  - Facebook
  - LinkedIn
- 💻 CLI-based interface, easy to run
- 🧱 Modular and extensible code (great for students & hackers)

---

# 🚀 How to Use

1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/netstalker.git
   cd netstalker


2. **Install required packages**

   ```bash
   pip install requests googlesearch-python
   ```

3. **Run the tool**

   ```bash
   python netstalker.py
   ```

---

🧪 Example Output

```text
Enter the person's name: Diprit Turul

[+] Searching Google for: Diprit Turul site:linkedin.com
[+] https://www.linkedin.com/in/diprit-turul

[+] Searching Google for: Diprit Turul site:instagram.com
[+] https://www.instagram.com/diprit.turul

Enter a username to check social media: diprit.turul

[+] Checking social media for: diprit.turul
[+] Possible profile found on Instagram: https://instagram.com/diprit.turul
[-] No profile found on Facebook
[+] Possible profile found on Twitter: https://twitter.com/diprit.turul
[-] No profile found on LinkedIn
```

---

# ⚙️ Dependencies

* Python 3.7 or higher
* [`requests`](https://pypi.org/project/requests/)
* [`googlesearch-python`](https://pypi.org/project/googlesearch-python/)

> 💡 Tip: If you're getting `TypeError: search() got an unexpected keyword argument`, make sure you've installed the correct version with:
>
> ```bash
> pip install googlesearch-python
> ```

---

# ⚠️ Disclaimer

> **NetStalker is intended strictly for educational and ethical use only.**

By using this tool, you agree to the following:

* ✅ You will use it only for legal and authorized purposes.
* ❌ You will **not** use this tool for harassment, stalking, surveillance, or data misuse.
* ⚖️ You understand the legal implications of OSINT and digital reconnaissance.
* 🧑‍⚖️ The author assumes **no responsibility for misuse** or damage caused by this tool.

If you're using this for penetration testing or red teaming, always get **written permission** from the system owner.

---

# 📌 Roadmap

* [ ] Add DuckDuckGo/Bing scraping fallback
* [ ] Result export to CSV/JSON
* [ ] Advanced CLI arguments using `argparse`
* [ ] Simple GUI with Flask or Streamlit

---

# 🧠 Why NetStalker?

Because learning how data travels across the internet makes you a smarter, safer, and more powerful netizen. Whether you're into ethical hacking, digital privacy, or CTFs — NetStalker is a great starting point.

---

# 👨‍💻 Author

Made with ☕ and Python by **Diprit**



