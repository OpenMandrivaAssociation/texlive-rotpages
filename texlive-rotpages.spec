# revision 18740
# category Package
# catalog-ctan /macros/latex/contrib/rotpages
# catalog-date 2007-01-14 10:43:12 +0100
# catalog-license lppl
# catalog-version 3.0
Name:		texlive-rotpages
Version:	3.0
Release:	1
Summary:	Typeset sets of pages upside-down and backwards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rotpages
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotpages.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rotpages.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The rotpages package allows you to format documents where small
sets of pages are rotated by 180 degrees and rearranged, so
that they can be read by turning the printed copy upside-down.
It was primarly meant for collecting exercises and solutions:
using the package, you can print the exercise text normally and
the solutions rotated.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
