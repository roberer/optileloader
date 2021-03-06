# -*- coding: utf-8 -*-
"""
/***************************************************************************
 OPTileLoader
                                 A QGIS plugin
 Load Mars and The Moon basemaps
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-12-29
        copyright            : (C) 2021 by Rober J
        email                : roberer_@outlook.es
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
    """Load OPTileLoader class from file OPTileLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .optileloader import OPTileLoader
    return OPTileLoader(iface)
