import os
ooo=os.listdir('/home/pet/kdocs')
#everything is read into list ooo
ooo.sort()#sorted items are easier to locate

print ooo

#os.makedirs("./docbook-kdocs")

f=open("./kdocs.xml","w");
head_shit= """
<?xml version="1.0" encoding="UTF-8"?>
 <!DOCTYPE book PUBLIC "-//OASIS//DTD DocBook XML V4.2//EN" "http://docbook.org/xml/4.2/docbookx.dtd">
 <book>
      <title>kdocs</title>
<titleabbrev>everything about tinylion</titleabbrev>
<bookinfo>
<legalnotice>
<para>Here you get everything about Project tinylion.

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.1 or any later version published by the Free Software Foundation;
 with the Back-Cover Texts being Back Cover Text.
</para>
</legalnotice>
<author>
<firstname>Peter</firstname><surname>King</surname>
</author>
</bookinfo>

<dedication>
<para>
For Billie, you are my life!
</para>
</dedication>
<preface>
<title>Forword</title>
<para>
I want to start this by recalling the how stupid I was to backup my documentation and notes.
Two years ago, I used a blog to backup my data, it got messy while more and more articles is added, and it was basiclly impossible to do changes, since there is no revision control.
later, I tried google doc for a while and it is nice.
now I use github and I like it so much.
But finally I decide only to keep the unstable stuff in github, and everything
I consider is not to be changed much will be do as docbook files, such like project Tinylion.
</para>
</preface>
"""
f.write(head_shit)
