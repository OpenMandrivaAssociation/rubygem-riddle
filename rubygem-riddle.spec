# Generated from riddle-1.2.2.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	riddle

Summary:	An API for Sphinx, written in and for Ruby
Name:		rubygem-%{rbname}

Version:	1.2.2
Release:	1
Group:		Development/Ruby
License:	MIT
URL:		http://riddle.freelancing-gods.com
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
A Ruby API and configuration helper for the Sphinx search service.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f spec

%install
rm -rf %{buildroot}
%gem_install

%clean
rm -rf %{buildroot}

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/riddle
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/riddle/*
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/spec
%{ruby_gemdir}/gems/%{rbname}-%{version}/spec/*
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.textile
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}


%changelog
* Thu Mar 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.2-1
+ Revision: 643539
- generate spec with gem2rpm5
- new release: 1.2.2

* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 623545
- import rubygem-riddle

