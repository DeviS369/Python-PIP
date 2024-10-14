class Audio:
    def __init__(self, title: str, artist: str, duration: float):
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def play(self):
        print(f"Playing '{self.title}' by {self.artist}")

    def pause(self):
        print(f"'{self.title}' paused")

    def stop(self):
        print(f"'{self.title}' stopped")


class Playlist:
    def __init__(self, name: str):
        self.name = name
        self.audios = []

    def add_audio(self, audio: Audio):
        self.audios.append(audio)
        print(f"Added '{audio.title}' to playlist '{self.name}'")

    def remove_audio(self, audio: Audio):
        if audio in self.audios:
            self.audios.remove(audio)
            print(f"Removed '{audio.title}' from playlist '{self.name}'")
        else:
            print(f"'{audio.title}' not found in playlist '{self.name}'")

    def play_all(self):
        print(f"Playing all tracks in playlist '{self.name}'")
        for audio in self.audios:
            audio.play()

    def list_audios(self):
        if self.audios:
            print(f"Playlist '{self.name}' contains:")
            for audio in self.audios:
                print(f" - {audio.title} by {audio.artist}")
        else:
            print(f"Playlist '{self.name}' is empty.")


class MusicPlayer:
    def __init__(self):
        self.playlists = []
        self.current_audio = None
        self.current_playlist = None

    def create_playlist(self, playlist_name: str):
        playlist = Playlist(playlist_name)
        self.playlists.append(playlist)
        print(f"Created playlist '{playlist_name}'")
        return playlist

    def select_playlist(self, playlist_name: str):
        for playlist in self.playlists:
            if playlist.name == playlist_name:
                self.current_playlist = playlist
                print(f"Selected playlist '{playlist_name}'")
                return playlist
        print(f"Playlist '{playlist_name}' not found")
        return None

    def play_audio(self, audio: Audio):
        self.current_audio = audio
        audio.play()

    def play_playlist(self, playlist_name: str):
        playlist = self.select_playlist(playlist_name)
        if playlist:
            playlist.play_all()

    def pause_audio(self):
        if self.current_audio:
            self.current_audio.pause()
        else:
            print("No audio is currently playing.")

    def stop_audio(self):
        if self.current_audio:
            self.current_audio.stop()
            self.current_audio = None
        else:
            print("No audio is currently playing.")

    def list_playlists(self):
        if self.playlists:
            print("Available playlists:")
            for playlist in self.playlists:
                print(f" - {playlist.name}")
        else:
            print("No playlists available.")


# Example Usage
if __name__ == "__main__":
    player = MusicPlayer()

    # Create some audios
    song1 = Audio("Song 1", "Artist A", 3.5)
    song2 = Audio("Song 2", "Artist B", 4.0)
    song3 = Audio("Song 3", "Artist C", 2.8)

    # Create playlists and add audios
    playlist1 = player.create_playlist("My Favorite Songs")
    playlist1.add_audio(song1)
    playlist1.add_audio(song2)

    playlist2 = player.create_playlist("Chill Vibes")
    playlist2.add_audio(song3)

    # List all playlists
    player.list_playlists()

    # Play all audios in a playlist
    player.play_playlist("My Favorite Songs")

    # Play, pause, and stop individual audio
    player.play_audio(song1)
    player.pause_audio()
    player.stop_audio()

    # List audios in a playlist
    playlist1.list_audios()
    playlist2.list_audios()
