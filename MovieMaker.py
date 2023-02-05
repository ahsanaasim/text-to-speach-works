from moviepy.editor import *

class MovieMaker:
    
    def generate(self, text):
    
        audio_clip = AudioFileClip("audios/audio.mp3")
        image_clip = ImageClip("images/bg.png")
        
        video_clip = image_clip.set_audio(audio_clip)
        
        video_clip.set_audio(audio_clip)
        video_clip.duration = audio_clip.duration
        
        video_clip.fps = 30

        screensize = (1720,980)
        txt_clip = TextClip(text, fontsize = 30, color = '#763c00', font="Sinhala-MN", method='caption', size=screensize) 
        txt_clip = txt_clip.set_pos('center').set_duration(audio_clip.duration)
        
        video = CompositeVideoClip([video_clip, txt_clip], size=video_clip.size) 
        video.duration = audio_clip.duration
        
        video.write_videofile('videos/ayah_' + '_CLIP.mp4')