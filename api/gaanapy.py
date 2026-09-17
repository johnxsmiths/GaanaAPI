import asyncio
import aiohttp
from api.songs.songs import Songs
from api.albums.albums import Albums
from api.artists.artists import Artists
from api.trending.trending import Trending
from api.newreleases.newreleases import NewReleases
from api.charts.charts import Charts
from api.playlists.playlists import Playlists
from api import endpoints
from api.functions import Functions
from api.errors import Errors

class GaanaPy(Songs, Albums, Artists, Trending, NewReleases, Charts, Playlists):
    def __init__(self):
        self._aiohttp = None
        self.api_endpoints = endpoints
        self.functions = Functions()
        self.errors = Errors()

    @property
    def aiohttp(self) -> aiohttp.ClientSession:
        if self._aiohttp is None or self._aiohttp.closed:
            self._aiohttp = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=30)
            )
        return self._aiohttp

    @aiohttp.setter
    def aiohttp(self, session: aiohttp.ClientSession):
        self._aiohttp = session

    async def _safe_request(self, method: str, url: str, **kwargs) -> dict:
        try:
            session = self.aiohttp
            if method == "GET":
                response = await session.get(url, **kwargs)
            else:
                response = await session.post(url, **kwargs)
            if response.status != 200:
                return await self.errors.no_results()
            result = await response.json()
            if not isinstance(result, dict):
                return await self.errors.no_results()
            return result
        except (aiohttp.ClientError, asyncio.TimeoutError, ValueError, TypeError):
            return await self.errors.no_results()

