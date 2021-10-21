# src: https://github.com/sublimehq/sublime_text/issues/299#issuecomment-757427207

class ClearConsoleCommand(sublime_plugin.WindowCommand):
    def run(self):
        a = sublime.load_settings("Preferences.sublime-settings")
        current = a.get("console_max_history_lines")
        a.set("console_max_history_lines", 1)
        print("")
        a.set("console_max_history_lines", current)
