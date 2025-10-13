# 🧩 Regular Expressions & Web Scraping in Python

---

## 🔹 1. Regular Expressions (RegEx)

Regular Expressions (or **RegEx**) are powerful tools for **pattern matching**, **searching**, and **text manipulation** in Python.

### Basic Syntax

| Pattern | Meaning |
|----------|----------|
| `[abc]` or `[A-Z]` | Match any single character in the set |
| `[^abc]` | Match any character **except** a, b, or c |
| `.` | Any character (except newline) |
| `\d` | Digit (0–9) |
| `\w` | Word character (letters, digits, `_`) |
| `\s` | Whitespace (space, tab, newline) |
| `*` | Zero or more occurrences |
| `+` | One or more occurrences |
| `?` | Zero or one occurrence — also used to make a pattern *lazy* |
| `{n}` | Exactly `n` repetitions |
| `{n,m}` | Between `n` and `m` repetitions |
| `^` | Start of string/line |
| `$` | End of string/line |
| `()` | Grouping or capturing |
| `\t` | Tab character |
| `\n` | Newline |
| `\r` | Carriage return |

> ⚠️ **Note:** Regex is *greedy* by default.  
> Use `?` to make it *lazy* (for example, `.+?` instead of `.+`).

### Common RegEx Functions in Python

```python
import re

text = "My number is 09123456789 and my name is Alireza."

# Find all matches
numbers = re.findall(r'\d+', text)
print(numbers)  # ['09123456789']

# Search for the first match
match = re.search(r'Alireza', text)
print(match.group())  # Alireza

# Replace with another string
cleaned = re.sub(r'\d+', '[hidden number]', text)
print(cleaned)
```
## 🔹 2. Requests Library

**The requests library is the standard Python package for making HTTP requests — useful for web scraping, APIs, and automation.**

**Installation**
```Text
pip install requests
```

#### Example
```python
import requests

r = requests.get("https://www.google.com")
print(r.status_code)  # 200 means OK
print(r.text[:200])   # Preview the HTML content
```
## 🔹 3. Beautiful Soup (HTML Parsing)

**BeautifulSoup helps parse and extract data from HTML or XML pages easily.
You can combine it with requests for powerful web scraping.**

### Installation
```text
pip install beautifulsoup4
pip install lxml
```
#### Example
```python
from bs4 import BeautifulSoup
import requests
import re

# Get the HTML content
r = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

# Parse it using BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")

# Find an element by tag and class
val = soup.find('h2', attrs={'class': 'headerlink'})

# Clean the text using regex
cleaned_text = re.sub(r'\s+', ' ', val.text).strip()
print(cleaned_text)
```
### More Useful Selectors
```python
# Select by tag
soup.select('p')

# Select by class
soup.select('.class-name')

# Select by id
soup.select('#id-name')

# Nested selection
soup.select('div > span')

# Multiple element types
soup.select('h1, h2, h3')
```
## 🔹 4. Quick Tips

**🧠 Always check your target page with Inspect Element → Copy Selector → Use it in soup.select().**

**⚙️ Use regex101.com to test and learn regex patterns interactively.**

**🕵️‍♂️ For pages with JavaScript-generated content, use Selenium or Playwright instead of BeautifulSoup.**

## ✅ Summary:

**With re, requests, and BeautifulSoup, you can:**

* Extract structured data from unstructured pages

* Automate repetitive web tasks

* Clean and analyze raw HTML text
