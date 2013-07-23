import csv
import os

class Group():
    def __init__(self, t = ''):
        self.title = t
        self.headings = list()
        self.items = list()
    
    def total_points(self):
        sum = 0
        for i in self.items:
            sum = sum + i.points
        return sum
    
    def add(self, columns, points):
        self.items.append(Item(columns, points))
    
    def latex(self):
        s = '\\textbf{%s}\n\n' % self.title
        aname = self.title.replace(' ','').lower()
        tstr = 'c'
        for i in range(1, len(self.headings)):
            tstr += 'c'
        tstr += 'Xcc'
        s += '\\begin{tabularx}{\\textwidth}{%s}\n' % tstr
        s += '\\toprule[1.5pt]\n'
        s += '\\textbf{\\#}'
        for h in self.headings:
            s+= ' & \\textbf{%s}' % h
        s += ' & \\textbf{Rec} & \\textbf{Poss}\\\\\n'
        s += '\\toprule[1.5pt]\n'
        for i in range(0,len(self.items)):
            s += str(i + 1)
            for c in self.items[i].columns:
                s += ' & %s' % c
            s += ' & \\' + aname + '(' + str(i) + ') & %d \\\\ ' % self.items[i].points
            if i == len(self.items) - 1:
                s += '\n'
            else:
                s += '\\midrule \n'
        s += '\\toprule[1.5pt]\n'
        s += '\\multicolumn{%d}{c}{\\textbf{TOTAL}} & \\%s(total) & \\textbf{%d} \\\\\n' % (len(self.headings) + 1, aname, self.total_points())
        s += '\\bottomrule[1pt]\n'
        s += '\\end{tabularx}\n'
        return s
    


class Rubric():
    def __init__(self, t, c, s):
        self.title = t
        self.course = c
        self.semester = s
        self.groups = list()
    
    def frontmatter(self):
        fm = r"""\documentclass[10pt]{article}
\usepackage{arrayjobx}
\usepackage{booktabs}
\usepackage{fancyhdr}
\usepackage[left=.5in,right=.5in,top=.5in,bottom=.75in,includehead,includefoot]{geometry}
\usepackage[parfill]{parskip}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage[usenames,dvipsnames]{color}

\definecolor{LightGray}{gray}{.5}

\usepackage[T1]{fontenc}
\usepackage{helvet}
\renewcommand*\familydefault{\sfdefault}

\newarray\docinfo
\readarray{docinfo}{%s&%s&%s}
\newcommand{othervars}{}

\newcommand{\class}{\docinfo(1)}
\newcommand{\semester}{\docinfo(2)}
\newcommand{\doctitle}{\docinfo(3)}
\newcommand{\firstname}{}
\newcommand{\lastname}{}
\newcommand{\comments}{}

\linespread{1.4}

\lhead{\small\textbf{\class}}
\rhead{\small\textbf{\semester}}
\rfoot{}
\cfoot{}
\lfoot{\footnotesize \color{LightGray} \textbf{SAVE THIS PAPER!} It is your submission receipt, and the only proof of your grade. Any corrections or appeals of grades must be made in writing no later than \textbf{one week} after it is returned to you.}

\pagestyle{fancyplain}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\begin{document}
\begin{tabularx}{\textwidth}{lX}
\multirow{2}{*}{\textbf{\Huge \doctitle}\hspace*{1em}} & \textbf{First Name\hspace*{1em}}\firstname \\
\cmidrule[1pt](l){2-2}		
& \textbf{Last Name\hspace*{1em}}\lastname \\
\cmidrule[1pt](l){2-2}
\end{tabularx}
\smallskip

""" % (self.course, self.semester, self.title)
        return fm
    
    def backmatter(self):
        s = r"""
\vfill
\begin{tabularx}{\textwidth}{Xl}
\textbf{Grader Signature} & \textbf{Date\hspace*{1em}}\today\\
\bottomrule[1pt]
\end{tabularx}
\end{document}"""
        return s
    
    def add(self,g):
        self.groups.append(g)
    
    def total_points(self):
        p = 0
        for g in self.groups:
            if g.total_points() > 0:
                p += g.total_points()
        return p
    
    def latex(self):
        s = self.frontmatter()
        l = self.groups[-1]
        for g in self.groups:
            if g == l:
                t = g.latex().replace('\\end{tabularx}','')
                t += r"""& & & \\
\cmidrule[1.5pt]{3-4}
\multicolumn{2}{l}{\multirow{2}{*}{\parbox{45em}{\textbf{\hspace*{1em}}\small\comments}}} & \multicolumn{2}{c}{\textbf{TOTAL}} \\
\cmidrule[1.5pt]{3-4}
& & \fulltotal & \textbf{%d} \\
\cmidrule[1pt]{3-4}
\end{tabularx}

""" % self.total_points()
                s += t
            else:
                s += g.latex()
                s += '\n\\bigskip'                
        s += self.backmatter()
        return s
    

class Item():
    def __init__(self, c = list(), p = 0):
        self.columns = c
        self.points = p
    
    def __str__(self):
        return '%d columns, %d points' % (len(self.columns), self.points)
    
    
    def __unicode__(self):
        return '%d columns, %d points' % (len(self.columns), self.points)
    

class Report():
    def __init__(self, r=None, f=''):
        self.first_name = ''
        self.last_name = ''
        self.rubric = r
        self.filename = f
    
    def generate(self):
        reader = csv.reader(open(self.filename,'rb'), delimiter=',')
        la = ''
        for row in reader:
            total = ''
            self.first_name = row[0]
            self.last_name = row[1]
            la = self.rubric.latex()
            la = la.replace(r"\newcommand{\firstname}{}",r"\newcommand{\firstname}{%s}" % self.first_name)
            la = la.replace(r"\newcommand{\lastname}{}",r"\newcommand{\lastname}{%s}" % self.last_name)
            gs = ''
            rtotal = 2
            for g in self.rubric.groups:
                gtotal = ''
                gn = g.title.replace(' ','').lower()
                gs += '\\newarray\\%s\n' % gn
                gs += '\\readarray{%s}{' % gn
                ni = len(g.items)
                for i in range(0,ni):
                    gs += "%s&" % row[rtotal]
                    # gtotal += int(row[rtotal])
                    rtotal += 1
                gs += '}\n'
                la = la.replace("\\%s(total)" % gn, str(gtotal))
                # total += gtotal
            la = la.replace(r"\newcommand{othervars}{}",gs)
            la = la.replace(r"\fulltotal", str(total))
            f = open('Reports/%s - %s, %s.tex' % (self.rubric.title, self.last_name, self.first_name),'w')
            f.write(la)
            f.close()
            os.system("find Reports/ -name *.tex -exec pdflatex --interaction=batchmode -output-directory=PDFs {} \;")
            # os.system("open PDFs/*.pdf")
    
