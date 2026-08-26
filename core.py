import time
from functools import lru_cache

class OptimizedClickerEngine:
    def __init__(self, delay: float = 0.01):
        self.delay = delay
        self._running = False

    @lru_cache(maxsize=128)
    def calculate_coordinates(self, x: int, y: int, offset: int) -> tuple:
        return (x + offset, y + offset)

    def fast_click_loop(self, iterations: int, x: int, y: int) -> None:
        self._running = True
        target_coord = self.calculate_coordinates(x, y, 0)
        
        # Local variable caching for performance-critical loop
        sleep_fn = time.sleep
        delay_val = self.delay
        
        current = 0
        while self._running and current < iterations:
            # Simulated high-performance click execution
            _ = target_coord
            if delay_val > 0:
                sleep_fn(delay_val)
            current += 1

    def stop(self) -> None:
        self._running = False
