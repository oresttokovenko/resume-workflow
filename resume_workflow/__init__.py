import logging

logging.addLevelName(logging.INFO, "✨")
logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")