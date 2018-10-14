#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-Strip
Version  : 1.02
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOMM/Pod-Strip-1.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOMM/Pod-Strip-1.02.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libp/libpod-strip-perl/libpod-strip-perl_1.02-2.debian.tar.xz
Summary  : Remove POD from Perl code
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
Pod::Strip - Remove POD from Perl code
Pod::Strip is a subclass of Pod::Simple that strips all POD from Perl Code.

%package dev
Summary: dev components for the perl-Pod-Strip package.
Group: Development
Provides: perl-Pod-Strip-devel = %{version}-%{release}

%description dev
dev components for the perl-Pod-Strip package.


%prep
%setup -q -n Pod-Strip-1.02
cd ..
%setup -q -T -D -n Pod-Strip-1.02 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Pod-Strip-1.02/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.26.1/Pod/Strip.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::Strip.3
