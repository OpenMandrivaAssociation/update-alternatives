Name:		update-alternatives
Version:	1.9.0
Release:	10
Summary:	Alternative management system
License:	GPL
Group:		System/Configuration/Packaging
URL:		https://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/update-alternatives/
Source0:	%{name}-%{version}.tar.bz2
Buildarch:	noarch
Conflicts:	rpm < 4.4.1
# explicit file provides
Provides:	%{_sbindir}/alternatives
Provides:	%{_sbindir}/update-alternatives

%description
Utility for managing concurent software. Original version comes from
Debian but has been patched by Mandriva for use with rpm systems.

%prep
%setup -q

%build
echo "Nothing to build"

%install
%makeinstall_std

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mkdir -p %{buildroot}%{_localstatedir}/lib/rpm/alternatives

(cd %{buildroot}%{_localstatedir}/lib && %{__ln_s} rpm/alternatives alternatives)
(cd %{buildroot}%{_sbindir} && %{__ln_s} update-alternatives alternatives)

%files
%attr(0755,root,root) %{_sbindir}/alternatives
%attr(0755,root,root) %{_sbindir}/update-alternatives
%{_mandir}/man8/update-alternatives.8*
%dir %{_localstatedir}/lib/alternatives
%dir %{_localstatedir}/lib/rpm/alternatives
%dir %{_sysconfdir}/alternatives
