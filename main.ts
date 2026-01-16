input.onGesture(Gesture.Shake, function () {
    basic.showNumber(6)
    basic.showIcon(IconNames.Yes)
    basic.showString("Hello!")
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Angry)
})
