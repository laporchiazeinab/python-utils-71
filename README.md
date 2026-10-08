# python-utils-71

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

`python-utils-71` is a high-precision, multi-threaded autoclicker designed for rapid automation tasks and input testing in Python. Built on top of native system input hooks, it delivers sub-millisecond click execution alongside configurable anti-detection algorithms.

## Features

- **Microsecond Precision Execution**: Multi-threaded click loops capable of reaching up to 1,000 clicks per second with minimal CPU overhead.
- **Human Emulation Mode**: Configurable gaussian jitter for click intervals and pixel coordinates to simulate organic user input.
- **Global Hotkey Intercepts**: Instant toggle controls listening across all active OS windows using native OS-level listeners.
- **Multi-Target Pattern Sequences**: Record and loop coordinate macros with specific click types (Left, Right, Middle, or Double Click).

## Installation

Install the package directly from GitHub using `pip`:

```bash
git clone https://github.com/Developer/python-utils-71.git
cd python-utils-71
pip install -r requirements.txt
python setup.py install
```

## Basic Usage

Run the autoclicker programmatically within your script:

```python
from python_utils_71 import AutoClicker, Button

# Initialize clicker with a 10ms delay and organic jitter
clicker = AutoClicker(
    button=Button.LEFT,
    interval=0.01,
    jitter=0.002,
    toggle_key="f8"
)

# Start background listener for the hotkey
clicker.start()
```

Alternatively, launch the CLI directly:

```bash
python -m python_utils_71 --interval 0.05 --button left --hotkey f8
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.