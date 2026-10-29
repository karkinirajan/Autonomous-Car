import numpy as np
import pytest
from rotations import Quaternion, angle_normalize, skew_symmetric


def test_angle_normalize_wraps_into_range():
    out = angle_normalize(np.array([3 * np.pi, -3 * np.pi / 2, 0.5, np.pi]))
    assert np.all(out > -np.pi - 1e-12) and np.all(out <= np.pi + 1e-12)
    assert out[2] == pytest.approx(0.5)
    assert out[1] == pytest.approx(np.pi / 2)


def test_skew_symmetric_is_cross_product():
    v, w = np.array([1.0, 2.0, 3.0]), np.array([-4.0, 0.5, 2.0])
    assert skew_symmetric(v) @ w == pytest.approx(np.cross(v, w))
    assert skew_symmetric(v) == pytest.approx(-skew_symmetric(v).T)


def test_identity_quaternion_gives_identity_matrix():
    assert Quaternion().to_mat() == pytest.approx(np.eye(3))


def test_euler_round_trip():
    rpy = np.array([0.1, -0.2, 0.3])
    assert Quaternion(euler=rpy).to_euler() == pytest.approx(rpy)


def test_axis_angle_rotates_about_z():
    q = Quaternion(axis_angle=[0, 0, np.pi / 2])
    assert q.to_mat() @ np.array([1.0, 0, 0]) == pytest.approx([0, 1, 0], abs=1e-12)


def test_rotation_matrix_is_orthonormal():
    r = Quaternion(euler=[0.4, 0.1, -0.7]).to_mat()
    assert r @ r.T == pytest.approx(np.eye(3))
    assert np.linalg.det(r) == pytest.approx(1.0)


def test_normalize_gives_unit_norm():
    assert np.linalg.norm(Quaternion(2, 0, 0, 0).normalize().to_numpy()) == pytest.approx(1.0)


def test_cannot_specify_both_euler_and_axis_angle():
    with pytest.raises(AttributeError):
        Quaternion(euler=[0, 0, 0], axis_angle=[0, 0, 0])


def test_axis_angle_requires_length_three():
    with pytest.raises(ValueError):
        Quaternion(axis_angle=[1, 2])
