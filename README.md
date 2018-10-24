# autobahn-autoreconnect

The old project from isra17 was outdated and did not support python3.5 and above.
This is an updated library that supports python3.5 and above.

## DISCLAIMER

This is a modified version of gitub.com/isra17/autobahn-autoreconnect.
We respect the original owner(s) and will not claim ownership of this project.

## Install

```
pip install git+https://github.com/wegroupwolves/autobahn-autoreconnect
```

## Usage

```
from AUTOBAHN_RECONNECT_TODO_LIBRARY import BackoffStrategy, ApplicationRunner

import asyncio

from config import CROSSBAR_REALM, CROSSBAR_IP

from crossbar_connection import Connection

strategy = BackoffStrategy(initial_interval=20, max_interval=40, factor=2)
r = ApplicationRunner(CROSSBAR_IP, CROSSBAR_REALM, retry_strategy=strategy)

if __name__ == "__main__":

    try:

        loop = asyncio.get_event_loop()
        asyncio.ensure_future(r.run(Client), loop=loop)
        loop.run_forever()

    except Exception as e:
        
        print(e)
```
