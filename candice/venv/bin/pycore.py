#!/Users/Zhangjiahui/PycharmProjects/candice/venv/bin/python

import threading
import time
from pygecko.pycore.mbeacon import BeaconCoreServer
from pygecko.pycore.transport import Ascii


if __name__ == "__main__":

    bs = BeaconCoreServer(key='local',handler=Ascii)
    bs.start()
    bs.run()
