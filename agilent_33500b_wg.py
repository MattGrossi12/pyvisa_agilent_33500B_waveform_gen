#!/usr/bin/env python3
import pyvisa

IP = "10.128.16.126"
PORT = 5025
TIMEOUT_MS = 5000
CHANNEL = 1

FREQUENCY_HZ = 2_000_000
HIGH_LEVEL_V = 3.3
LOW_LEVEL_V = 0.0
DUTY_CYCLE_PCT = 50.0


def open_waveform_generator(ip: str = IP, port: int = PORT):
    """Open a raw SCPI socket connection to the Agilent 33500B/33522B."""

    rm = pyvisa.ResourceManager("@py")
    wg = rm.open_resource(f"TCPIP0::{ip}::{port}::SOCKET")
    wg.timeout = TIMEOUT_MS
    wg.write_termination = "\n"
    wg.read_termination = "\n"
    return rm, wg


def check_errors(wg):
    """Read and return all pending SCPI errors."""

    errors = []
    while True:
        err = wg.query("SYST:ERR?").strip()
        errors.append(err)
        if err.startswith('+0') or err.startswith('0'):
            break
    return errors



def configure_clock(
    wg,
    channel: int = CHANNEL,
    frequency_hz: float = FREQUENCY_HZ,
    high_level_v: float = HIGH_LEVEL_V,
    low_level_v: float = LOW_LEVEL_V,
    duty_cycle_pct: float = DUTY_CYCLE_PCT,
) -> None:
    """Configure a 0 V to 3.3 V square-wave clock on the selected channel."""

    source = f"SOUR{channel}"
    output = f"OUTP{channel}"

    wg.write("*CLS")

    # Note: this model accepts the waveform/output commands below,
    # but does not require SYST:REM for raw socket control.
    # Using SYST:REM on this instrument generates -113 Undefined header.
    wg.write(f"{output}:LOAD INF")
    wg.write(f"{source}:FUNC SQU")
    wg.write(f"{source}:FREQ {frequency_hz}")
    wg.write(f"{source}:FUNC:SQU:DCYC {duty_cycle_pct}")
    wg.write(f"{source}:VOLT:HIGH {high_level_v}")
    wg.write(f"{source}:VOLT:LOW {low_level_v}")
    wg.write(f"{output} ON")



def main() -> None:
    rm, wg = open_waveform_generator()

    try:
        print("Instrument:", wg.query("*IDN?").strip())

        configure_clock(wg)

        print("Clock configurado com sucesso.")
        print(f"Frequência : {FREQUENCY_HZ} Hz")
        print(f"Nível alto : {HIGH_LEVEL_V} V")
        print(f"Nível baixo: {LOW_LEVEL_V} V")
        print(f"Duty cycle : {DUTY_CYCLE_PCT} %")

        errors = check_errors(wg)
        for idx, err in enumerate(errors, start=1):
            print(f"SCPI error {idx}: {err}")
    finally:
        wg.close()
        rm.close()


if __name__ == "__main__":
    main()
