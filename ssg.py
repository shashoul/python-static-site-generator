import typer
from ssg.site import Site
import ssg.parsers


def main(source='content', dest='dist'):
    config ={
        "source": source,
        "dest": dest,
        "parsers": [ssg.parsers.ResourceParser(), ssg.parsers.MarkdownParser(), ssg.parsers.ReStructuredTextParser()]
    }

    Site(**config).build()
    # site = Site(**config)

    # site.build()

typer.run(main)