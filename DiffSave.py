import sublime
import sublime_plugin
import os.path
import difflib



def ds_settings():
	return sublime.load_settings( 'Preferences.sublime-settings' )

class dsController():
	def get_view_contents( self, view ):
		selection = sublime.Region( 0, view.size() )
		content = view.substr( selection )
		return content


class dsDiffSaveCommand(sublime_plugin.TextCommand, dsController):
	def run(self, edit):

		workingView = sublime.active_window().active_view()
		workingCopy = self.get_view_contents( workingView )
		filePath = workingView.file_name()

		linesA = workingCopy.splitlines( False )
		fh = open(filePath)
		linesB = [line.rstrip() for line in fh.readlines()]
		fh.close()

		diff = difflib.ndiff( linesA, linesB, linejunk = None, charjunk = None )

		sublime.active_window().run_command( 'new_window' )
		win = sublime.active_window()
		win.set_layout( { "cols": [0.0, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [0, 0, 1, 1]] } )

		if ds_settings().get( 'toggle_sidebar', False ):
			win.run_command( 'toggle_side_bar' )
		if ds_settings().get( 'toggle_menu', False ):
			win.run_command( 'toggle_menu' )

		newView = win.active_view()
		newView.set_scratch(1)
		newView.set_syntax_file("Packages/Diff/Diff.tmLanguage");

		newView.insert(edit, 0, '\n'.join( diff ))
