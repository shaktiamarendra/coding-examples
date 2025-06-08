from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the Phi-2 model and tokenizer
model_id = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

# Create a text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_prompt(song):
    return (
        f"Generate a catchy SEO title and description for a music detail page.\n\n"
        f"Song Title: {song.get('title')}\n"
        f"Artist: {song.get('artist')}\n"
        f"URL: {song.get('url')}\n\n"
        f"Output Format:\n"
        f"Title: <title>\n"
        f"Description: <description>\n"
    )

def generate_metadata(song):
    prompt = generate_prompt(song)
    print("🧠 Prompt:\n", prompt)
    result = generator(prompt, max_new_tokens=100, temperature=0.7, do_sample=True)
    output = result[0]['generated_text']
    
    # Extract only the generated part (after the prompt)
    generated_part = output[len(prompt):].strip()
    return generated_part

# Example song
song = {
    "title": "Shape of You",
    "artist": "Ed Sheeran",
    "url": "https://music.amazon.com/tracks/B0C6YFYSXS"
}

print("🔹 Metadata:\n", generate_metadata(song))