import asyncio
import motor.motor_asyncio
import logging

import requests
from fastapi import FastAPI
from requests.exceptions import SSLError

app = FastAPI()
logger = logging.getLogger(__name__)


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://mongo:27017")
db = client["html_cache"]
collection = db["pages"]


def parse_html(url):
    try:
        response = requests.get(url)
        return response.text
    except SSLError:
        logger.warning("Could not parse this url")
    except Exception as exc:
        context = {"exc": exc.args}
        msg = "Error while parsing site: %(exc)s"
        logger.error(msg, context)


async def cache_html(url, html):
    try:
        await collection.update_one({"url": url}, {"$set": {"html": html}}, upsert=True)
    except Exception as exc:
        logger.error(exc.args)


async def fetch_html(url):
    cached_result = await collection.find_one({"url": url})
    if cached_result:
        print("Cache used")
        return url, cached_result["html"]

    print("No cache")
    html = parse_html(url)
    asyncio.create_task(cache_html(url, html))
    return url, html


@app.post("/parse")
async def parse_urls(urls: list[str]):
    tasks = [fetch_html(url) for url in urls]
    results = await asyncio.gather(*tasks)

    response = {url: html for url, html in results}
    return response
