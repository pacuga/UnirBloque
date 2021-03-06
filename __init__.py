# -*- coding: utf-8 -*-
"""
/***************************************************************************
 AumentarBuffer
                                 A QGIS plugin
 Añade aleros a una construcción catastral
                             -------------------
        begin                : 2017-04-03
        copyright            : (C) 2017 by seresco
        email                : pablo.cuadrado@seresco.es
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
    """Load AumentarBuffer class from file AumentarBuffer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .AumentarBuffer import AumentarBuffer
    return AumentarBuffer(iface)
