# $Id: e-smith-turba.spec,v 1.20 2010/11/13 18:45:03 mrjhb3 Exp $

Summary: e-smith module to configure Turba 1.0
%define name e-smith-turba
Name: %{name}
%define version 3.2.0
%define release 17
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-turba-2.3.patch
Patch2: e-smith-turba-2.3.1.patch
Patch3: e-smith-turba_remove_sql_schema.patch
Patch4: e-smith-turba-2.3.2.patch
Patch5: e-smith-turba-2.3.3.patch
Patch6: e-smith-turba-3.2.0-ldap_scope.patch
Patch7: e-smith-turba-3.2.0-turbatype_search.patch 
Patch8: e-smith-turba-3.2.0-freebusy.patch
Patch9: e-smith-turba-3.2.0-attributes.php.patch
Patch10: e-smith-turba-3.2.0-LDAP_Group.patch
Patch11: e-smith-turba-3.2.0-remove-turbatype.patch 
Patch12: e-smith-turba-3.2.0-basedn.patch
Patch13: e-smith-turba-3.2.0-basedn2.patch 
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-base, e-smith-lib, e-smith >= 4.1
Requires: turba-h3 >= 2.2
AutoReqProv: no
Obsoletes: dcb-e-smith-turba
Obsoletes: smeserver-turba-menuarray

%changelog
* Sat Nov 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-17
- Fix bug in refactored code used to set ldap base dn. [SME: 2939]

* Fri Nov 12 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-16

- Refactored code used to set ldap base dn.  Thanks Shad Lords [SME: 2939]

* Sun Aug 1 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-15
- Update to remove turbaContact info that SME is not using [SME: 5942]

* Mon May 10 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-14
- Patch that adds the ability to have a local LDAP Group Address book.  [SME: 5944]

* Mon May 10 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-13
- Patch to template attributes.php to add ability to have multiple email values
  for a contact.  Separate entries with a comma and a space [SME: 5943]

* Mon May 10 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-12
- Update to freebusy info in sources.php [SME 5942]

* Sat Feb 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-11
- Update to fix turbatype error when using turba LDAP address search [SME: 5772]

* Sat Feb 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-10
- Update LDAP for changed scope [SME: 2939]

* Sat Feb 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-9
- Updated template files to reflect changes in Turba 2.3.3 [SME: 5778]
- Remove previous patch.  Will add new partial patch for bug 2939

* Sat Feb 13 2010 Stephen Noble <support@dungog.net> 3.2.0-8
- Update LDAP for changed schema [SME: 2939]

* Tue Oct 13 2009 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-7   
- Updated template files to reflect changes in Turba 2.3.2 [SME: 5512]

* Wed Apr 8 2009 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-6
- Remove redundant 49turba_migrate_contacts template fragments [SME: 5148]

* Sun Jan 4 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 3.2.0-5
- Fix date in previous changelog entry [SME: 4910]

* Sun Jan 4 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 3.2.0-4
- Fix turba.sql patch to prevent creating a .orig file [SME: 4910]

* Fri Jan 2 2009 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-3       
- Updated template files to reflect changes in Turba 2.3.1

* Sat Dec 06 2008 John H. Bennett III <bennettj@johnbennettservices.com> 3.2.0-2       
- Updated template files to reflect changes in Turba 2.3 [SME: 4833]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 3.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

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
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

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

