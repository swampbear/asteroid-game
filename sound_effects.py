from pygame import mixer

mixer.init()
mixer.music.set_volume(0.7)

SHOT_SOUND = mixer.Sound("./assets/shot-kristian.wav")

def play_shot_sound():
    mixer.Sound.play(SHOT_SOUND)
