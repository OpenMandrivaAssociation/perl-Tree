%define upstream_name    Tree
%define upstream_version 1.16
Name:		perl-%{upstream_name}
Version:	1.16
Release:	1

Summary:	A tree datastructure
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}
Source0:	https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Tree-1.16.tgz

BuildRequires:	make
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
%setup -q -n %{upstream_name}-%{version}

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

