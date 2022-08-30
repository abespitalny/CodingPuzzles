import socket, sched, time, json, select, threading, pyvisa, asyncio

class PowerSupply:
    SCPI_READ = "MEAS:CURR:DC?;MEAS:VOLT:DC?"
    SCPI_SET = "CURR {};VOLT {};OUTP:{}"

    def __init__(self, instrument):
        self._instrument = instrument
        self._voltage = 0
        self._current = 0
        self._enabled = False
        self._set_current = 0
        self._set_voltage = 0
 
    def read(self):
        measurement = self._instrument.query(self.SCPI_READ)
        current, voltage = measurement.split(",")
        self._current = float(current)
        self._voltage = float(voltage)

    def set(self, current, voltage, enabled):
        self._instrument.write(self.SCPI_SET.format(current, voltage, "START" if enabled else "STOP"))
        self._set_current = current
        self._set_voltage = voltage
        self._enabled = enabled

    @property
    def voltage(self):
        return self._voltage

    @property
    def current(self):
        return self._current

    @property
    def enabled(self):
        return self._enabled
    
    @property
    def set_current(self):
        return self._set_current

    @property
    def set_voltage(self):
        return self._set_voltage

class TelemetryClient:
    def __init__(self, conn):
        self._conn = conn

    async def send(self, payload):
        self._conn.sendall(payload)

class Driver:
    BUFFER_SIZE = 4096

    def __init__(self, power_supply, command_clients, broadcast_rate, read_rate):
        self._power_supply = power_supply
        self._command_clients = command_clients
        self._broadcast_rate = broadcast_rate
        self._read_rate = read_rate
        self._power_supply_lock = threading.Lock()
        self._telemetry_lock = threading.Lock()
        self._telemetry_clients = []

    async def broadcast(self):
        while True:
            time.sleep(self._broadcast_rate)

            payload = {
                "current": self._power_supply.current,
                "voltage": self._power_supply.voltage,
                "set_current": self._power_supply.set_current,
                "set_voltage": self._power_supply.set_voltage,
                "enabled": self._power_supply.enabled
            }

            payload = json.dumps(payload).encode("utf-8")
            with self._telemetry_lock:
                send_tasks = [client.send(payload) for client in self._telemetry_clients]

            await asyncio.gather(*send_tasks)

    def poll(self):
        while True:
            rlist, _, _ = select.select(self._command_clients, [], [])

            with self._power_supply_lock:
                for sock in rlist:
                    payload = json.loads(sock.recv(self.BUFFER_SIZE).decode("utf-8"))
                    self._power_supply.set(payload["set_current"], payload["set_voltage"], payload["enabled"])

    def read(self):
        while True:
            time.sleep(self._read_rate)

            with self._power_supply_lock:
                self._power_supply.read()

    def run_driver(self, host, port):
        # Start broadcast thread
        broadcast_thread = threading.Thread(target=self.broadcast)
        broadcast_thread.start()

        # Start command thread
        command_thread = threading.Thread(target=self.poll)
        command_thread.start()

        # Start read thread
        read_thread = threading.Thread(target=self.read)
        read_thread.start()

        # Listen for connections from telemetry clients.
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen()

        while True:
            client_sock, _ = sock.accept()

            # Use lock when adding new telemetry client to broadcast list
            # because the list is shared by the broadcast thread.
            with self._telemetry_lock:
                self._telemetry_clients.append(TelemetryClient(client_sock))


def main():
    rm = pyvisa.ResourceManager("@sim")
    instrument = rm.open_resource("ASRL1::INSTR", read_termination="\n", baud_rate=9600)

    power_supply = PowerSupply(instrument)
    command_clients = []
    driver = Driver(power_supply, command_clients, 0.1, 5)
    driver.run_driver()

if __name__ == "__main__":
    main()
