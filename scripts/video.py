import moviepy.editor as mp
import pyttsx3

# Set up the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Set up the text and audio variables
text = "Hello, world! This is a sample text to be converted to audio and embedded in a video."
audio_file = "audio.mp3"

# Convert the text to audio
engine.save_to_file(text, audio_file)
engine.runAndWait()

# Set up the video variables
video_file = "video.mp4"
duration = 10  # Video duration in seconds
fps = 30  # Frames per second

# Create the video clip
text_clip = mp.TextClip(text, fontsize=24, color='white').set_duration(
    duration).set_position(('center', 'bottom'))
audio_clip = mp.AudioFileClip(audio_file).set_duration(duration)
final_clip = mp.CompositeVideoClip(
    [text_clip.set_audio(audio_clip)], size=(640, 480))

# Write the video file to disk
final_clip.write_videofile(video_file, fps=fps)
