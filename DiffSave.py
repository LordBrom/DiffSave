import sublime
import sublime_plugin
import os.path
import difflib



def ds_settings():
	return sublime.load_settings( 'Preferences.sublime-settings' )

class dsController():
	def get_commit_scope(self):
		s = sublime.load_settings('Preferences.sublime-settings')
		




class dsTestCommand(sublime_plugin.TextCommand, svnController):
	def run(self, edit):
		print('starting test command')





		print('ending test command')


