Name:           update-alternatives
Version:        1.8.9
Release:        %mkrel 4
Summary:        Alternative management system
License:        GPL
Group:          System/Configuration/Packaging
URL:            http://svn.mandriva.com/cgi-bin/viewvc.cgi/soft/update-alternatives/  
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-1.8.9-remove_all-list-set-all.patch
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
%patch0 -p1

%build

%install
%{__rm} -rf %{buildroot}

%{makeinstall}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/alternatives
%{__mkdir_p} %{buildroot}%{_localstatedir}/rpm/alternatives

(cd %{buildroot}%{_localstatedir} && %{__ln_s} rpm/alternatives alternatives)
(cd %{buildroot}%{_sbindir} && %{__ln_s} update-alternatives alternatives)

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_sbindir}/alternatives
%attr(0755,root,root) %{_sbindir}/update-alternatives
%{_mandir}/man8/update-alternatives.8*
%dir %{_localstatedir}/alternatives
%dir %{_localstatedir}/rpm/alternatives
%dir %{_sysconfdir}/alternatives
