import logging

import pytest

from problem_360 import Playlist

logging.basicConfig(level=logging.DEBUG)


@pytest.mark.parametrize(
    "left, right",
    (
        pytest.param("1423", [1, 4, 2, 3], id="1423"),
        pytest.param(range(0, 5), list(range(0, 5)), id="range(0,5)"),
        pytest.param([9, 3.5, 7], [9, 3, 7], id="[1, 3.5, 7]"),
    ),
)
def test_playlist(left, right):
    playlist = Playlist(left)
    assert playlist.rankings == right


@pytest.mark.parametrize(
    "left, exc",
    (
        pytest.param("14234", ValueError, id="14234"),
        pytest.param("142a34", ValueError, id="142a34"),
        pytest.param(range(-1, 5), ValueError, id="range(-1,5)"),
        pytest.param([1, "a", 7], ValueError, id='[1, "a", 7]'),
        pytest.param([1, 5j, 7], TypeError, id="[1, 5j, 7]"),
        pytest.param([1, None, 7], TypeError, id="[1, None, 7]"),
        pytest.param([1, -1.0, 7], ValueError, id="[1, -1.0, 7]"),
    ),
)
def test_playlist_negative(left, exc):
    with pytest.raises(exc):
        _ = Playlist(left)


def test_create_playlist():
    playlist = Playlist.create_playlist(
        [Playlist([1, 7, 3]), Playlist([2, 1, 6, 7, 9]), Playlist([3, 9, 5]),]
    )
    logging.info(f"Created => {playlist}")


@pytest.mark.parametrize(
    "playlists, exc",
    (
        pytest.param([Playlist([1]), None], TypeError, id="Bad playlist"),
        pytest.param([Playlist([1])], ValueError, id="Not enough playlists"),
        pytest.param([Playlist([]), Playlist([])], ValueError, id="Not enough songs"),
    ),
)
def test_create_playlist_negative(playlists, exc):
    with pytest.raises(exc):
        _ = Playlist.create_playlist(playlists)
