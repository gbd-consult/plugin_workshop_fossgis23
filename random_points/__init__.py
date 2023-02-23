# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RandomPoints
                                 A QGIS plugin
 be random
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-02-23
        copyright            : (C) 2023 by Random Corp
        email                : info@random.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RandomPoints class from file RandomPoints.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .random_points import RandomPoints
    return RandomPoints(iface)