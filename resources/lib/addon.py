# -*- coding: utf-8 -*-
# GNU General Public License v3.0 (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, unicode_literals
import logging
import routing

from Exceptions import Exceptions
from Yelo import Yelo

_LOGGER = logging.getLogger('plugin')
plugin = routing.Plugin()

# instantiate yelo object
yelo = Yelo()


@plugin.route('/')
def main_menu():
    yelo.list_channels()


@plugin.route('/play/id/<uniqueName>')
def play(uniqueName):
    try:
        yelo.play(uniqueName)
    except Exceptions.YeloException as exc:
        _LOGGER.error(exc)


@plugin.route('/iptv/channels')
def iptv_channels():
    from iptvmanager import IPTVManager
    port = int(plugin.args['port'][0])
    IPTVManager(port).send_channels(yelo)


@plugin.route('/iptv/epg')
def iptv_epg():
    from iptvmanager import IPTVManager
    port = int(plugin.args['port'][0])
    IPTVManager(port).send_epg(yelo)


def run(args):
    plugin.run(args)
