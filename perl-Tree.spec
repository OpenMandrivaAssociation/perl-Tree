%define upstream_name    Tree
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A tree datastructure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This is meant to be a full-featured N-ary tree representation with
configurable error-handling and a simple events system that allows for
transparent persistence to a variety of datastores. It is derived from the
Tree::Simple manpage, but has a simpler interface and much, much more.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.10.0-2mdv2011.0
+ Revision: 658411
- rebuild for updated rpm-setup

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 444017
- import perl-Tree


* Thu Sep 17 2009 cpan2dist 1.01-1mdv
- initial mdv release, generated with cpan2dist
