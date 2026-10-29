# python-utils-71

A lightweight and high-performance autoclicker built in Python. This tool provides precise mouse automation with configurable intervals and customizable click triggers for desktop applications.

## Features

*   **Configurable CPS:** Fine-tune your clicks-per-second to simulate human-like behavior or maximize task efficiency.
*   **Hotkey Integration:** Start and stop automation instantly using global keyboard shortcuts.
*   **Low Latency Execution:** Built on the `pynput` library to ensure minimal overhead and rapid response times.
*   **Multi-Button Support:** Choose between left, right, and middle mouse button automation.

## Installation

Ensure you have Python 3.8+ installed. Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Developer/python-utils-71.git
cd python-utils-71
pip install -r requirements.txt
```

## Usage

To launch the autoclicker with default settings, execute the main script:

```bash
python main.py --interval 0.1 --button left
```

Once running, use your designated trigger key (default: `F6`) to toggle clicking on and off. You can modify the `config.json` file to save your preferred delay settings and keybindings permanently.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Note: Use this tool responsibly. Excessive or automated clicking in violation of application Terms of Service may result in account restrictions.*