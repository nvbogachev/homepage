+++
date = "2017-01-01T00:00:00"
title = "Example Talk"
abstract = ""
abstract_short = ""
event = "Hugo Academic Theme Conference"
event_url = "https://example.org"
location = "London, United Kingdom"

selected = false
math = true

url_pdf = ""
url_slides = ""
url_video = ""

# Optional featured image (relative to `static/img/` folder).
[header]
image = "headers/bubbles-wide.jpg"
caption = "My caption :smile:"

+++

Embed your slides or video here using [shortcodes](https://gcushen.github.io/hugo-academic-demo/post/writing-markdown-latex/). Further details can easily be added using *Markdown* and $\rm \LaTeX$ math code. 


\documentclass[14pt,a4paper]{moderncv}

% moderncv themes
%\moderncvtheme[blue]{casual}                 % optional argument are 'blue' (default), 'orange', 'red', 'green', 'grey' and 'roman' (for roman fonts, instead of sans serif fonts)
\moderncvtheme[blue]{classic}                % idem
\usepackage{a4wide,amsmath,pxfonts}
\usepackage[colorlinks, citecolor=orange,unicode]{hyperref}
%\usepackage[T1]{fontenc}
% character encoding
\usepackage[utf8x]{inputenc}                   % replace by the encoding you are using
%\usepackage[croatian]{babel}

% adjust the page margins
\usepackage[scale=0.8]{geometry}
\recomputelengths                             % required when changes are made to page layout lengths

%\fancyfoot{} % clear all footer fields
%\fancyfoot[LE,RO]{\thepage}           % page number in "outer" position of footer line
%\fancyfoot[RE,LO]{\footnotesize } % other info in "inner" position of footer line




% personal data
\firstname{Nikolay V.} 
\familyname{\\ Bogachev}


\title{Curriculum Vitae}               % optional, remove the line if not wanted
%\address{<Address Street>}{<Addres Place>}    % optional, remove the line if not wanted
\mobile{+79168147191}                    % optional, remove the line if not wanted
%\phone{<Phone number>}                      % optional, remove the line if not wanted
%\fax{<Fax number>}                          % optional, remove the line if not wanted
\email{nvbogach@mail.ru}                      % optional, remove the line if not wanted
%\extrainfo{additional information (optional)} % optional, remove the line if not wanted
%\hskip 1cm
\photo[78pt]{bigPhoto.jpg}                        
% '64pt' is the height the picture must be resized to and 'picture' is the name of the picture file; 
%optional, remove the line if not wanted
%\quote{"Success is the ability to go from failure to failure without losing your enthusiasm." -- 
%Winston Churchill}                 % optional, remove the line if not wanted

%\nopagenumbers{}                             % uncomment to suppress automatic page numbering for CVs longer than one page


%----------------------------------------------------------------------------------
%            content
%----------------------------------------------------------------------------------
\begin{document}
\maketitle

%Section
\section{{\scshape Personal Information}}
\cvline{\textbf{Birth}}{\small 19 Oct 1992 (Moscow, Russia)\normalsize}
\cvline{\textbf{Citizenship}}{\small Russia \normalsize}
\cvline{\textbf{Status}}{\small Married, we have a child   \normalsize}
\cvline{\textbf{Languages}}{\small Russian (native), English, German (intermediate)
\normalsize}

\section{{\scshape Education}}

\subsection{Postgraduate study}

\cventry{\textbf{Sep 2014 -- present}}{Lomonosov Moscow State University}
{the Chair of Higher Algebra of the 
Department of Mechanics and Mathematics }{Moscow}
{Russia}{Scientific advisor: Prof. E. B. Vinberg.}

\subsection{University}

\cventry{\textbf{Aug 2009 -- Jun 2014}}{Lomonosov Moscow State University}
{the Chair of Higher Algebra of the 
Department of Mechanics and Mathematics }{Moscow}
{Russia}{The gold Medal and Diploma with Honours in Mathematics (M.Sc., cum laude), 
$GPA \sim 4.9$ (5.0 = "excellent'');
Diploma Title: Reflective hyperbolic lattices of rank $4$; 
\\Scientific advisor: Prof. E. B. Vinberg.}% arguments 3 to 6 are optional



\section{{\scshape Research Interests}}
\cvline{}{\small Hyperbolic geometry \normalsize}
\cvline{}{\small Geometry of discrete groups \normalsize}
\cvline{}{\small Hyperbolic reflection groups \normalsize}
\cvline{}{\small Coxeter groups and polyhedra \normalsize}
\cvline{}{\small Determinantal point processes\normalsize}



\section{{\scshape Publications \& Preprints}}
\subsection{Preprints/submitted publications}
\cventry{\textbf{Oct 2016}}{Reflective anisotropic hyperbolic lattices of rank $4$}{}{}{}
{preprint is available on ArXiv: \href{https://arxiv.org/abs/1610.06148}{1610.06148}}
%\url{https://arxiv.org/abs/1610.06148}}
\subsection{Published/accepted articles}
\cventry{\textbf{Feb 2017}}{Reflective anisotropic hyperbolic lattices of rank $4$}
{Russian Mathematical Surveys}{2017}{Vol. 1, p. 193 -- 194 (transl. from Russian), DOI:
\href{http://dx.doi.org/10.1070/RM9756}{10.1070/RM9756}}{}



\section{{\scshape Conference Proceedings}}
\cventry{\textbf{Jan 2017}}{The Sixth School-Conference on Lie Algebras, Algebraic Groups and 
Invariant Theory, Jan 30 -- Feb 04, 2017, Abstracts}{MSU \& IUM}{Moscow, Publ. Dept. Mech. Math. 
MSU, 2017}{p. 18 - 19, ISBN: \href{http://halgebra.math.msu.su/alg_conf/2017/Thesis_full_2017.pdf}{978–5–4439–0988–2}}{Topic: Reflective anisotropic 
hyperbolic lattices of rank $4$}

\section{{\scshape Positions}}
\cventry{\textbf{Feb 2017 --- present}}{Research Scientist}{The Laboratory of Advanced Combinatorics
and Network Applications}{Moscow Institute of Physics and Technology}{Moscow, Russia}{}{}
\cventry{\textbf{Sep 2016 --- present}}{Lecturer}
{Moscow Institute of Physics and Technology}{Moscow}{Russia}
{Lecturer on Differential Geometry and Linear Algebra} % arguments 3 to 6 are optional
\cventry{\textbf{Dec 2015 --- Feb 2017}}{Researcher}{JSC <<Infotecs>>}
{Moscow}{Russia}{Geometric and algebraic 
applications to Cryptography} % arguments 3 to 6 are optional

\cventry{\textbf{Sep 2014 --- Jun 2015}}{Methodist and Teaching 
Assistant}{the Center of online education <<Foxford>>}
{Moscow}{Russia}{Methodist and teaching 
assistant on geometric and olympiad's courses}

\cventry{\textbf{Feb 2010 --- Apr 2016}}{ Teacher on Mathematics}{School 54}
{Moscow}{Russia}{Geometry, Algebra, Olympiad Mathematics}


\section{{\scshape Short Term Visiting Research Positions}}
\cventry{\textbf{Jun 2015}}{Visiting scholar}
{University of Bielefeld}{Bielefeld}{Germany}
{Research on convergence of determinantal point processes} 

\section{{\scshape Talks at Seminars and Conferences}}
\cventry{\textbf{May 2016}}{Seminar <<Lie groups and invariant theory>>}
{MSU}{Moscow}{Russia}{Topic: $1.2$-reflective anisotropic lattices of rank $4$}


\cventry{\textbf{Nov 2016}}{Conference <<MIPT-59>>}
{MIPT}{Moscow}{Russia}{Topic: Reflective hyperbolic lattices}

\cventry{\textbf{Jan 2017}}{The Sixth School-Conference on Lie Algebras,
Algebraic Groups and Invariant Theory}{MSU \& IUM}{Moscow}{Russia}
{Topic: Reflective anisotropic hyperbolic lattices of rank $4$}

\cventry{\textbf{Feb 2017}}{Seminar <<MIPT \& Yandex>>}
{Yandex}{Moscow}{Russia}{Topic: Hyperbolic reflection groups and reflective hyperbolic lattices}

\cventry{\textbf{Mar 2017}}
{S.\,P. Novikov's Seminar <<Geometry, Topology and Mathematical Physics>>}
{MSU}{Moscow}{Russia}{Topic: Arithmetic reflection groups in Lobachevsky spaces}

% arguments 3 to 6 are optional


\section{{\scshape Grants and Awards}}


\subsection{Grants and scholarships}
\cventry{2017}
{Simons Foundation Prize}{The competition of grants of PhD-students 
in mathematics}{}{}{}
\cventry{2012 --- 2014}
{Increased scholarships}{The financial support
for university students-honors for their scientific achievements and 
social activities (in my case for annual participation in the work of methodical commissions of 
All-Russian Mathematical Olympiads 2011---2014 and participation in organizing of 
Moscow Mathematical Olympiads)}{}{}{}

\subsection{Competitions of teachers of mathematics}
\cventry{2012, 2014}
{$2^{nd}$ Prizes}{All-Russian competitions of teachers of mathematics}
{}{}{}



% arguments 3 to 6 are optional
\subsection{University Olympiads}
\cventry{2011}{$3^{rd}$  Prize}{Olympiad on Ordinary Differential Equations}{}{}{}
\cventry{2010, 2011}{$3^{rd}$ Prizes}{Olympiads on Calculus}{}{}{}
\cventry{2010, 2011}{<<Honourable mention>>}{Final Mathematical Olympiads of MSU}
{}{}{}
\cventry{2010}{<<Honourable mention>>}{Kolmogorov Probability Olympiad}
{}{}{}
\cventry{2009}{$3^{rd}$ Prize}{Olympiad on Algebra}{}{}{}

\subsection{School Olympiads}
\cventry{2009}{$1^{st}$  Prize}{Mathematical Olympiad <<Lomonosov>>}{}{}{}
% arguments 3 to 6 are optional
\cventry{2009}{$3^{rd}$ Prize}{Moscow Mathematical Olympiad}{}{}{}
\cventry{2009}{$3^{rd}$ Prize}{Oral Sharygin Moscow Olympiad on Geometry}{}{}{}
\cventry{2007}{$3^{rd}$ Prize}{Olympiad of Department of Mechanics and Mathematics}
{}{}{}


\section{{\scshape References}}
\cventry{}{Professor E.B. Vinberg}{Lomonosov Moscow State Univesity}{Department of
Mechanics and Mathematics}{Moscow, Russia}{Email: evinberg@gmail.com}
\cventry{}{Professor O.V. Schwarzman}{National Research University Higher School of 
Economics}{Department of Mathematics}{Moscow, Russia}{Email: ossipsh@gmail.com}
\cvline{}{\small }


\end{document}


Let us considet $f(x) = \frac{x+1}{x-1}$
