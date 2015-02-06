%define upstream_name    Locale-Msgfmt
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Functions used internally by Locale::Msgfmt
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Locale/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module does the same thing as msgfmt from GNU gettext-tools, except this
is pure Perl.

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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Locale
%{perl_vendorlib}/Module


%changelog
* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.150.0-1mdv2011.0
+ Revision: 602031
- new version

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.140.0-1mdv2011.0
+ Revision: 393849
- import perl-Locale-Msgfmt


* Thu Jul 09 2009 cpan2dist 0.12-1mdv
- initial mdv release, generated with cpan2dist
