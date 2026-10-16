"""Discord webhook helper recycled from the legacy regime-trade alerts."""

from __future__ import annotations

from datetime import datetime, timezone

import httpx


class DiscordNotifier:
    def __init__(self, webhook_url: str = "", *, enabled: bool = True, timeout: float = 10.0):
        self.webhook_url = (webhook_url or "").strip()
        self.enabled = enabled and bool(self.webhook_url)
        self._client = httpx.Client(timeout=timeout)

    def close(self) -> None:
        self._client.close()

    def send_message(self, title: str, lines: list[str] | None = None) -> bool:
        if not self.enabled:
            return False
        content = "\n".join([title, *(line for line in (lines or []) if line)])
        response = self._client.post(self.webhook_url, json={"content": content[:2000]})
        response.raise_for_status()
        return True

    def send_test_message(self, *, exchange_detail: str = "n/a") -> bool:
        return self.send_message(
            "Jesse live test alert",
            [
                f"sent_at={datetime.now(timezone.utc).isoformat()}",
                f"exchange={exchange_detail}",
            ],
        )
