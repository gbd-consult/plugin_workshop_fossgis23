# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RandomPointsDialog
                                 A QGIS plugin
 be random
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-02-23
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Random Corp
        email                : info@random.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
import random

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import (
    QgsFeature,
    QgsVectorLayer,
    QgsGeometry,
    QgsPointXY,
    QgsProject
)

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'random_points_dialog_base.ui'))


class RandomPointsDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, iface, parent=None):
        """Constructor."""
        super(RandomPointsDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)

        self.iface = iface
        self.crs = (
            self.iface.mapCanvas().mapSettings().destinationCrs().authid()
        )
        self.accepted.connect(self.generate_points)

    def generate_points(self):
        n = int(self.number_points_edit.text())
        extent = self.iface.mapCanvas().extent()

        crs = self.iface.mapCanvas().mapSettings().destinationCrs().authid()
        layer = QgsVectorLayer(f"Point?crs={crs}", "rnd", "memory")

        for i in range(n):
            x = random.uniform(extent.xMinimum(), extent.xMaximum())
            y = random.uniform(extent.yMinimum(), extent.yMaximum())
            feat = QgsFeature()
            feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(x, y)))
            layer.dataProvider().addFeature(feat)

        layer.commitChanges()
        layer.updateExtents()

        QgsProject.instance().addMapLayer(layer)
