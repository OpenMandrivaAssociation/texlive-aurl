%global tl_name aurl
%global tl_revision 75878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Extends the hyperref package with a mechanism for hyperlinked URLs abbreviate...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aurl
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aurl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aurl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Semantic Web resource URLs are often abbreviated with prefixes, like
owl:Class or rdf:type. The abbreviated URL (aurl) package provides the
correct hyperlinks for those URLs. The 1000 most common prefixes are
predefined and more can be added.

