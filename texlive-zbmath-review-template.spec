Name:		texlive-zbmath-review-template
Version:	59693
Release:	1
Summary:	Template for a zbMATH Open review
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zbmath-review-template
License:	gpl3 cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zbmath-review-template.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zbmath-review-template.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains a template for zbMATH Open reviews. It
will show what your review will look like on zbMATH Open and
you can test whether your LaTeX-Code will compile on our
system. The template has to be compiled using XeLaTeX and
relies on scrartcl, scrlayer-scrpage, amsfonts, amssymb,
amsmath, babel, enumitem, etoolbox, fontspec, gensymb,
geometry, graphicx, mathrsfs, mathtools, stmaryrd, textcomp,
tikz-cd, xcolor, and xparse.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/zbmath-review-template
%doc %{_texmfdistdir}/doc/xelatex/zbmath-review-template

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
