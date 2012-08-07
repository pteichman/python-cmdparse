from cmdparse import Command


class EchoCommand(Command):
    def __init__(self):
        Command.__init__(self, "echo", summary="echo a string")

    def run(self, options, args):
        print " ".join(args)
