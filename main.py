import pytube
import moviepy.editor as mp

def download_audio(url):
    try:
        youtube = pytube.YouTube(url)
        video = youtube.streams.filter(only_audio=True).first()
        video.download()
        print("Video downloaded successfully!")

        video_file = video.default_filename
        mp4_file = video_file.replace('.webm', '.mp4')
        mp3_file = video_file.replace('.webm', '.mp3')

        video_clip = mp.VideoFileClip(mp4_file)
        video_clip.audio.write_audiofile(mp3_file)

        video_clip.close()
        print("Audio extracted and saved as MP3 successfully!")
    except pytube.exceptions.PytubeError as e:
        print(f"Error: {str(e)}")

# Example usage
video_url = input("Enter video link here: ")

download_audio(video_url)
