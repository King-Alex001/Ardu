#!/usr/bin/env python3

from __future__ import annotations

import os
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    os.chdir(root)

    host = "127.0.0.1"
    port = 8000
    url = f"http://{host}:{port}/"

    print(f"Serving {root} at {url}")
    webbrowser.open(url)

    server = ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()