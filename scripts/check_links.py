#!/usr/bin/env python3
"""Report dead links in data/tools/*.yml.

Status codes 401/403/429 and 5xx are reported as "blocked" (bot protection or login walls), not dead.
Exit code is 1 only when a link is really dead (404/410/DNS failure/timeout on every attempt).
"""
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
HEADERS = {"User-Agent": "Mozilla/5.0 (studie-research link check)"}
SOFT = {401, 403, 429, 999}


def check(url):
    result = "dead"
    for method in ("HEAD", "GET", "GET"):  # second GET retries transient network errors
        try:
            req = urllib.request.Request(url, method=method, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=25) as r:
                return "ok" if r.status < 400 else "dead"
        except urllib.error.HTTPError as e:
            if e.code in SOFT or e.code >= 500:
                result = f"blocked ({e.code})"
            elif method == "GET":
                result = f"dead ({e.code})"
        except Exception as e:
            result = f"dead ({type(e).__name__})"
    return result


def main():
    items = [(p.name, yaml.safe_load(p.read_text())["url"]) for p in sorted((ROOT / "data" / "tools").glob("*.yml"))]
    with ThreadPoolExecutor(max_workers=12) as pool:
        results = list(pool.map(lambda it: check(it[1]), items))
    dead = [(n, u, r) for (n, u), r in zip(items, results) if r.startswith("dead")]
    blocked = [(n, u, r) for (n, u), r in zip(items, results) if r.startswith("blocked")]
    for n, u, r in blocked:
        print(f"BLOCKED {r}: {n} {u}")
    for n, u, r in dead:
        print(f"DEAD {r}: {n} {u}")
    print(f"{len(items)} links: {len(items) - len(dead) - len(blocked)} ok, {len(blocked)} blocked, {len(dead)} dead")
    return 1 if dead else 0


if __name__ == "__main__":
    sys.exit(main())
