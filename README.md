# python-utils-71

A high-performance, cross-platform autoclicker library and CLI tool built with Python. Designed for automation tasks, testing, and repetitive workflows, it provides low-latency input simulation with minimal resource overhead.

## Features

*   **Precision Control:** Configurable click intervals (milliseconds) and mouse button selection (left, right, middle).
*   **Dynamic Targeting:** Supports both coordinate-based clicking and instant "follow-cursor" automation modes.
*   **Safety Interlocks:** Includes an emergency keyboard hotkey to instantly kill automation processes if needed.
*   **Cross-Platform:** Built on top of `pynput` for seamless operation across Windows, macOS, and Linux.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-71.git
cd python-utils-71
pip install -r requirements.txt
```

## Usage

You can run the autoclicker directly via the command line or import it into your own scripts.

### CLI Execution
Run the script with default settings (100ms interval):
```bash
python main.py --interval 100 --button left
```

### Python API Example
```python
from utils import AutoClicker

# Initialize with a 50ms delay
bot = AutoClicker(interval=0.05)

# Start clicking at the current cursor position
bot.start()

# Stop after 10 seconds
import time
time.sleep(10)
bot.stop()
```

## Contributing
Contributions are welcome! Please open an issue to discuss major changes before submitting a pull request. Ensure all new code passes existing unit tests.

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.