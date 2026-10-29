"""Send a bounded motor command over a serial connection.

The receiving controller must accept newline-terminated ``speed,in1,in2``
commands at 9600 baud. Importing this module never opens a port or moves a motor.
"""

import argparse
import time

from serial import Serial


def send_motor_command(connection, speed, direction):
    """Send a PWM value (0-255) and direction (-1, 0, or 1)."""
    if not 0 <= speed <= 255:
        raise ValueError("speed must be between 0 and 255")
    if direction not in (-1, 0, 1):
        raise ValueError("direction must be -1, 0, or 1")

    in1, in2 = (1, 0) if direction == 1 else (0, 1) if direction == -1 else (0, 0)
    connection.write(f"{speed},{in1},{in2}\n".encode("ascii"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", required=True, help="serial device, for example /dev/ttyACM0")
    parser.add_argument("--speed", required=True, type=int, help="PWM speed from 0 to 255")
    parser.add_argument("--direction", choices=("forward", "reverse"), required=True)
    parser.add_argument("--duration", type=float, default=1.0, help="run time in seconds (default: 1)")
    args = parser.parse_args()

    if not 0 <= args.speed <= 255:
        parser.error("--speed must be between 0 and 255")
    if args.duration <= 0:
        parser.error("--duration must be greater than zero")

    direction = 1 if args.direction == "forward" else -1
    with Serial(args.port, 9600, timeout=1, write_timeout=1) as connection:
        try:
            send_motor_command(connection, args.speed, direction)
            time.sleep(args.duration)
        finally:
            send_motor_command(connection, 0, 0)


if __name__ == "__main__":
    main()
