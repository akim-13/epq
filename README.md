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

[^win-history]: https://www.britannica.com/technology/Windows-OS

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

Mac OS was developed by the American computer company Apple Inc. The OS was
introduced in 1984 to run the company’s Macintosh line of personal computers.
The Macintosh heralded the era of graphical user interface (GUI)
systems, and it inspired Microsoft Corporation to develop its own GUI, the
Windows OS.

In 1996 Apple acquired rival NeXT Computers, which was founded by Steve Jobs
after his departure from Apple, and in 2001 the company rolled out Mac OS X, a
major redesign based on both the NextStep system and Apple’s most recent OS
release. OS X ran on a UNIX kernel (core software code) and offered technical
advances such as memory protection and preemptive multitasking, along with a
more versatile Finder, an elegant-looking interface called Aqua, and a
convenient graphical “Dock” bar for launching frequently used
applications.[^mac-history]

[^mac-history]: https://www.britannica.com/technology/Mac-OS

Although Mac OS may be considered open source (the kernel, [BSD
subsystems](https://infomory.com/what-is/what-is-bsd-subsystem/), [browser
rendering engine WebKit](https://webkit.org/), etc.) it has a proprietary
application programming interface ([API](https://en.wikipedia.org/wiki/API)),
which is much larger than in both Linux and Windows. Consequently, it raises
the same privacy concern as discussed in the [Windows section](#windows), i.e.
collecting personal data.

Although the software side customization is more promising on Mac OS, there is
a major disadvantage to using this operating system due to the hardware
limitations. Officially Mac OS is only available for Apple devices (MacBooks,
iMacs and such), therefore in order to use it, one must be willing to use one
of the hardware configurations provided by the company. The minimum price that
has to be paid for the OS is equivalent to the price of the [cheapest official
MacBook](https://www.apple.com/macbook-air-m1/) — $999.


### Linux

In 1969, a team of developers of Bell Labs started a project to make a common
software for all the computers and named it as "Unix". It was simple and
elegant, used "C" language instead of assembly language and its code was
recyclable. As it was recyclable, a part of its code now commonly called
"kernel" was used to develop the operating system and other functions and could
be used on different systems. Also its source code was open source. 

In 1983, Richard Stallman developed GNU project with the goal to make it freely
available Unix like operating system and to be used by everyone. But his
project failed in gaining popularity. In 1991, Linus Torvalds a student at the
university of Helsinki, Finland, thought to have a freely available academic
version of Unix started writing its own code. Later this project became the
Linux kernel. He started it just for fun but ended up with such a large
project. He published the Linux kernel under his own license and was restricted
to use it commercially. Linux uses most of its tools from GNU software and are
under GNU copyright. In 1992, he released the kernel under GNU General Public
License.[^linux-history]

[^linux-history]: https://www.javatpoint.com/linux-history

Because Linux was developed as FOSS ([Free and Open Source
Software](https://en.wikipedia.org/wiki/Free_and_open-source_software)) it
abides by the four essential freedoms of free software, defined by Richard M.
Stallman in his book "Free Software, Free Society" and later adopted by the FSF
([Free Software Foundation](https://www.fsf.org/)):

> - The freedom to run the program as you wish, for any purpose (**freedom 0**).
> - The freedom to study how the program works, and change it so it does your
>    computing as you wish (**freedom 1**). Access to the source code is a
>    precondition for this.
> - The freedom to redistribute copies so you can help others (**freedom 2**).
> - The freedom to distribute copies of your modified versions to others
>    (**freedom 3**). By doing this you can give the whole community a chance to
>    benefit from your changes. Access to the source code is a precondition for
>    this.[^four-freedoms]

[^four-freedoms]: https://www.gnu.org/philosophy/free-sw.en.html#four-freedoms

These four simple principals allow Linux to resolve major issues present in
Windows and Mac OS. Firstly, there are no privacy, surveillance or data selling
concerns with Linux, due to the first freedom. Every changed setting, ran
command or any other undertaken action can be freely traced and analyzed to
ensure that it does what it is supposed to do, instead of sending user data to
a big corporation for instance.

Secondly, Linux is free and widely available. The Kernel itself is 100% free
and open source, as are most of the
[distributions](https://en.wikipedia.org/wiki/Linux_distribution). Some of them
are paid (e.g.
[RHEL](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux)),
however with [over 600 active
distributions](https://truelist.co/blog/linux-statistics/#:~:text=Today%2C%20there%20are%20over%20600%20active%20Linux%20distros.,-Another%20500%20are&text=Some%20of%20the%20most%20commonly,Linux%20distribution%20usage%20statistics%20show.)
the proportion of the proprietary ones is negligible.

There are no special limiting hardware requirements either. In fact, it runs
90% of the public cloud workload, has 62% market share of embedded operating
systems (from smart fridges to cars and airplanes), 99% of the supercomputer
market share and 82% of all smartphones run on Linux.[^linux-market] This
allows for maximum hardware customizability, i.e. almost any laptop or even a
self-assembled PC, no matter how cheap, expensive, old or new, can run this OS
absolutely for free.

[^linux-market]: https://www.rackspace.com/en-gb/blog/realising-the-value-of-cloud-computing-with-linux

Finally, one of the most significant "selling" points of Linux is its endless
software customization capabilities. There is not a single thing that cannot be
modified in this OS. Because the source code is open source, even the most
fundamental parts such as the Kernel can be altered, recompiled and freely put
into production. This allows for a maximum degree of flexibility both in terms
of technical details (e.g. system security) and general aesthetics (e.g. the
overall look and feel). Figure 5 shows examples of how Linux users customized
their OS.

| ![Linux rice 1](https://preview.redd.it/ptbibz0gdk861.png?width=640&crop=smart&auto=webp&s=49ae9646b1ccb7ec27a63a23381d144ae3219994) | ![Linux rice 2](https://preview.redd.it/4ew694tuiud81.jpg?width=640&crop=smart&auto=webp&s=919d90f9141b0f3392b70c5200e29e61eae9b347) |
|--- | --- |
|![Linux rice 3](https://preview.redd.it/ajgofc7utfz51.png?width=640&crop=smart&auto=webp&s=2e408335f8e6533281e34d86fd627e5c379e85b2) | ![Linux rice 4](https://preview.redd.it/5mjm5s90e7m41.png?width=640&crop=smart&auto=webp&s=52cf43dae248f57fb1fc23053944bc94878489ca) |

*<p align="center"> Figure 5 </p>*

*However, Linux is bad because reasons...*

## Which Linux?
