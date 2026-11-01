import time
from typing import Callable, Optional

class OptimizedClickEngine:
    """High-precision autoclicker engine with hybrid timing optimization."""

    def __init__(self, interval_ms: float = 10.0, target_action: Optional[Callable[[], None]] = None):
        self.interval = max(0.0001, interval_ms / 1000.0)
        self.target_action = target_action or self._dummy_action
        self.is_running = False
        self.clicks_performed = 0

    @staticmethod
    def _dummy_action() -> None:
        pass

    def run_burst(self, duration_seconds: float) -> int:
        """Runs click loop using hybrid sleep/busy-wait for low latency precision."""
        self.is_running = True
        self.clicks_performed = 0
        
        start_time = time.perf_counter()
        end_time = start_time + duration_seconds
        next_click = start_time

        while self.is_running and time.perf_counter() < end_time:
            now = time.perf_counter()
            
            if now >= next_click:
                self.target_action()
                self.clicks_performed += 1
                next_click += self.interval

            # Hybrid sleep: sleep for larger gaps, spin-wait for remaining < 2ms
            time_to_wait = next_click - time.perf_counter()
            if time_to_wait > 0.002:
                time.sleep(time_to_wait - 0.001)
            elif time_to_wait > 0:
                pass  # Spin-wait for ultra-precise sub-millisecond dispatch

        self.is_running = False
        return self.clicks_performed

    def stop(self) -> None:
        """Stops the active click burst loop."""
        self.is_running = False
