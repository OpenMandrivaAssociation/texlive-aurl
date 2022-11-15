Name:		texlive-aurl
Version:	41853
Release:	1
Summary:	Extends the hyperref package with a mechanism for hyperlinked URLs abbreviated with prefixes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aurl
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aurl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aurl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Semantic Web resource URLs are often abbreviated with prefixes,
like "owl:Class" or "rdf:type". The abbreviated URL (aurl)
package provides the correct hyperlinks for those URLs. The
1000 most common prefixes are predefined and more can be added.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/aurl
%doc %{_texmfdistdir}/doc/latex/aurl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
