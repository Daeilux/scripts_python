import pytube

video_url = input("Inserta la url del video: ")
youtube = pytube.YouTube(video_url)

video = youtube.streams.first()
video.download()