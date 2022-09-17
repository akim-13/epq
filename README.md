# Linux: an OS You Control

## Table of Contents
* [Abstract](#abstract)
* [Remarks](#remarks)
  + [Format](#format)
  + [Activity Logging](#activity-logging)
* [Why Linux?](#why-linux)
  + [Operating Systems](#operating-systems)
  + [Windows](#windows)
  + [Mac OS](#mac-os)
  + [Linux](#linux)
* [Which Linux?](#which-linux)

## Abstract

## Remarks
### Format
The following project will be made entirely in a Markdown format. From the
official website:

> **Markdown** is a lightweight markup language that you can use to add formatting
> elements to plaintext text documents.[^md]

[^md]: https://www.markdownguide.org/getting-started/

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

![Git comparison](./attachments/git-diff.png) 
*<p align="center"> Figure 1 </p>*

![Git timeline](./attachments/git-timeline.png)
*<p align="center"> Figure 2 </p>*

## Why Linux?
### Operating Systems
> An **Operating System (OS)** is an interface between a computer user and
> computer hardware *(fig. 3)*. It is a software which performs all the basic tasks like
> file management, memory management, process management, handling input and
> output, and controlling peripheral devices such as disk drives and
> printers.[^os-def]

[^os-def]: https://www.tutorialspoint.com/operating_system/os_overview.htm

![OS definition](./attachments/os_def.png) 
*<p align="center"> Figure 3 </p>*

There are three major OSs in the current market *(fig. 4)*:
1. Windows
2. Mac OS
3. Linux

The most popular one OS by far is Windows, accounting for roughly 70% of global
market share. It is aimed to be compatible with as many devices as possible,
hence it is a go-to choice of all major PC/laptop manufacturers.

In second place is Mac OS at around 15% market share. Although it is only
available for laptops produced by Apple, with [over 20 million units sold
annually](https://www.macrumors.com/2021/01/19/mac-sales-skyrocketing-after-m1-launch/),
big market share is not a surprise.

However, Linux, being free and compatible with almost all of the devices
running Windows or Mac OS, comprises only 2-3% of the current market. To
understand why that is, a deeper understanding of each OS is needed.


![OSs bar chart](./attachments/oss.png) 
*<p align="center"> Figure 4 </p>*

### Windows
The first version of Windows, released in 1985, was simply a GUI offered as an
extension of Microsoft’s existing disk operating system, or MS-DOS. Based in
part on licensed concepts that Apple Inc. had used for its Macintosh System
Software, Windows for the first time allowed DOS users to visually navigate a
virtual desktop, opening graphical “windows” displaying the contents of
electronic folders and files with the click of a mouse button, rather than
typing commands and directory paths at a text prompt.[^win-history]

[^win-history]: https://www.britannica.com/technology/Palm-OS

In subsequent years the functionality of the OS gradually expanded, whilst most
of the complexity behind it remained unseen by an average user. This approach
appealed to many people around the World, and soon Windows became the most
widely used desktop OS in the market. 

Nonetheless, the convenience of being pre-installed on most of the devices,
pre-configured and relatively straightforward
[GUI](https://en.wikipedia.org/wiki/Graphical_user_interface) and just the fact
of being an
[off-the-shelf](https://en.wikipedia.org/wiki/Commercial_off-the-shelf)
software, comes at a price. Both figuratively and literally.

At the time of writing, the price of the full and latest Windows version for an
individual is
[$199.99](https://www.microsoft.com/en-us/d/windows-10-pro/df77x4d43rkt/48dn?rtc=1&activetab=pivot:overviewtab).
Although it is possible to use a newly bought Windows laptop without
explicitly paying such a high price, the functionality of the OS will be
severely constrained (e.g. unable to set a custom wallpaper). Consequently, the
cost of the OS is usually paid indirectly, because it is included in the price
of a device, or directly through Microsoft store in order to activate the
product.

Furthermore, to appeal to [almost 1.5 billion
people](https://news.microsoft.com/bythenumbers/en/windowsdevices), a multitude
of immutable decisions must be made for them by the system developers, which
might not be in the best interest of the people themselves. For instance, the
general look of the GUI, the core services used or even the
[kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system)). Allowing to
alter something that has been permanently set by the developers would most
likely harm the compatibility, stability and security of the system, and
increase the configuration complexity for an end-user. None of the above seem
to be beneficial for such a huge business, therefore the amount of available
customisation is substantially limited.

However, a far dangerous, albeit less noticeable in the short term, price is
one's privacy. Microsoft is known to collect hundreds upon hundreds of [data
entries](https://igotoffer.com/microsoft/what-data-does-microsoft-collect),
such as installed applications, hardware/device information, browsing, search
and query data, details about the voice and typing input features. If you ever
wondered how the internet ads match exactly the topic of conversation that you
recently had with your friend, relative or college, this is one of the reasons.
The main motivation behind collecting such sensitive personal information is
to:

> - Personalise our products and make recommendations.
> - Advertise and market to you, which includes sending promotional
>   communications, targeting advertising, and presenting you with relevant
>   offers.[^ads]

[^ads]: https://privacy.microsoft.com/en-gb/privacystatement

This also serves as a big source of system diagnostics, which is used for
development and improvement. Nonetheless, if the consumers were actually aware
that in order to use the OS every little action they take would have to be
under constant surveillance, such shady business model would have been very
unlikely to succeed on the global market.

### Mac OS


### Linux


## Which Linux?
