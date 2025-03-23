import httpx
from dotenv import load_dotenv
import os


load_dotenv()
SERPER_API_KEY = os.getenv("SERPER_API_KEY")


async def get_news_summary(topic: str) -> str:
    """Fetch news summary for a specified topic over the last 7 days using Serper (Google Search)."""
    url = "https://google.serper.dev/news"
    headers = {
        "X-API-KEY": SERPER_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "q": topic,
        "tbs": "qdr:w",  # Фильтр: новости за последнюю неделю (7 дней)
        "num": 10  # Результат количества выводимых ограничен до 10
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=headers, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            news_items = data.get("news", [])
            if not news_items:
                return "No news found for this topic in the last 7 days."
            news_list = [f"{item['title']} - {item['link']}" for item in news_items[:5]]
            return "\n---\n".join(news_list)
        except httpx.HTTPStatusError as e:
            return f"Error fetching news from Serper: {e.response.status_code} - {e.response.text}"
        except Exception as e:
            return f"Unable to fetch news data: {str(e)}"