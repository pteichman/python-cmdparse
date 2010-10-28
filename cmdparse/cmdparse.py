import sys, os
import types

from optparse import OptionParser, OptionError, SUPPRESS_USAGE
from gettext import gettext as _

class Command(OptionParser):
    def __init__(self, name, *args, **kwargs):
        self.name = name

        self.aliases = kwargs.get("aliases", [])
        self.summary = kwargs.get("summary", None)

        for key in ("aliases", "summary"):
            if kwargs.has_key(key):
                del kwargs[key]

        OptionParser.__init__(self, *args, **kwargs)

        if len(self.aliases) > 0:
            self.helpstr = self.name + " (%s)" % ", ".join(self.aliases)
        else:
            self.helpstr = self.name

    def get_prog_name(self):
        if self.prog is None:
            return os.path.basename(sys.argv[0])
        else:
            return self.prog

    def expand_cmd_name(self, s):
        return s.replace("%cmd", self.get_name())

    def expand_prog_name(self, s):
        return s.replace("%prog", self.get_prog_name())

    def set_usage(self, usage):
        if usage is None:
            self.usage = _("%prog %cmd [options]")
        elif usage is SUPPRESS_USAGE:
            self.usage = None
        else:
            self.usage = usage

    def get_usage(self):
        if self.usage:
            return self.formatter.format_usage(
                self.expand_cmd_name(self.expand_prog_name(self.usage)))
        else:
            return ""

    def has_name(self, alias):
        if alias == self.name:
            return True
        if alias in self.aliases:
            return True

    def run(self, options, args):
        pass

    def get_name(self):
        return self.name

    def error(self, msg=None):
        # This is pretty nasty, but it's helpful to users.. rewrite
        # "no such option" error messages to include the command name.
        # I wonder how to add i18n properly here, so we'll match the
        # correct string everywhere

        s = "no such option: "
        if msg and msg.startswith(s):
            msg = _("no such %s option: %s") % (self.name, msg[len(s):])
        self.exit(1, msg)

    def exit(self, status=0, msg=None):
        if msg:
            sys.stderr.write(msg)
            sys.stderr.write("\n")
        sys.exit(status)

class CommandParser(OptionParser):
    """Parse command-line options CVS style."""
    def __init__(self, *args, **kwargs):
        if not kwargs.has_key("usage"):
            kwargs["usage"] = "%prog [options] <command> [command options]"
        OptionParser.__init__(self, *args, **kwargs)

        self.commands = []
        self.groups = {}

    def check_required(self, opt):
        option = self.get_option(opt)

        # Assumes the options's 'default' is set to None!
        if getattr(self.values, option.dest) is None:
            self.error("%s option not supplied" % option)

    def add_command(self, command, group="Other"):
        command.parser = self
        self.commands.append(command)
        self.groups.setdefault(group, []).append(command)

    def add_commands(self, module, group="Other"):
        # add all the Command subclasses found in a module
        for attr in dir(module):
            cls = getattr(module, attr)

            if not type(cls) is types.ClassType:
                continue

            if (not cls is Command) \
                   and issubclass(getattr(module, attr), Command):
                self.add_command(cls(), group)

    def find_command(self, alias):
        for command in self.commands:
            if command.has_name(alias):
                return command

    def exit(self, status=0, msg=None):
        if msg:
            sys.stderr.write(msg)
        sys.exit(status)

    def parse_args(self, *args, **kwargs):
        self.disable_interspersed_args()
        (options, args) = OptionParser.parse_args(self, *args, **kwargs)

        cmd = None

        if len(args) > 0:
            cmd = self.find_command(args[0])

            if cmd is None:
                self.print_unknown_command(args[0])
            else:
                (cmdoptions, args) = cmd.parse_args(args[1:])

                # update options with the values from cmdoptions
                for (attr, val) in cmdoptions.__dict__.items():
                    setattr(options, attr, val)

        return (cmd, options, args)

    def print_unknown_command(self, cmdname, file=None):
        if file is None:
            file = sys.stdout
        file.write("Unknown command '%s'\n" % cmdname)

    def format_help(self, *args, **kwargs):
        help = OptionParser.format_help(self, *args, **kwargs)
        return help + "\n" + self.format_command_help()

    def format_command_help(self):
        result = []

        groups = self.groups.keys()
        groups.sort()

        max_cmd_length = 0
        for cmd in self.commands:
            max_cmd_length = max(max_cmd_length, len(cmd.helpstr))

        for group in groups:
            result.append("%s commands:\n" % group)
            commands = self.groups[group]
            commands.sort(lambda x, y: cmp(x.get_name(), y.get_name()))

            for cmd in commands:
                result.append("  %s%s  %s\n" % (cmd.helpstr, " "*(max_cmd_length-len(cmd.helpstr)), cmd.summary))
        return "".join(result)
