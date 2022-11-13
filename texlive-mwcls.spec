Name:		texlive-mwcls
Version:	44352
Release:	1
Summary:	Polish-oriented document classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mwcls
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
mwcls is a set of document classes for LaTeX 2e designed with
Polish typographical tradition in mind. Classes include:
'mwart' (which is a replacement for 'article'), 'mwrep'
('report'), and 'mwbk' ('book'). Most features present in
standard classes work with mwcls. Some extensions/exceptions
include: sectioning commands allow for second optional argument
(it's possible to state different texts for running head and
for TOC), new environments 'itemize*' and 'enumerate*' for
lists with long items, page styles have variants for normal,
opening, closing, and blank pages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mwcls/mw10.clo
%{_texmfdistdir}/tex/latex/mwcls/mw11.clo
%{_texmfdistdir}/tex/latex/mwcls/mw12.clo
%{_texmfdistdir}/tex/latex/mwcls/mwart.cls
%{_texmfdistdir}/tex/latex/mwcls/mwbk.cls
%{_texmfdistdir}/tex/latex/mwcls/mwbk10.clo
%{_texmfdistdir}/tex/latex/mwcls/mwbk11.clo
%{_texmfdistdir}/tex/latex/mwcls/mwbk12.clo
%{_texmfdistdir}/tex/latex/mwcls/mwrep.cls
%doc %{_texmfdistdir}/doc/latex/mwcls/CZYTAJ
%doc %{_texmfdistdir}/doc/latex/mwcls/ChangeLog
%doc %{_texmfdistdir}/doc/latex/mwcls/README
%doc %{_texmfdistdir}/doc/latex/mwcls/mwclsdoc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mwcls/mwcls.dtx
%doc %{_texmfdistdir}/source/latex/mwcls/mwcls.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
