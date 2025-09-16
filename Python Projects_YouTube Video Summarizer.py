"""
This is a python code which does the following:-

It fetches the video title from YouTube.

Uses that title as the filename prefix.

Writes the cleaned transcript into a .txt file.
"""
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
from urllib.parse import urlparse, parse_qs
import requests
import re

def sanitize_filename(name):
    """Remove invalid filename characters."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

def get_full_transcript(video_id, paragraph_break=5.0):
    """
    Fetches the full transcript for a video, merges chunks into paragraphs,
    and saves it to a .txt file named after the video title.
    """
    yt = YouTubeTranscriptApi()
    transcript = yt.fetch(video_id)  # returns FetchedTranscriptSnippet objects

    paragraphs = []
    current_para = []
    last_end = 0.0

    for entry in transcript:
        # Support both object-style and dict-style entries
        text = entry.text if hasattr(entry, "text") else entry["text"]
        start = entry.start if hasattr(entry, "start") else entry["start"]
        duration = entry.duration if hasattr(entry, "duration") else entry["duration"]

        if start - last_end > paragraph_break and current_para:
            paragraphs.append(" ".join(current_para))
            current_para = []

        current_para.append(text)
        last_end = start + duration

    if current_para:
        paragraphs.append(" ".join(current_para))

    # Fetch video title from YouTube oEmbed API
    try:
        resp = requests.get(f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json")
        title = resp.json().get("title", f"video_{video_id}")
    except Exception:
        title = f"video_{video_id}"

    safe_title = sanitize_filename(title)
    filename = f"{safe_title}_{video_id}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        for i, para in enumerate(paragraphs, start=1):
            f.write(f"Paragraph {i}:\n{para}\n\n")

    print(f"✅ Transcript saved to: {filename}")
    return filename

# Example usage
video_id = "64Zp3tzNbpE"
try:
    get_full_transcript(video_id)
except NoTranscriptFound:
    print("❌ No transcript found.")
except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except VideoUnavailable:
    print("❌ Video unavailable.")
except Exception as e:
    print("⚠️ Unexpected error:", e)
