Name:           update-alternatives
Version:        1.9.0
Release:        %mkrel 9
Summary:        Alternative management system
License:        GPL
Group:          System/Configuration/Packaging
URL:            http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/update-alternatives/  
Source0:        %{name}-%{version}.tar.bz2
Buildarch:      noarch
Conflicts:  rpm < 4.4.1
# explicit file provides
Provides:       %{_sbindir}/alternatives
Provides:       %{_sbindir}/update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Utility for managing concurent software. Original version comes from
Debian but has been patched by Mandriva for use with rpm systems.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}

%{makeinstall}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/alternatives
%{__mkdir_p} %{buildroot}%{_localstatedir}/lib/rpm/alternatives

(cd %{buildroot}%{_localstatedir}/lib && %{__ln_s} rpm/alternatives alternatives)
(cd %{buildroot}%{_sbindir} && %{__ln_s} update-alternatives alternatives)

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_sbindir}/alternatives
%attr(0755,root,root) %{_sbindir}/update-alternatives
%{_mandir}/man8/update-alternatives.8*
%dir %{_localstatedir}/lib/alternatives
%dir %{_localstatedir}/lib/rpm/alternatives
%dir %{_sysconfdir}/alternatives


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-8mdv2011.0
+ Revision: 670748
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-7mdv2011.0
+ Revision: 608115
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-6mdv2010.1
+ Revision: 524304
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.9.0-5mdv2010.0
+ Revision: 427482
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.9.0-4mdv2009.1
+ Revision: 351454
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.9.0-3mdv2009.0
+ Revision: 225904
- rebuild

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-2mdv2008.1
+ Revision: 179671
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jul 22 2007 Anssi Hannula <anssi@mandriva.org> 1.9.0-1mdv2008.0
+ Revision: 54387
- 1.9.0
  o fix bug causing update-alternatives to not update the slaves of a
    manually selected alternative during --install
  o fix bug causing update-alternatives to switch a link into automatic mode
    when any alternative associated with the link is removed and the link
    points to the alternative with the highest priority at the time
  o remove --test option, it was never implemented
  o add support for --remove-all, --list and --set from Debian
  o allow overwriting of unknown files/symlinks when --set or --config is used
  o better --help output from Debian
  o update man page
  o clean duplicated code
- drop no longer needed patch0

* Sat Jul 21 2007 David Walluck <walluck@mandriva.org> 1.8.9-4mdv2008.0
+ Revision: 54244
- add full patch for missing options

* Sat Jul 21 2007 David Walluck <walluck@mandriva.org> 1.8.9-3mdv2008.0
+ Revision: 54239
- add patch for --set support

* Sat Jul 21 2007 David Walluck <walluck@mandriva.org> 1.8.9-2mdv2008.0
+ Revision: 54144
- use %%{_sbindir} not /usr/sbin for provides
- remove %%{buildroot} in %%install, not %%prep
- use %%{makeinstall} macro
- add %%{_sbindir}/alternatives and %%dir %%{_localstatedir}/alternatives for (FC) compatibility
- add (empty) %%build section to silence rpmlint

  + Anssi Hannula <anssi@mandriva.org>
    - fix URL

* Sun Jul 01 2007 Anssi Hannula <anssi@mandriva.org> 1.8.9-1mdv2008.0
+ Revision: 46212
- 1.8.9
  o fix a bug introduced in 1.8.8 causing a fatal failure when trying to
    remove a nonexistent alternative (bug #31688)

* Fri Jun 29 2007 Anssi Hannula <anssi@mandriva.org> 1.8.8-1mdv2008.0
+ Revision: 45883
- 1.8.8
  o fix bug causing a switch to automatic mode when a symlink in
    /etc/alternatives had been replaced with a relative symlink by the user
  o do not remove or modify symlinks that had been originally created by
    update-alternatives but since retargeted by something else

* Thu Jun 28 2007 Anssi Hannula <anssi@mandriva.org> 1.8.7-1mdv2008.0
+ Revision: 45475
- 1.8.7
  o fix bug causing the removal of legitimate files if a symlink had been
    replaced with a regular file (#19851)

* Wed Jun 27 2007 Anssi Hannula <anssi@mandriva.org> 1.8.6-1mdv2008.0
+ Revision: 44847
- 1.8.6
  o fix bug causing manual alternative to not enter automatic mode when
    /etc/alternatives/foo symlink is noticed missing
  o fix bug causing automatic alternative to enter manual mode when the
    symlink target is noticed missing
  o enter automatic mode when the symlink target is noticed missing
  o fix bug causing symlinks pointing into /etc/alternatives/foo not being
    created when --config is used to select a symlink target which includes
    slave links not already present

* Mon Apr 30 2007 Pixel <pixel@mandriva.com> 1.8.5-2mdv2008.0
+ Revision: 19545
- explicit file provide /usr/sbin/update-alternatives


* Mon Mar 19 2007 Olivier Thauvin <nanardon@mandriva.org> 1.8.5-1mdv2007.1
+ Revision: 146477
- 1.8.5: fix not removed symlink (Anssi Hannula)

* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org> 1.8.4-2mdv2007.0
+ Revision: 54774
- rebuild
- Import update-alternatives

* Thu Jan 12 2006 Warly <warly@mandriva.com> 1.8.4-1mdk
- fix some remaining mandrake references

* Thu Apr 28 2005 Olivier Thauvin <nanardon@mandriva.org> 1.8.3-2mdk
- reintroduce in mandriva as rpm 4.4 will no longer provide it

