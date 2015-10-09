#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin


class LnToggleDisplayCommand(sublime_plugin.TextCommand):

    def run(self, edit, **kwargs):
        action = kwargs['action'].upper()
        view = self.view
        my_id = self.view.id()

        settings = view.settings()

        if action == 'WHITE_SPACE':
            propertyName, propertyValue1, propertyValue2 = "draw_white_space", "all", "selection"

        elif action == 'GUTTER':
            propertyName, propertyValue1, propertyValue2 = "gutter", False, True

        elif action == 'LINE_NO':
            propertyName, propertyValue1, propertyValue2 = "line_numbers", False, True
            # propertyName = "line_numbers"

        elif action == 'INDENT_GUIDE':
            propertyName, propertyValue1, propertyValue2 = "draw_indent_guides", False, True

        else:
            propertyValue = None

        if propertyName:
            propertyValue = propertyValue1 if settings.get(
                propertyName, propertyValue1) != propertyValue1 else propertyValue2
            settings.set(propertyName, propertyValue)

    def is_checked(self, **kwargs):
        action = kwargs['action'].upper()
        if action == "WHITE_SPACE":
            sett = self.view.settings().get("draw_white_space")
            if sett == "all":
                return True
            return False
        if action == "LINE_NO":
            return self.view.settings().get("line_numbers")
        if action == "GUTTER":
            return self.view.settings().get("gutter")
        if action == "INDENT_GUIDE":
            return self.view.settings().get("draw_indent_guides")