from pygame import mixer

mixer.init()

bullet_sound = mixer.Sound('sounds/laser.wav')
explosion = mixer.Sound('sounds/explosion.wav')
detecting = mixer.Sound('sounds/detecting.wav')
target_detected = mixer.Sound('sounds/target_detected.wav')