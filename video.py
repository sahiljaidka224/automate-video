import praw
import moviepy.editor as mp
import pyttsx3
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    user_agent=os.getenv('USER_AGENT'),
    password=os.getenv('PASSWORD'),
    username=os.getenv('USERNAME')
)


def create_audio_clip(text, id):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    engine.save_to_file(comment_text, 'temp_audio.mp3')
    engine.runAndWait()

    # filePath = f"comment-{id}.mp3"
    # engine.save_to_file(text, filePath)
    # engine.runAndWait()
    return


subreddit = reddit.subreddit("wallstreetbets")
posts = subreddit.top(time_filter="day", limit=1)

comment_text = "Test"
comment_id = "id"

for post in posts:
    print(post)
    comment_text = post.comments[0].body
    comment_id = post.comments[0].id

create_audio_clip(comment_text, comment_id)

background_clip = mp.VideoFileClip("background.mp4")
audio_clip = mp.AudioFileClip("temp_audio.mp3")
text_clip = mp.TextClip(comment_text, fontsize=24,
                        color='white').set_duration(background_clip.duration)
text_clip = text_clip.set_position('center')

final_clip = mp.CompositeVideoClip([background_clip, text_clip])
final_clip = final_clip.set_audio(audio_clip)
final_clip.write_videofile("output.mp4")
