import httpx
from dotenv import load_dotenv
import os

load_dotenv()
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")

async def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """Fetch the current exchange rate between two currencies."""
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            data = response.json()
            if data["result"] == "success":
                rate = data["conversion_rate"]
                return f"Current {base_currency} to {target_currency} exchange rate: {rate}"
            return f"Error fetching rate for {base_currency} to {target_currency}: {data.get('error-type', 'Unknown error')}"
        except Exception:
            return f"Unable to fetch exchange rate data for {base_currency} to {target_currency}."