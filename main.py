from GSpeaker import GSpeaker
from moviepy.editor import *

ayah = "O believers! When you contract a loan for a fixed period of time, commit it to writing. Let the scribe maintain justice between the parties. The scribe should not refuse to write as Allah has taught them to write. They will write what the debtor dictates, bearing Allah in mind and not defrauding the debt. If the debtor is incompetent, weak, or unable to dictate, let their guardian dictate for them with justice. Call upon two of your men to witness. If two men cannot be found, then one man and two women of your choice will witness—so if one of the women forgets the other may remind her.1 The witnesses must not refuse when they are summoned. You must not be against writing ˹contracts˺ for a fixed period—whether the sum is small or great. This is more just ˹for you˺ in the sight of Allah, and more convenient to establish evidence and remove doubts. However, if you conduct an immediate transaction among yourselves, then there is no need for you to record it, but call upon witnesses when a deal is finalized. Let no harm come to the scribe or witnesses. If you do, then you have gravely exceeded ˹your limits˺. Be mindful of Allah, for Allah ˹is the One Who˺ teaches you. And Allah has ˹perfect˺ knowledge of all things."

speaker = GSpeaker(ayah)
speaker.speak()

def mp3PNGMerge(fileSaveName):
    
    audio_clip = AudioFileClip("audios/audio.mp3")
    image_clip = ImageClip("images/bg.png")
    
    video_clip = image_clip.set_audio(audio_clip)
    
    video_clip.set_audio(audio_clip)
    video_clip.duration = audio_clip.duration
    
    video_clip.fps = 30

    screensize = (1720,980)
    txt_clip = TextClip(ayah +" \n\n[Surah Al-Baqarah 2:282]", fontsize = 30, color = '#763c00', font="Sinhala-MN", method='caption', size=screensize) 
    txt_clip = txt_clip.set_pos('center').set_duration(audio_clip.duration)
    
    video = CompositeVideoClip([video_clip, txt_clip], size=video_clip.size) 
    video.duration = audio_clip.duration
    # video.set_duration(audio_clip.duration)
    video.write_videofile(fileSaveName + '_CLIP.mp4')

mp3PNGMerge('videos/test')
# for x in TextClip.list('font'):
#     print(x)
