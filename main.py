from mcp.server.fastmcp import FastMCP
from services.weather_api import  get_forecast as weather_forecast
from services.exchange_api import get_exchange_rate as exchange_rate
from services.serper_api import get_news_summary as news_summary

mcp = FastMCP("weather_exchange_news")

@mcp.tool()
async def get_forecast(city: str) -> str:
    """Get current weather forecast for a city anywhere in the world.

    Args:
        city: Name of the city (e.g., Moscow, London)
    """
    return await weather_forecast(city)

@mcp.tool()
async def get_exchange_rate(base_currency: str, target_currency: str) -> str:
    """Get the current exchange rate between two currencies.

    Args:
        base_currency: The base currency code (e.g., USD, EUR)
        target_currency: The target currency code (e.g., RUB, JPY)
    """
    return await exchange_rate(base_currency, target_currency)

@mcp.tool()
async def get_news(topic: str) -> str:
    """Get news summary for a specified topic over the last 7 days using Serper."""
    return await news_summary(topic)

if __name__ == "__main__":
   
    mcp.run(transport="stdio")