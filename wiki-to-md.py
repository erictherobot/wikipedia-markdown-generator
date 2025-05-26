import os
import wikipedia
import argparse
import re


def generate_markdown(topic):
    try:
        page = wikipedia.page(topic)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        return None
    except wikipedia.exceptions.PageError:
        print(f"Page not found for the topic: {topic}")
        return None

    markdown_text = f"# {topic}\n\n"

    page_content = re.sub(r"=== ([^=]+) ===", r"### \1", page.content)
    page_content = re.sub(r"== ([^=]+) ==", r"## \1", page_content)

    sections = re.split(r"\n(## .*)\n", page_content)
    for i in range(0, len(sections), 2):
        if i + 1 < len(sections) and any(
            line.strip() for line in sections[i + 1].split("\n")
        ):
            markdown_text += f"{sections[i]}\n{sections[i+1]}\n\n"

    # Create a directory for markdown files
    directory = "md_output"
    os.makedirs(directory, exist_ok=True)

    filename = os.path.join(directory, f"{topic.replace(' ', '_')}.md")

    with open(filename, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_text)

    print(f"Markdown file created: {filename}")
    return filename


parser = argparse.ArgumentParser(
    description="Generate a markdown file for a provided topic."
)
parser.add_argument(
    "topic",
    type=str,
    help="The topic to generate a markdown file for.",
)
parser.add_argument(
    "--lang",
    type=str,
    default="en",
    help="The 2-letter language code for the Wikipedia page (default: 'en')."
)

args = parser.parse_args()

# Set the language for Wikipedia if provided
wikipedia.set_lang(args.lang)

topic = f"{args.topic}"

generate_markdown(topic)

