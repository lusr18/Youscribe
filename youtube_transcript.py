from youtube_transcript_api import YouTubeTranscriptApi
import os

def sanitize_filename(filename):
    illegal_chars = '<>:"/\\|?*'
    for char in illegal_chars:
        filename = filename.replace(char, '')
    return filename

def youtube_to_transcript(title, url):
    #identify unique url id
    video_id = url.split("=")[1]
    if '&pp' in video_id:
        video_id = video_id.split("&pp")[0]

    # Acquire transcript from url
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id,
                                            languages=['en'])
    except:
        print("Transcript could not be fetched, skipping video.")
        return

    # Write transcript from received object into file
    path = os.path.join(".\youtube_transcripts", 
                        (sanitize_filename(title) + ".txt"))
    with open(path, "w", encoding='utf-8') as f:
        f.write(title + "\n" + url + "\n")
        for i in transcript:
            f.write(i["text"] + "\n")
    f.close()
    print("File made for: " + title + '\n')

if __name__ == "__main__":
    pass
    # test input
    #youtube_to_transcript("https://www.youtube.com/watch?v=mMv6OSuitWw&pp=ygUbZ2V0dGluZyBzdGFydGVkIHdpdGggcHl0aG9u", "Python 101 Learn the 5 Must-Know Concepts")