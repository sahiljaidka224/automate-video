import pyttsx3
import requests
import praw
import moviepy.editor as mp


voiceoverDirectory = "Voiceovers"

reddit = praw.Reddit(
    client_id="JKbFMDkzV7Lw1mcmTSDXaA",
    client_secret="KQDSwdMYfe-16peiy96FoTEAo8xNNQ",
    user_agent="yt-videos",
    password="@@LvZ3kdw*@L7:c",
    username="PossibleThanks4757"
)


def createVoiceOver(id, text):
    engine = pyttsx3.init()
    filePath = f"{voiceoverDirectory}/comment-{id}.mp3"
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath


def createClip(imageUrl, commentId, comment):
    # image_data = requests.get(imageUrl).content

    # imageClip = mp.ImageClip("test.jpeg")

    # print("imageCLip", imageClip)

    voiceOverFile = createVoiceOver(commentId, comment)
    audioClip = mp.AudioClip(voiceOverFile)
    print("audioClip", audioClip)

    # videoClip = imageClip.set_audio(audioClip)
    # print("videoClip", videoClip)

    return
    with open("image.jpg", "wb") as handler:
        handler.write(image_data)
        imageClip = mp.ImageClip("test.jpeg")

        print("imageCLip", imageClip)

        print("Imageclip", imageClip)
        audioClip = mp.AudioClip(createVoiceOver("random", "this is random"))
        print("audioClip", audioClip)

        videoClip = imageClip.set_audio(audioClip)
        print("videoClip", videoClip)

        return videoClip


clips = []

subreddit = reddit.subreddit("wallstreetbets")
print("Display Name:", subreddit.display_name)

for submission in subreddit.top(time_filter="day", limit=1):
    print("***************")
    print("Submission")
    print("Title", submission.title)
    print("Id", submission.id)
    print("Url", submission.url)

    comment = submission.comments[0].body
    commentId = submission.comments[0].id

    print("***************")
    print("Submission")
    print("comment", comment)
    print("commentId", commentId)

    # voiceOverFile = createVoiceOver(commentId, comment)

    clip = createClip(submission.url, commentId, comment)
    print("clip", clip)
    clips.append(clip)


# def mixComments(comments):
#     for comment in comments:
#         if (len(comment.body.split()) > 100):
#             continue

# video_clips = []

# for post in top_posts:
#     top_comment = post.title
#     print(top_comment)

#     image_url = post.url
#     image_data = requests.get(image_url).content
#     with open("image.jpg", "wb") as handler:
#         handler.write(image_data)
#         video_clip = mp.ImageClip("image.jpg").set_duration(10)
# text_clip = mp.TextClip(top_comment, fontsize=24, color="white").set_duration(10).set_position(("center", "bottom"))
# final_clip = mp.CompositeVideoClip([video_clip, text_clip])
# video_clips.append(final_clip)

# final_video = mp.concatenate_videoclips(video_clips)
# final_video.write_videofile("wallstreetbets_top_posts.mp4", fps=24)

# connect to YouTube's API to publish the video to your channel
