Summary: e-smith module to configure Turba 1.0
%define name e-smith-turba
Name: %{name}
%define version 1.5.1
%define release 12
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-turba-1.5.1-02.mitel_patch
Patch1: e-smith-turba-1.5.1-03.mitel_patch
Patch2: e-smith-turba-1.5.1-04.mitel_patch
Patch3: e-smith-turba-1.5.1-05.mitel_patch
Patch4: e-smith-turba-1.5.1-06.mitel_patch
Patch5: e-smith-turba-1.5.1-07.mitel_patch
Patch6: e-smith-turba-1.5.1-11.menusettings.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-base, e-smith-lib, e-smith >= 4.1
Requires: turba-h3 >= 2.0
AutoReqProv: no
Obsoletes: dcb-e-smith-turba

%changelog
* Tue Feb 28 2006 Charlie Brady <charlie_brady@mitel.com> 1.5.1-12
- Back out menusettings changes for now. We'll do them later. [SME: 883]

* Sat Feb 25 2006 John H. Bennett III <bennettj@johnbennettservices.com> 1.5.1-11
- Removed menu-apps line from 100Conf and added 120MenuSettings.
- added %post and %postun lines to spec file that add/remove db settings
  that 120MenuSettings will reference. [SME: 883]

* Wed Feb  8 2006 1.5.1-10
- Change default group of included files from www to root. [SME: 700]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.5.1-09
- Bump release number only

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [1.5.1-08]
- Update requires (turba-h3 replaces turba).

* Tue Aug  2 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-07]
- Purge deprecated esmith::config and esmith::db APIs
  from template fragments.

* Wed Jul  6 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-06]
- Mark ldap address book as readonly. [SF: 1189640]

* Sun May  1 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-05]
- Switch from localldap to localsql addressbook

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-04]
- Fix a few small probs in combined upgrade script and template which
  calls it.

* Tue Apr 19 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-03]
- Combine 1.1->1.2 and 1.2->2.0 upgrade scripts. Fix path in turba db
  create script. Don't bother running migrate-imp-to-turba unless there
  is an imp address book table (very old hat now).

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-02]
- Horde 3 config updates, courtesy of Greg Swallow.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.1-01]
- Roll to new development stream for horde 3 update - 1.5.1

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-05]
- Fix mysql.init shell script name and paths to template expand.

* Mon Apr 18 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-04]
- Add templates.metadata files so that ownership and perms of conf.php
  and sources.php is correct.
- Replace conf-turba-startup with templated shell scripts.

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-03]
- Add migrate fragment missing from last change. [MN00064391]

* Mon Jan 17 2005 Charlie Brady <charlieb@e-smith.com>
- [1.5.0-02]
- Obsolete conf-turba action by using generic_template_expand action and
  default db fragments. Update e-smith-lib dependency. [MN00064130]
- Delete redundent db key deletion code in conf-turba-startup. [MN00064391]

* Wed Feb  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.5.0-01]
- rolling to dev - 1.5.0

* Wed Feb  4 2004 Michael Soulier <msoulier@e-smith.com>
- [1.4.0-01]
- rolling to stable - 1.4.0

* Wed Nov 26 2003 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-06]
- Fixed typo. s/Config/ConfigDB. [msoulier 4796]

* Wed Nov 26 2003 Michael Soulier <msoulier@e-smith.com>
- [1.3.0-05]
- Updated two actions to fetch the horde db password from configuration.
  [msoulier 4796]

* Fri Nov 21 2003 Mark Knox <markk@e-smith.com>
- [1.3.0-04]
- Fetch the horde db password from configuration [markk 4796]

* Fri Sep 12 2003 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-03]
- Explicitly check for existence of turba_objects columns before attempting
  to add them. Don't try to create an owner_id index if one already
  exists. [charlieb 9971]

* Wed Sep 10 2003 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-02]
- Do not skip turba table update if imp address book table does
  not exist (it usually won't exist). [charlieb 9971]

* Fri Aug 22 2003 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-01]
- Changing version to development stream number - 1.3.0

* Thu Jul 17 2003 Mark Knox <markk@e-smith.com>
- [1.2.2-01]
- Rolling as source to pick up missing files - again [markk 9279]

* Wed Jul 16 2003 Charlie Brady <charlieb@e-smith.com>
- [1.2.1-02]
- Unlink sql/init symlinks before creating new ones, in case
  symlink exists and points to the wrong place. [charlieb 9476]
- Replace Copyright header with License header.

* Fri Jul  4 2003 Mark Knox <markk@e-smith.com>
- [1.2.1-01]
- Bug 9279: Repackage to include missing files from 1.1.1-05 - 1.2.1

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-01]
- Changing version to stable stream number - 1.2.0

* Thu Jun  5 2003 Mark Knox <markk@e-smith.com>
- [1.1.1-05]
- Fixed up indenting slightly and added two missing fields to turba_objects
  insert statement [markk 8834]

* Thu Jun  5 2003 Lijie Deng <lijied@e-smith.com>
- [1.1.1-04]
- Added drop imp_addr table statement [lijied 8834]

* Fri May 30 2003 Mark Knox <markk@e-smith.com>
- [1.1.1-03]
- Added further wraps around turba db creation [markk 8581]

* Wed May 21 2003 Mark Knox <markk@e-smith.com>
- [1.1.1-02]
- Converted mysql_upgrade_1.1_to_1.2 to perl and linked as 
  50turba_upgrade_1.1_to_1.2 [markk 8581]
- Added wrapper around turba db creation [markk 8581]

* Wed Apr 23 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.1.1-01]
- Include changes from Dan Brown's e-smith-turba-1.1.0-05db [gordonr 7794]
  * Sun Apr  6 2003 Dan Brown <dan@familybrown.org>
  - [1.1.0-05db]
  - changed menu settings to dynamically include all installed
    horde modules
  - created horde-update event
  * Wed Mar 26 2003 Dan Brown <dan@familybrown.org>
  - [1.1.0-04db]
  - uncommented objectclass and version lines in sources.php
  - added comma to 'root' line in sources.php
  * Sun Mar 23 2003 Dan Brown <dan@familybrown.org>
  - [1.1.0-03db]
  - commented out objectclass and version lines in sources.php
    for local LDAP.  Don't know why, but they break all sources.
  * Sun Mar 23 2003 Dan Brown <dan@familybrown.org>
  - [1.1.0-02db]
  - added objectclass definition to sources.php
  * Wed Mar 12 2003 Dan Brown <dan@familybrown.org>
  - [1.1.0-01db]
  - Update sources.php for compatibility with Turba 1.2
  - Add link to mysql_upgrade_1.1_to_1.2.sql
- Updated Requires: line for turba to >= 1.2 [gordonr 7794]
- Moved symlink noted in 1.1.0-01db0 into the %build section (from %post)

* Sat Apr 19 2003 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-01]
- Roll development stream to 1.1.0

* Tue Mar 18 2003 Lijie Deng <lijied@e-smith.com>
- [1.0.0-02]
- Deleted ./httpd/html/horde/turba/config/{conf.php, sources.php}
  /template-{begin,end}, modified %build code [lijied 3295]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.0.0-01]
- Roll to maintained version number to 1.0.0

* Wed Sep 25 2002 Charlie Brady <charlieb@e-smith.com>
- [0.21.3-05]
- Rename migrate-imap-to-turba to migrate-imp-to-turba. We had the
  correct symlink name, but wrong filename [charlieb 4782]

* Wed Sep 25 2002 Charlie Brady <charlieb@e-smith.com>
- [0.21.3-04]
- Always run migrate-imp-to-turba script in mysql.init after
  install/upgrade/restore. [charlieb 4782]

* Thu Sep 19 2002 Charlie Brady <charlieb@e-smith.com>
- [0.21.3-03]
- Add conf-turba action to bootstrap-console-save event. [charlieb 4782]

* Fri Sep  6 2002 Charlie Brady <charlieb@e-smith.com>
- [0.21.3-02]
- Move migrate-imp-to-turba into events/actions, and set up symlink into
  /etc/e-smith/init/sql so that mysql.init can run the script [charlieb 4782]
- Greatly simplify conf-turba and conf-turba-startup scripts, and
  remove duplication between them. Leave it to mysql.init to do the
  grunt work [charlieb 4782]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [0.21.3-01]
- Don't set deprecated InitscriptsOrder property, it's already implicit in
  the rc7.d symlink [charlieb 4458]

* Mon Jul  8 2002 Mark Knox <markk@e-smith.com>
- [0.21.2-01]
- Small fix to prevent migration failure when imp_addr is empty [markk 4228]

* Wed Jun 19 2002 Mark Knox <markk@e-smith.com>
- [0.21.1-01]
- Expand turba templates even if we create a new address book [markk 3920]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [0.21.0-01]
- Changing version to development stream number to 0.21.0

* Fri May 31 2002 Charlie Brady <charlieb@e-smith.com>
- [0.20.0-01]
- Changing version to maintained stream number to 0.20.0

* Thu May 30 2002 Tony Clayton <apc@e-smith.com>
- [0.19.4-01]
- rework the conf-turba-startup script, and add a conf-turba script in the
  email-update event in order to handle every upgrade scenario.  lots of inline
  comments. [tonyc 3751]

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.19.3-01]
- RPM rebuild forced by cvsroot2rpm

* Sat May 18 2002 Mark Knox <markk@e-smith.com>
- [0.19.2-01]
- Don't run the migration script (and disable it) if there's no imp_addr
  table, or if webmail is disabled. [markk 3197]

* Sat May 18 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.19.1-01]
- Change version to match our numbering standards [gordonr 3528]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [0.18-01]
- Move action to post-{install,upgrade} and detect proper db migration based
  on event [markk 3197]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [0.17-01]
- Make sure we have a link to the migration script in the rpm [markk 3197]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [0.16-01]
- Be more verbose during conversion [markk 3197]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [0.15-01]
- Logic error in system() fixed. Delete BASH_ENV too. [markk 3197]

* Fri May 17 2002 Mark Knox <markk@e-smith.com>
- [0.14-01]
- Need to ensure that horde db is created (by running mysql.init) before we
  try to add tables. [markk 3197]

* Thu May 16 2002 Mark Knox <markk@e-smith.com>
- [0.13-01]
- Create turba tables in migrate script instead of conf action. We can't use
  mysql.init to create them because it runs after the migrate script.
  [markk 3197]

* Thu May 16 2002 Mark Knox <markk@e-smith.com>
- [0.12-01]
- Change service name in migrate-imp-to-turba script as well, and don't run
  unless the service is enabled [markk 3197]

* Thu May 16 2002 Mark Knox <markk@e-smith.com>
- [0.11-01]
- Rename "turba" service to more accurate "migrate-imp-to-turba" [markk 3197]

* Thu May 16 2002 Mark Knox <markk@e-smith.com>
- [0.10-01]
- Changes to support running addressbook migration as an initscript 
  [markk 3197]
- Removed migrate-imp-to-turba from events and moved into init.d [markk 3197]

* Wed May 15 2002 Mark Knox <markk@e-smith.com>
- [0.9-01]
- Another try at fixing addressbook migration on upgrades: create sql fragment
  and let mysql.init import it [markk 3197]

* Tue May  7 2002 Mark Knox <markk@e-smith.com>
- [0.8-01]
- Fixed address book migration problem [markk 2825]

* Tue Apr 23 2002 Mark Knox <markk@e-smith.com>
- [0.7-01]
- Removed links to 'foreign' address books (Netscape, Bigfoot, Verisign)
  [markk 3229]

* Fri Apr 19 2002 Mark Knox <markk@e-smith.com>
- [0.6-01]
- Added 'equals 0' test to system call in conf-turba-startup. Action was
  failing before expading templates due to bad test logic. [markk 3197]

* Wed Apr 10 2002 Mark Knox <markk@e-smith.com>
- [0.5-01]
- Added action to migrate address book [markk 2825]

* Tue Apr  9 2002 Mark Knox <markk@e-smith.com>
- [0.4-01]
- Removed %preun and %post scripts [markk]
- Added new action conf-turba-startup to configure mysql and expand config 
  files. This is called via bootstrap-console-save. [markk]

* Mon Apr 8 2002 Mark Knox <markk@e-smith.com>
- [0.3-01]
- rollRPM: Rolled version number to 0.3-01. Includes patches up to 0.2-03.
- Prepared for CVS import.

* Mon Apr 08 2002 Mark Knox <markk@e-smith.com>
- [0.2-03]
- Renamed to e-smith-turba for import into 5.5 distribution. Obsoletes
  equivalent dcb package. Renamed tarball and BUILD directory.
- Removed events directory and example action.

* Mon Feb 11 2002 Dan Brown <dan@familybrown.org>
- 0.2 release 3
- run turba.sql script at installation using mysql.init service

* Sun Feb 10 2002 Dan Brown <dan@familybrown.org>
- Release 0.2-2
- Broke apart template fragments for sources.php
- Added support for local LDAP server in sources.php
- Added template for conf.php
- Added link to IMP in top menu

* Sun Feb 10 2002 Dan Brown <dan@familybrown.org>
- Initial release for Turba 1.0

* Sat Jan  6 2001 Charlie Brady <charlieb@e-smith.com>
- Make dependent on e-smith-devtools

* Sat Jun 17 2000 Charlie Brady <charlieb@e-smith.com>
- initial release

%description
e-smith server enhancement to configure Turba 1.2 (address book 
application for horde/IMP)

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
#%patch6 -p1

%build
for i in bootstrap-console-save post-install post-upgrade email-update
do
    mkdir root/etc/e-smith/events/$i
done
mkdir -p root/etc/rc.d/rc7.d 
perl createlinks

for file in conf.php sources.php
do
    mkdir -p root/etc/e-smith/templates/home/httpd/html/horde/turba/config/$file
    ln -s /etc/e-smith/templates-default/template-begin-php \
      root/etc/e-smith/templates/home/httpd/html/horde/turba/config/$file/template-begin
    ln -s /etc/e-smith/templates-default/template-end-php \
      root/etc/e-smith/templates/home/httpd/html/horde/turba/config/$file/template-end
done


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

