from pytube import YouTube
import os

def download_youtube_video():
    #Get the Youtube URL from the user
    youtube_url = input("Enter your Youtube URL: ")
    
    #Get The file directory from the user
    save_directory = input("Enter where you want your video to be downloaded to: ")
    
    #Get the directory to strings
    save_directory = save_directory.strip('"')
    #Enser the saved file directory exists
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    try:
        #Create a Youtube Object:
        yt = YouTube(youtube_url)
        
        #Get the highest resolution stream available
        # video_stream = yt.streams.get_highest_resolution()
        
        #GEt all available video streams options
        video_stream = yt.streams.filter(progressive=True).order_by("resolution").desc()
        
        #Display available streams to the user
        print("Available video streams: ")
        for i, stream in enumerate(video_stream):
            print(f"")
        
        
        #Download Video
        print(f"Downloading '{yt.title}....>")
        video_stream.download(save_directory)
        print(f"Your download is located in  ({save_directory})!!!")
        
    except Exception as e:
        print(f"An error occured: {e}")
        
if __name__ == '__main__':
    download_youtube_video()
        
    
    
