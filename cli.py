#!/usr/bin/env python3

import fire
from db import initialize_db

if __name__ == "__main__":
    fire.Fire(initialize_db)
