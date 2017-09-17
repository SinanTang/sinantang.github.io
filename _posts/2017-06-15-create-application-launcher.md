---
title: How to create an application launcher (Linux) 
date: 2017-06-15
categories:
- Linux Tips
tags:
- Linux
- Unix
---

This post applies to Linux Red Hat (and probably some other Linux versions too).

If you want to create an application launcher for, for example, Eclipse so you can launch it much faster, you can follow this step-by-step tutorial. 

.

Open a txt editor, and copy the following information to your file, edit the path so it applies to your case:

> ```
> [Desktop Entry]
> Encoding=UTF-8
> Name=Eclipse IDE
> Exec=/home/USER/programs/eclipse/eclipse
> Icon=/home/USER/programs/eclipse/eclipse.png
> Type=Application
> Categories=Development;IDE;
> ```

You can download the icon from the offical site if you don't have it ready.

.

Save this file to `/home/YOUR_USER/.local/share/applications/eclipse.desktop`. Note the extension of the file name is `.desktop`.

> If you don't see the hidden folders (folder name starts with '.'), type `Ctrl+H` to display them.



This file should change to the icon of the desktop file.