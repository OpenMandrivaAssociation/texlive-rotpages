Name:		texlive-rotpages
Version:	18740
Release:	2
Summary:	Typeset sets of pages upside-down and backwards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rotpages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotpages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotpages.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The rotpages package allows you to format documents where small
sets of pages are rotated by 180 degrees and rearranged, so
that they can be read by turning the printed copy upside-down.
It was primarly meant for collecting exercises and solutions:
using the package, you can print the exercise text normally and
the solutions rotated.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rotpages/rotpages.sty
%doc %{_texmfdistdir}/doc/latex/rotpages/Documentation/rotpages-doc.pdf
%doc %{_texmfdistdir}/doc/latex/rotpages/Documentation/rotpages-doc.tex
%doc %{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-doublecolumn-ex.pdf
%doc %{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-doublecolumn-ex.tex
%doc %{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-fancy-ex.pdf
%doc %{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-fancy-ex.tex
%doc %{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-singlecolumn-ex.pdf
%doc %{_texmfdistdir}/doc/latex/rotpages/Examples/rotpages-singlecolumn-ex.tex
%doc %{_texmfdistdir}/doc/latex/rotpages/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
