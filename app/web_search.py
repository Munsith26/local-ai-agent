import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def web_search(query: str):

    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=5,
        )

        results = response.get("results", [])

        if not results:
            return "No search results found."

        text = ""

        for item in results:
            text += f"Title: {item['title']}\n"
            text += f"Content: {item['content']}\n"
            text += f"URL: {item['url']}\n\n"

        return text

    except Exception as e:
        return f"Web Search Error: {str(e)}"