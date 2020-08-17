from subprocess import Popen, PIPE, STDOUT

class PyTrip:
    """Helper object to start, monitor and disconnect JackTrip"""

    def __init__(self, params):
        print(params)
        self.ip = params["ip"]
        self.hub_mode = params["hub_mode"]
        self.server = params["server"]
        self.channels = "-n" + params["channels"]
        self.queue = "-q" + params["queue"]
        self.current_jacktrip = None
        self.connected = False

    def start(self):
        """Start JackTrip with relevent parameters"""

        command = ["jacktrip", "-C", self.ip, self.channels, self.queue, "-z"]

        self.current_jacktrip = Popen(command,
                                      stdout=PIPE,
                                      stderr=STDOUT)

    def stop(self):
        """Stop JackTrip"""
        self.current_jacktrip.terminate()
        self.current_jacktrip.wait()