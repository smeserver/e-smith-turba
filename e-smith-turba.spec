# $Id: e-smith-turba.spec,v 1.5 2008/07/12 03:52:19 mrjhb3 Exp $

Summary: e-smith module to configure Turba 1.0
%define name e-smith-turba
Name: %{name}
%define version 2.2
%define release 3
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-turba-2.2.1-header.patch
Patch2: e-smith-turba-2.2-migrate_turba_contacts.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-base, e-smith-lib, e-smith >= 4.1
Requires: turba-h3 >= 2.2
AutoReqProv: no
Obsoletes: dcb-e-smith-turba
Obsoletes: smeserver-turba-menuarray

%changelog
* Fri Jul 11 2008 John H. Bennett III <bennettj@johnbennettservices.com> 2.2-3
- Patch to fix 49turba_migrate_contacts to not run on post-install

* Fri Jun 20 2008 John H. Bennett III <bennettj@johnbennettservices.com> 2.2-2
- Upgrade patch for Turba 2.2.1

* Sat Jun 7 2008 John H. Bennett III <bennettj@johnbennettservices.com> 2.2-1    
- Initial production build

* Sat May 24 2008 John H. Bennett III <bennettj@johnbennettservices.com> 2.2-02
- Updated to include changes in Turba 2.2 RC4
- Re-rolled tarball

* Fri Apr 11 2008 John H. Bennett III <bennettj@johnbennettservices.com> 2.2-01
- Initial build
- Jump in package name to reflect new version of turba

%description
This package adds necessary templates and configuration items
so that Turba will work properly on SME Server

%prep
%setup

%patch1 -p1
%patch2 -p1

%build
for i in bootstrap-console-save post-install post-upgrade email-update
do
    mkdir root/etc/e-smith/events/$i
done
mkdir -p root/etc/rc.d/rc7.d 
perl createlinks


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

