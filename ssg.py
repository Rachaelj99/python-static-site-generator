import typer

from ssg.site import Site

#a function that captures command line arguments
def main(source="content", dest="dist"):
    config = {"source": source, "dest": dest}

    #creates an instance of 'Site' class
    #2 attributes/args = unpacked dictionary values with **
    #chains a call to the build()
    Site(**config).build()

typer.run(main)
