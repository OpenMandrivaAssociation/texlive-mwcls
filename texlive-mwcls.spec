# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mwcls
# catalog-date 2009-09-28 14:47:14 +0200
# catalog-license lppl
# catalog-version 0.74
Name:		texlive-mwcls
Version:	0.74
Release:	1
Summary:	Polish-oriented document classes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mwcls
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwcls.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

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

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
