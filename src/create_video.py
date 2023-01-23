import math, random
from tts import convert_tts
from moviepy.editor import *
from moviepy.video.VideoClip import TextClip


def create_video(sentence_list:list[str]) -> None:
    """Creates a reddit tts video with list of sentences.
    
        Parameters
        ----------
        sentence_list : list[str]
            List of sentences to be converted to audio and added to the video.
        
        Returns
        -------
        None
        """
    
    # Initialize variables
    audio_clips = []
    text_clips = []
    duration = 0

    for i, sentence in enumerate(sentence_list):
        # Create the audio for sentence
        audio_path = convert_tts(sentence, i)
        audio_clip = AudioFileClip(audio_path)
        # Add it to audio clip list
        audio_clips.append(audio_clip)
        
        # Create subtitle
        text_clip = TextClip(sentence, font = "Ebrima-Bold", fontsize = 50, color = "white", stroke_color="black", stroke_width=1.75, method="caption", align="center", size=(720, 1080))
        text_clip = text_clip.set_position(("center", 0.2), relative=True)
        
        if i == 0:
            # Set text clip length
            text_clip = text_clip.set_start(0)
            text_clip = text_clip.set_end(audio_clip.duration)
        else:
            # Set text clip length
            text_clip = text_clip.set_start(text_clips[i-1].end)
            text_clip = text_clip.set_end(text_clip.start + audio_clip.duration)
        
        # Add subtitle to list
        text_clips.append(text_clip)
        # Will be set to the last subtitle's end point
        duration = text_clip.end
        
    # Get a random start time that won't cause an error by being to close to the end of the background video
    clip_length = VideoFileClip("./background_clips/background.mp4").duration
    random_start_time = random.randrange(0, math.floor(clip_length-duration))
    
    # Generate background video with correct length
    video_clip = VideoFileClip("./background_clips/background.mp4").subclip(random_start_time, random_start_time + duration + 0.5)
     
    # Create one continous audio from the audio clip list   
    final_audio_clip = concatenate_audioclips(audio_clips)
    
    # Set it to the video's audio
    video_clip = video_clip.set_audio(final_audio_clip)

    # Add all subtitles to the video
    final_video_clip = CompositeVideoClip([video_clip, *text_clips])
    
    # Export the video
    final_video_clip.write_videofile(f"C:\\Users\\{os.getlogin()}\\Downloads\\finalvideo.mp4")