Name:		update-alternatives
Version:	1.8.5
Release:	%mkrel 1
Summary:	Alternative management system
License:	GPL
Group:		System/Configuration/Packaging
Source0:	%{name}-%{version}.tar.bz2
Buildarch:	noarch
Url:        http://cvs.mandriva.com/cgi-bin/cvsweb.cgi/soft/update-alternatives/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
Conflicts:  rpm < 4.4.1

%description
Utility for managing concurent software. Original version comes from
Debian but has been patched by Mandriva for use with rpm systems.

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%install
%make install DESTDIR=%buildroot prefix=%_prefix

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/alternatives
install -d -m 755 $RPM_BUILD_ROOT%{_localstatedir}/rpm/alternatives

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/alternatives
%{_sbindir}/update-alternatives
%{_mandir}/man8/update-alternatives.8*
%dir %{_localstatedir}/rpm/alternatives


