import os
import wikipedia
import argparse
import re
import requests
import urllib.parse


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
    output_directory = "md_output"
    os.makedirs(output_directory, exist_ok=True)

    # Create a directory for image files
    image_directory = os.path.join(output_directory, "images")
    os.makedirs(image_directory, exist_ok=True)

    for image_url in page.images:
        image_filename = urllib.parse.unquote(os.path.basename(image_url))
        image_path = os.path.join(image_directory, image_filename)
        image_data = requests.get(image_url).content
        with open(image_path, "wb") as image_file:
            image_file.write(image_data)
        markdown_text += f"![{image_filename}](./images/{image_filename})\n"

    filename = os.path.join(output_directory, f'{topic.replace(" ", "_")}.md')

    with open(filename, "w") as md_file:
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

args = parser.parse_args()

topic = f"{args.topic}"

generate_markdown(topic)
