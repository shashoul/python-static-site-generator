import typer
from ssg.site import Site
import sgg.parsers


def main(source='content', dest='dist'):
    config ={
        "source": source,
        "dest": dest,
        "parsers": [ssg.parsers.ResourceParser()]
    }

    Site(**config).build()
    # site = Site(**config)

    # site.build()

typer.run(main)