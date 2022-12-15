from pytube import YouTube

def Download(url):
    youtubeObj = YouTube(url)
    
    youtubeObj1 = youtubeObj.streams.get_highest_resolution()
    try:
        youtubeObj1.download()
    except:
        
        print("Error in downloading " + youtubeObj.title)
    print("Download was successfull! for " + youtubeObj.title)

urlLink = input("Please  enter the link/links of the youtube video you want to download: ")
links = urlLink.split(' ')

for link in links:
    Download(link)
