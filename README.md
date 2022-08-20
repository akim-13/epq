# Linux: an OS You Control

## Table of Contents
- [Abstract](#abstract)
- [Remarks](#remarks)
  * [Format](#format)
  * [Activity Logging](#activity-logging)
- [Introduction](#introduction)

## Abstract

## Remarks
### Format
The following project will be made entirely in a Markdown format. From the
official website:

> Markdown is a lightweight markup language that you can use to add formatting
elements to plaintext text documents.

Markdown is mostly used for simple tasks where minimal formatting is needed,
e.g. emails, technical documentations or notes. Consequently, it might be
argued that such a format is inappropriate for an extensive academic project,
such as this one. 

However, every issue that may be encountered has been carefully considered and
accounted for. Moreover, this format brings some substantial benefits over
standard solutions (PDF, DOCX, etc.) to both the author and the readers,
namely:

- **Interactivity**
    - Video demonstrations are necessary for showcasing the OS at work
    - External links make it easier to link sources of information
    - Internal links make traversing the document effortless
- **Minimalistic design**
    - Easier editing
    - Better readability
- **Accessibility**
    - This document is hosted on [GitHub](https://github.com/) where Markdown
      is neatly integrated for viewing and accessing such projects

### Activity Logging
Thorough logging of every undertaken action is both a requirement and a big
part of the project. The initial solution was to write a [custom Python
program](activity.py) called the *Activity Logger* to provide an all-in-one
[file](activity.log) with activities as plain text entries:

```
    _        _   _       _ _            _                                    
   / \   ___| |_(_)_   _(_) |_ _   _   | | ___   __ _  __ _  ___ _ __       
  / _ \ / __| __| \ \ / / | __| | | |  | |/ _ \ / _` |/ _` |/ _ \ __|   
 / ___ \ (__| |_| |\ V /| | |_| |_| |  | | (_) | (_| | (_| |  __/ |        
/_/   \_\___|\__|_| \_/ |_|\__|\__, |  |_|\___/ \__, |\__, |\___|_|
                               |___/            |___/ |___/                  
Creator: Akim                                                                
Source code: https://github.com/akim/epq
                                  
Tags:                                                                        
( A ) - Activity                                                             
( D ) - Description                                                          
( F ) - Fixed                                                                
(I__) - Issue                                                                
(W__) - Warning
                                                            
=====================================================================
      
[10-12-2021 19:12] ( A ) Downloaded the Arch Linux ISO file
[10-12-2021 19:25] ( A ) Verfied the image signature using gpg
[10-12-2021 19:33] ( A ) `dd`-ed the image to a usb drive
[10-12-2021 19:51] (I01) Cannot boot into the live environment
  [11-12-2021 18:08] ( F ) Reformatted the usb and reinstalled the iso
[11-12-2021 18:08] ( A ) Fixed I01
  [11-12-2021 18:08] ( D ) The iso might have been corrupted
[11-12-2021 18:08] ( A ) Added a description to A24
[11-12-2021 18:13] ( A ) Connected to wifi using iwctl
[11-12-2021 18:21] ( A ) Created a LUKS encrypted container
[11-12-2021 18:50] ( A ) Made and formatted the logical volumes (LVM)
[11-12-2021 19:04] ( A ) Mounted the file systems
...
```
Nevertheless, this solution has proved to be unsustainable in the long run, as
the program needed to be improved and maintained, which put a significant, but
more importantly an unnecessary, extra load.

A better solution turned out to be the use of an already existing and utilised
system — GitHub. At its core, GitHub is a website and cloud-based service for
sharing code, which incorporates a [Version Control
System](https://en.wikipedia.org/wiki/Version_control) (VCS) called
[git](https://git-scm.com/). 

This system provides an extremely detailed breakdown of every little change in
the system, right down to a side-to-side comparison of every altered line of
code *(fig. 1)*. Yet understandability remains unharmed, as all the changes can
be presented with a short description on a simple timeline *(fig. 2)*, thus
each aspect of this solution has been proven to be superior to the previous
one.

![Git comparison](./attachments/1.png) 
*<p align="center"> Figure 1 </p>*

![Git timeline](./attachments/2.png)
*<p align="center"> Figure 2 </p>*

# Why Linux?
There are three major Operating Systems (OSs) *(fig 3)*:
1. Windows
2. Mac OS
3. Linux

The most popular one OS by far is Windows, accounting for roughly 70% of global
market share. It is aimed to be compatible with as many devices as possible,
hence it is a go-to choice of all major PC/laptop manufacturers.

On the second place is Mac OS at around 15% market share.



![OSs bar chart](./attachments/oss.png) 
*<p align="center"> Figure 3 </p>*



# Which Linux?
