### Steps

- Create a very simple _streamlit_ user interface.
- Accept a website URL as input from the user.
- When the user clicks a button, trigger the scraping process.
- Use **Selenium** to open the website and grab the HTML content.
- Parse the HTML using **Beautiful Soup**.
- Extract the `<body>` content from the HTML.
- Clean the extracted content by removing `<script>` and `<style>` tags.
- Display the cleaned text content in the Streamlit app.
- (Optional) Pass the cleaned content **in batches** (especially for big sites, because we have limited tokens about 8000 chars) to an LLM for further analysis or summarization.

## Selenium:

- Allows us to automate browsers so we can actually navigate to a webpage.
- Grab all of the content that's on that page then we could do some filtering on it.
- And we could pass them into an LLM.
- We can use that LLM to actually parse through the data and give us some meaningful response.

## Cleaning up DOM Content

- We dont wanna pass the script and styles to the LLMs
- So we can reduce the amount of the characters or batches that we consume minimum tokens possible
