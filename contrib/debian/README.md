
Debian
====================
This directory contains files used to package mued/mue-qt
for Debian-based Linux systems. If you compile mued/mue-qt yourself, there are some useful files here.

## mue: URI support ##


mue-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install mue-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your mue-qt binary to `/usr/bin`
and the `../../share/pixmaps/mue128.png` to `/usr/share/pixmaps`

mue-qt.protocol (KDE)

