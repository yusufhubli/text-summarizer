import click
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def summarize_text(text):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 8)  # Summarize to 2 sentences
    return " ".join(str(sentence) for sentence in summary)

@click.command()
@click.option('-t', '--text', type=str, help='Text or path to text file to be summarized')
def main(text):
    if text.endswith('.txt'):
        try:
            with open(text, 'r') as file:
                content = file.read()
                summary = summarize_text(content)
        except FileNotFoundError:
            click.echo(f"File {text} not found.")
            return
    else:
        summary = summarize_text(text)
    
    click.echo(summary)

if __name__ == '__main__':
    main()
