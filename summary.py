"""Provide a summary of the data in the cer-feeds.json"""

import json
import os
import sys

with open(os.path.join("feeds", "cer-feeds.json"), "r", encoding="UTF-8") as feeds_file:
    data = json.loads(feeds_file.read())


feeds = [
    f"{feed['label']}::{feed['source']}::{feed['status']}::{feed['deviation']}%"
    for feed in data["feeds"]
]

print(json.dumps({"count": len(data["feeds"]), "feeds": feeds}, indent=2))
if len(set(feeds)) != len(feeds):
    print("warning: duplicate data in feed list", file=sys.stderr)
feeds = [(feed["pair"], feed["label"]) for feed in data["feeds"]]
for item in feeds:
    if item[0].upper() == item[1].upper():
        continue
    print(
        f"warning: name and pair for '{item}' may not be configured correctly",
        file=sys.stderr,
    )
