from crewai import Agent, Task, Crew, Process
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
import requests, re, os

# ---------- Utility ----------
def sanitize_filename(name):
    """Remove invalid filename characters for cross-platform safety."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

# ---------- Agent ----------
class TranscriptAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Transcript Agent",
            goal="Fetch and save accurate transcripts from YouTube videos",
            backstory="This agent fetches real transcripts using YouTubeTranscriptApi, not LLM."
        )

    def run(self, video_id: str, paragraph_break: float = 5.0):
        # Fetch transcript
        yt = YouTubeTranscriptApi()
        transcript = yt.fetch(video_id)

        paragraphs = []
        current_para = []
        last_end = 0.0

        for entry in transcript:
            text = entry.text
            start = entry.start
            duration = entry.duration

            if start - last_end > paragraph_break and current_para:
                paragraphs.append(" ".join(current_para))
                current_para = []

            current_para.append(text)
            last_end = start + duration

        if current_para:
            paragraphs.append(" ".join(current_para))

        # Fetch video title
        try:
            resp = requests.get(
                f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
            )
            title = resp.json().get("title", f"video_{video_id}")
        except Exception:
            title = f"video_{video_id}"

        safe_title = sanitize_filename(title)
        os.makedirs("transcripts", exist_ok=True)
        filename = f"transcripts/{safe_title}_{video_id}.txt"

        # Save transcript
        with open(filename, "w", encoding="utf-8") as f:
            for i, para in enumerate(paragraphs, start=1):
                f.write(f"Paragraph {i}:\n{para}\n\n")

        return {
            "file_path": filename,
            "title": title,
            "content": "\n\n".join(paragraphs)
        }

# ---------- Crew Setup ----------
def build_transcript_crew():
    agent = TranscriptAgent()

    # Important: input_keys ensures Crew passes video_id to agent.run
    task = Task(
        description="Fetch transcript for a YouTube video and save to file.",
        expected_output="Dictionary with file_path, title, and content",
        agent=agent,
        input_keys=["video_id"],          # maps inputs to run() argument
        output_keys=["file_path", "title", "content"]  # ensures output captured
    )

    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential
    )
    return crew

# ---------- Example Usage ----------
if __name__ == "__main__":
    video_id = "64Zp3tzNbpE"
    os.environ["OPENAI_API_KEY"] = "sk-proj-"

    crew = build_transcript_crew()

    try:
        # Kickoff Crew
        results = crew.kickoff(inputs={"video_id": video_id})
        print(f"✅ Crew kickoff completed. Result type: {type(results)}\n")

        # Convert CrewOutput to a dictionary safely
        if hasattr(results, "to_dict"):
            res_dict = results.to_dict()
        else:
            res_dict = dict(results)

        # Print the output dictionary for debugging
        print("CrewOutput converted to dict:")
        print(res_dict)

        # Access transcript fields
        file_path = res_dict.get("file_path")
        title = res_dict.get("title")
        content = res_dict.get("content")

        if file_path and title and content:
            print(f"\n✅ Transcript saved to: {file_path}")
            print(f"🎬 Video Title: {title}")
            print("\n📜 First 500 characters of transcript:\n")
            print(content[:500], "...")
        else:
            print("⚠️ Unexpected CrewOutput structure:")
            print(res_dict)

    except NoTranscriptFound:
        print("❌ No transcript found for this video.")
    except TranscriptsDisabled:
        print("❌ Transcripts are disabled for this video.")
    except VideoUnavailable:
        print("❌ Video unavailable.")
    except Exception as e:
        print("⚠️ Unexpected error:", e)
