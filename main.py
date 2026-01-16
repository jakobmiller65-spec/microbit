def on_gesture_shake():
    basic.show_number(6)
    basic.show_icon(IconNames.YES)
    basic.show_string("Hello!")
    music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
