# 🕸️ AI-Powered Web Scraper with Streamlit + Selenium + LangChain

This project is a **simple AI-driven web scraping tool** that lets you:

- Input a website URL
- Scrape the page content using **Selenium**
- Clean and extract meaningful text with **BeautifulSoup**
- (Optionally) send the content to an **LLM** (via LangChain + Ollama) for summarization or analysis

It’s perfect for exploring website content, generating summaries, or extracting insights while minimizing token usage.

## ✨ Features

- ✅ **Streamlit UI** – simple web interface for user input
- ✅ **Selenium Automation** – loads dynamic websites (not just static HTML)
- ✅ **BeautifulSoup Parsing** – extracts `<body>` content for processing
- ✅ **DOM Cleaning** – removes `<script>` and `<style>` to reduce noise
- ✅ **Token-Efficient** – splits content into batches before sending to LLM
- ✅ **LLM Integration** – works with **LangChain** + **Ollama** to analyze or summarize scraped data

## 📦 Requirements

Install the dependencies from `requirements.txt`:

```txt
streamlit         # Web app framework
langchain         # LLM application framework
langchain_ollama  # Ollama integration for LangChain
selenium          # Browser automation for web scraping
beautifulsoup4    # HTML/XML parsing for web scraping
lxml              # Fast XML and HTML parsing
html5lib          # Pure Python HTML parser
python-dotenv     # Load environment variables from .env files
```

## 📦 Installation

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## 🛠️ How It Works

### 1️⃣ Streamlit UI

- Accepts a website URL from the user
- Button click triggers the scraping process

### 2️⃣ Selenium Scraper

- Opens the target page in a **headless browser**
- Captures the full HTML content (including dynamic elements)

### 3️⃣ BeautifulSoup Parser

- Extracts the `<body>` content
- Removes `<script>` and `<style>` tags
- Produces a **clean text-only output**

### 4️⃣ Cleaned Output

- Displays the extracted content in the UI
- _(Optional)_ Sends cleaned text to an **LLM** for summarization/analysis

---

## 🧠 LLM Processing

When using **LangChain + Ollama** integration:

- Content is **split into batches** (to stay within token limits)
- Each batch is sent to the LLM
- Responses are combined into a single result

This is great for:

- 📝 **Summarizing long pages**
- 📊 **Extracting structured insights**
- 📑 **Generating reports from web data**

## 🚀 Example Workflow

- Run the app:
  ```bash
  streamlit run app.py
  ```
- Enter a website URL (e.g., https://example.com)
- Click Scrape
  - Selenium fetches the page
  - BeautifulSoup parses and cleans it
- View the extracted text right in the browser
- (Optional) Click Analyze to pass the content to an LLM

## 📊 Architecture(High-level)

```mermaid
flowchart LR
    A[User Input (Streamlit)] --> B[Selenium: Fetch HTML]
    B --> C[BeautifulSoup: Parse & Clean]
    C --> D[Cleaned Text Output]
    D -->|Optional| E[LangChain + Ollama: Analyze / Summarize]
    E --> F[Display Results in UI]
```

## 💡 Future Improvements

- 🛑 Bypass anti-bot mechanisms or CAPTCHA handling (via services like 2Captcha or Playwright stealth mode)
- 🌐 Multi-page crawling support
- 🛡️ Better error handling (timeouts, blocked pages)
- 🗄️ Caching for previously visited URLs
- 🤖 Multiple LLM support (OpenAI, Claude, etc.)
