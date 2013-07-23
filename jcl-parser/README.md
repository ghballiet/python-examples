# JCL Parser #

At one of my previous jobs, I wrote a quick parser for 
[Job Control Language][jcl] which could read a JCL file 
and determine what jobs were spawned, and which days they ran.

The final version of this parser actually does quite a bit more than that; it
generates color coded GraphViz documents (PDFs) that are searchable and
organized, illustrating the entire job flow over a period of days. 

I could not include that code here, because I no longer have it - it is still
being used at the company I was working for when I wrote it, and it's
considered proprietary information.

[jcl]: http://en.wikipedia.org/wiki/Job_Control_Language