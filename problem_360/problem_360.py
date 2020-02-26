import logging
from typing import Iterable, List

logger = logging.getLogger(__name__)


class Playlist(object):
    def __init__(self, rankings: Iterable[int]):

        # Unique collection
        ranked = set()

        # Rankings for songs
        self.rankings: List[int] = []

        # Cast to int
        for v in map(int, rankings):

            # Verify unique
            if v in ranked:
                raise ValueError(f"Already ranked song ID: {v}")

            # Verify greater than 0
            elif v < 0:
                raise ValueError(f"Song ID can not be less than 0, got: {v}")

            # Add to rankings
            ranked.add(v)
            self.rankings.append(v)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.rankings})"

    @classmethod
    def create_playlist(cls, playlists: Iterable["Playlist"]) -> "Playlist":

        # Number of playlist
        n_playlists = 0

        # Rankings across all playlists
        all_rankings = {}

        # Average # of songs per playlist
        average_songs = 0

        # Gather playlist stats
        for playlist in playlists:

            # Type check
            if not issubclass(type(playlist), cls):
                raise TypeError(f"Did not receive playlist: {playlist}")

            # Determine composite stats
            n_playlists += 1
            n_songs = len(playlist.rankings)
            average_songs += (n_songs - average_songs) / n_playlists

        # Confirm at least two playlists provided
        if n_playlists < 2:
            raise ValueError("Must be given at least two playlists to make playlist")

        # Determine individual song scores
        for playlist in playlists:
            n_songs = len(playlist.rankings)
            for i, v in enumerate(playlist.rankings):
                all_rankings.setdefault(v, []).append(i * n_songs / average_songs)

        # Confirm at least one song available
        total_songs = len(all_rankings)
        if total_songs < 1:
            raise ValueError("No sounds found across all playlists")

        # Log stats
        logger.info(f"Creating playlist based off {n_playlists:,} playlist")
        logger.info(f"Number of unique songs = {total_songs:,}")
        logger.info(
            f"Average number of songs ranked per playlist = {average_songs:,.02f}"
        )

        # Determine total scores
        scores = (
            (k, sum(v) + (total_songs - len(v)) ** 2) for k, v in all_rankings.items()
        )

        # Create final playlist based off of scores
        return cls(k for k, _ in sorted(scores, key=lambda x: x[1]))
