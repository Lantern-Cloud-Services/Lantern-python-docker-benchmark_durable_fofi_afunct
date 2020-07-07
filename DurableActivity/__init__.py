import logging

def main(activity: str):
    logging.warning(f"Activity Triggered: {activity}")

    base = activity["base"]
    exp = activity["exp"]
    return base**exp