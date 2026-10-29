import pytest

from motor import send_motor_command


class FakeConnection:
    def __init__(self):
        self.written = []

    def write(self, data):
        self.written.append(data)


@pytest.mark.parametrize(
    ("speed", "direction", "expected"),
    [(80, 1, b"80,1,0\n"), (80, -1, b"80,0,1\n"), (0, 0, b"0,0,0\n"), (255, 1, b"255,1,0\n")],
)
def test_command_encoding(speed, direction, expected):
    conn = FakeConnection()
    send_motor_command(conn, speed, direction)
    assert conn.written == [expected]


@pytest.mark.parametrize("speed", [-1, 256])
def test_rejects_out_of_range_speed(speed):
    conn = FakeConnection()
    with pytest.raises(ValueError):
        send_motor_command(conn, speed, 1)
    assert conn.written == []


def test_rejects_bad_direction():
    with pytest.raises(ValueError):
        send_motor_command(FakeConnection(), 10, 2)
