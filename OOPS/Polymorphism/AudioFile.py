"""A user defined exception class"""
class InvalidAudioFormatError(Exception):
    def __str__(self):
        return "Invalid File Format"


class AudioFile:
    ext = ""

    def __init__(self, filename):
        
        if not filename.endswith(self.ext):
            raise InvalidAudioFormatError
        
        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))

if __name__=="__main__":
    try:
        myAudio = MP3File("lecture1.mp3")
        myAudio.play()

        myAudio = WavFile("lecture1.wav")
        myAudio.play()

        myAudio = OggFile("lecture1.ogg")
        myAudio.play()

        myAudio = MP3File("lecture1.wmv")
        myAudio.play()
        
    except InvalidAudioFormatError as e:
        print(e)
        
