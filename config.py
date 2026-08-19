import os

class Config:
    def __init__(self):
        self.click_interval = 0.1  # Interval between clicks
        self.click_duration = 10    # Duration to click
        self.click_button = 'left'   # Which mouse button to click
        self.output_file = 'click_log.txt'  # Log file for clicks
        self.load_env_variables()  # Load any overriding settings

    def load_env_variables(self):
        # Override the config with environment variables if they exist
        self.click_interval = float(os.getenv('CLICK_INTERVAL', self.click_interval))
        self.click_duration = int(os.getenv('CLICK_DURATION', self.click_duration))
        self.click_button = os.getenv('CLICK_BUTTON', self.click_button)
        self.output_file = os.getenv('OUTPUT_FILE', self.output_file)

    def __str__(self):
        return f'Config(click_interval={self.click_interval}, click_duration={self.click_duration}, click_button={self.click_button}, output_file={self.output_file})'

config = Config()