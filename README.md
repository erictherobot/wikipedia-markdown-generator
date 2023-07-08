# Wikipedia To Markdown

This is a simple script to convert a Wikipedia article to Markdown.

## Prerequisites

- Python 3

## Installation

```bash
git clone
cd wikipedia-markdown-generator
pip3 install -r requirements.txt
```

## Usage

```bash
python3 wiki-to-md.py <topic_name>
```

## Output

The output is a Markdown file with the same name as the topic name under the newly created directory `md_output` if using `wiki-to-md.py`. If you want to download images too, use the `wiki-to-md-images.py` file and the images will be placed inside `md_output/images/`.

> Note: eventually, `wiki-to-md.py` and `wiki-to-md-images.py` will be combined into one script with a flag to download images or not.

## Why?

I wanted to convert some Wikipedia articles to Markdown for my personal notes. I couldn't find a simple script to do this, so I wrote one myself.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
