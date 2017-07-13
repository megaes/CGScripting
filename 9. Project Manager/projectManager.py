#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os, webbrowser, shutil
from PySide.QtGui import *
from widgets import projectManager_UI as ui, projectListWidget
import settingsDialog, createProjectDialog, templateEditor, settings, createProject


class ProjectManagerClass(QMainWindow, ui.Ui_projectManager):
    def __init__(self):
        super(ProjectManagerClass, self).__init__()
        self.setupUi(self)

        # widgets
        self.projectList_lwd = projectListWidget.ProjectListClass()
        self.projectList_ly.addWidget(self.projectList_lwd)

        # connects
        self.create_btn.clicked.connect(self.create_project)
        self.refresh_btn.clicked.connect(self.update_list)
        self.settings_btn.clicked.connect(self.open_settings_dialog)
        self.templateEditor_btn.clicked.connect(self.open_template_editor_dialog)
        self.projectList_lwd.itemClicked.connect(self.show_info)
        self.projectList_lwd.itemDoubleClicked.connect(self.openProject)
        self.archive_btn.clicked.connect(lambda: self.archiveProject(self.getFocusedProject()))
        self.openArchive_btn.clicked.connect(lambda: self.openFolder('archive'))
        self.openBackup_btn.clicked.connect(lambda: self.openFolder('backup'))

        # start
        self.update_list()
        self.info_lb.setText('')

    def update_list(self):
        if not self.projectList_lwd.update_project_list():
            self.create_btn.setEnabled(0)
        else:
            self.create_btn.setEnabled(1)

    def open_settings_dialog(self):
        # Modal window
        self.dial = settingsDialog.SettingsDialogClass(self)
        if self.dial.exec_():
            data = self.dial.get_table_data()
            settings.SettingsClass().save(data)
        self.update_list()

    def open_template_editor_dialog(self):
        # Modeless window
        self.dial = templateEditor.TemplateEditorClass()
        self.dial.show()

    def create_project(self):
        # Modal window
        self.dial = createProjectDialog.CreateProjectDialogClass(self)
        if self.dial.exec_():
            data = self.dial.getDialogData()
            createProject.createProject(data)
            self.update_list()

    def show_info(self, item):
        info = createProject.getProjectInfo(item.data(32))
        if info:
            text = """Name:
{0}

Comment:
{1}
""".format(info['name'], info['comment'])
        else:
            text = ''
        self.info_lb.setText(text)

    def openProject(self, item):
        path = item.data(32)
        webbrowser.open(path)

    def getFocusedProject(self):
        item = self.projectList_lwd.currentItem()
        return item

    def archiveProject(self, item):
        old_path = item.data(32)
        project_name = os.path.split(old_path)[-1]
        archive_folder = settings.SettingsClass().load()['archive']
        new_path = os.path.join(archive_folder, project_name)
        if os.path.exists(new_path):
            pass
        else:
            shutil.move(old_path, new_path)
        self.update_list()

    def openFolder(self, folder):
        try:
            path = settings.SettingsClass().load()[folder]
            if not os.path.exists(path):
                os.mkdir(path)
            webbrowser.open(path)
        except KeyError:
            pass


if __name__ == '__main__':
    app = QApplication([])
    w = ProjectManagerClass()
    w.show()
    app.exec_()
