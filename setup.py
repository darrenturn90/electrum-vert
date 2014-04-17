#!/usr/bin/python

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp


version = imp.load_source('version', 'lib/version.py')
util = imp.load_source('version', 'lib/util.py')

if sys.version_info[:3] < (2, 6, 0):
    sys.exit("Error: Electrum requires Python version >= 2.6.0...")

usr_share = '/usr/share'
if not os.access(usr_share, os.W_OK):
    usr_share = os.getenv("XDG_DATA_HOME", os.path.join(os.getenv("HOME"), ".local", "share"))

data_files = []
if (len(sys.argv) > 1 and (sys.argv[1] == "sdist")) or (platform.system() != 'Windows' and platform.system() != 'Darwin'):
    print "Including all files"
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-vert.desktop']),
        (os.path.join(usr_share, 'app-install', 'icons/'), ['icons/electrum-vert.png'])
    ]
    if not os.path.exists('locale'):
        os.mkdir('locale')
    for lang in os.listdir('locale'):
        if os.path.exists('locale/%s/LC_MESSAGES/electrum.mo' % lang):
            data_files.append((os.path.join(usr_share, 'locale/%s/LC_MESSAGES' % lang), ['locale/%s/LC_MESSAGES/electrum.mo' % lang]))

appdata_dir = util.appdata_dir()
if not os.access(appdata_dir, os.W_OK):
    appdata_dir = os.path.join(usr_share, "electrum-vert")

data_files += [
    (appdata_dir, ["data/README"]),
    (os.path.join(appdata_dir, "cleanlook"), [
        "data/cleanlook/name.cfg",
        "data/cleanlook/style.css"
    ]),
    (os.path.join(appdata_dir, "sahara"), [
        "data/sahara/name.cfg",
        "data/sahara/style.css"
    ]),
    (os.path.join(appdata_dir, "dark"), [
        "data/dark/name.cfg",
        "data/dark/style.css"
    ])
]


setup(
    name="Electrum-VTC",
    version=version.ELECTRUM_VERSION,
    install_requires=['slowaes', 'ecdsa>=0.9', 'vert_scrypt'],
    package_dir={
        'electrum_vert': 'lib',
        'electrum_vert_gui': 'gui',
        'electrum_vert_plugins': 'plugins',
    },
    scripts=['electrum-vert'],
    data_files=data_files,
    py_modules=[
        'electrum_vert.account',
        'electrum_vert.bitcoin',
        'electrum_vert.blockchain',
        'electrum_vert.bmp',
        'electrum_vert.commands',
        'electrum_vert.daemon',
        'electrum_vert.i18n',
        'electrum_vert.interface',
        'electrum_vert.mnemonic',
        'electrum_vert.msqr',
        'electrum_vert.network',
        'electrum_vert.plugins',
        'electrum_vert.pyqrnative',
        'electrum_vert.scrypt',
        'electrum_vert.simple_config',
        'electrum_vert.socks',
        'electrum_vert.transaction',
        'electrum_vert.util',
        'electrum_vert.verifier',
        'electrum_vert.version',
        'electrum_vert.wallet',
        'electrum_vert.wallet_bitkey',
        'electrum_vert_gui.gtk',
        'electrum_vert_gui.qt.__init__',
        'electrum_vert_gui.qt.amountedit',
        'electrum_vert_gui.qt.console',
        'electrum_vert_gui.qt.history_widget',
        'electrum_vert_gui.qt.icons_rc',
        'electrum_vert_gui.qt.installwizard',
        'electrum_vert_gui.qt.lite_window',
        'electrum_vert_gui.qt.main_window',
        'electrum_vert_gui.qt.network_dialog',
        'electrum_vert_gui.qt.password_dialog',
        'electrum_vert_gui.qt.qrcodewidget',
        'electrum_vert_gui.qt.receiving_widget',
        'electrum_vert_gui.qt.seed_dialog',
        'electrum_vert_gui.qt.transaction_dialog',
        'electrum_vert_gui.qt.util',
        'electrum_vert_gui.qt.version_getter',
        'electrum_vert_gui.stdio',
        'electrum_vert_gui.text',
        'electrum_vert_plugins.aliases',
        'electrum_vert_plugins.exchange_rate',
        'electrum_vert_plugins.labels',
        'electrum_vert_plugins.pointofsale',
        'electrum_vert_plugins.qrscanner',
        'electrum_vert_plugins.virtualkeyboard',
    ],
    description="Lightweight Vertcoin Wallet",
    author="ecdsa",
    author_email="ecdsa@github",
    license="GNU GPLv3",
    url="http://electrum.org",
    long_description="""Lightweight Vertcoin Wallet"""
)
