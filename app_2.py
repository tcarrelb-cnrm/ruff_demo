import datetime
from pathlib import Path
import math
from collections import defaultdict
import json
 
def add_numbers(a, b):
    """Add two numbers together."""
    result = a + b
    return result
 
def get_current_time():
    """Get the current time."""
    return datetime.datetime.now()
 
def read_config():
    """Read configuration from a JSON file."""
    config_path = Path("config.json")
    if config_path.exists():
        return json.loads(config_path.read_text())
    return {}
 
def calculate_stats(values):
    """Calculate statistics for a list of values."""
    stats = defaultdict(int)
    stats["sum"] = sum(values)
    stats["average"] = stats["sum"] / len(values)
    stats["sqrt_sum"] = math.sqrt(stats["sum"])
    return stats
 
def process_items(items=[]):  # Bugbear will flag mutable default argument
    """Process a list of items."""
    return [x for x in items for y in items]  # Bugbear will flag nested comprehension
 
x = 10
y = 20
print(add_numbers(x, y))
print(get_current_time())
print(calculate_stats([1, 2, 3, 4, 5]))
