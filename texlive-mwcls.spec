%global tl_name mwcls
%global tl_revision 77050

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.77
Release:	%{tl_revision}.1
Summary:	Polish-oriented document classes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mwcls
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
mwcls is a set of document classes for LaTeX2e designed with Polish
typographical tradition in mind. Classes include: 'mwart' (which is a
replacement for 'article'), 'mwrep' (replacing 'report'), and 'mwbk'
(replacing 'book'). Most features present in standard classes work with
mwcls classes. Some extensions/exceptions include: sectioning commands
allow for second optional argument (it is possible to state different
texts for running head and for TOC), new environments 'itemize*' and
'enumerate*' for lists with long items, page styles have variants for
normal, opening, closing, and blank pages.

