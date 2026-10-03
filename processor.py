import time
import urllib.request
import urllib.error
import json
import logging

logger = logging.getLogger("autoclicker.processor")

class NetworkProcessor:
    """Handles network requests for autoclicker configurations with retry logic."""

    def __init__(self, max_retries: int = 3, backoff_factor: float = 2.0):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor

    def fetch_remote_profile(self, url: str) -> dict:
        """
        Retrieves a clicking coordinate profile configuration from a remote endpoint.
        Applies exponential backoff for handling intermittent connection failures.
        """
        delay = 1.0
        for attempt in range(1, self.max_retries + 1):
            try:
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "Autoclicker-Processor/1.0"}
                )
                with urllib.request.urlopen(req, timeout=5.0) as response:
                    if response.status == 200:
                        return json.loads(response.read().decode("utf-8"))
            except (urllib.error.URLError, urllib.error.HTTPError) as err:
                logger.warning("Attempt %d failed for url %s: %s", attempt, url, err)
                if attempt == self.max_retries:
                    logger.error("Max retries reached. Network operation failed.")
                    raise err
                
                time.sleep(delay)
                delay *= self.backoff_factor
        
        return {}
