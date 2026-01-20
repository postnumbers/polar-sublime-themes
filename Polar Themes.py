import re
import sublime
import sublime_plugin

class ActivatePolarThemeCommand(sublime_plugin.TextCommand):
    def run(self, action):

        names = [
            "Polar",
            "Polar Dark",
        ]
        self.themes = [
            "Packages/User/Polar Themes/themes/Polar Adaptive",
            "Packages/User/Polar Themes/themes/Polar Adaptive",
        ]
        self.schemes = [
            "Packages/User/Polar Themes/schemes/Polar.sublime-color-scheme",
            "Packages/User/Polar Themes/schemes/Polar Dark.sublime-color-scheme",
        ]

        self.view.window().show_quick_panel(names, self.on_done, on_highlight=self.on_highlighted)

    def on_done(self, index):
        scheme = self.schemes[index]
        theme = self.themes[index]
        self.set_scheme(scheme)
        self.set_theme(theme)
        self.save_settings(theme)

    def on_highlighted(self, index):
        scheme = self.schemes[index]
        theme = self.themes[index]
        self.set_scheme(scheme)
        self.set_theme(theme)

    def set_scheme(self, scheme):
        self.get_settings().set('color_scheme', scheme)

    def set_theme(self, theme):
        self.get_settings().set('theme', theme)

    def get_settings(self):
        return sublime.load_settings('Preferences.sublime-settings')

    def save_settings(self, theme):
        sublime.save_settings('Preferences.sublime-settings')
        sublime.status_message('Polar: ' + theme)
        print('')
        print('[Polar] ' +  theme)
        print('')
