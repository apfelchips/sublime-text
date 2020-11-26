import sublime
import sublime_plugin

class PythonExecCommand(sublime_plugin.WindowCommand):
    def run(self, cmd):
            exec(cmd)
