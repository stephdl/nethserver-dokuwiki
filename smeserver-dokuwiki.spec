%define name nethserver-dokuwiki
%define version 0.0.1
%define release 1
Summary: Nethserver integration of dokuwiki
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL
URL: http://www.splitbrain.org/projects/dokuwiki
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRequires: nethserver-devtools
BuildRoot: /var/tmp/%{name}-%{version}
Requires: dokuwiki
Requires: nethserver-httpd
Requires: nethserver-directory
AutoReqProv: no

%description
Nethserver integration of dokuwiki
DokuWiki is a simple to use Wiki aimed at the documentation needs of a small company


%prep
%setup

%build
perl ./createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%clean
rm -rf $RPM_BUILD_ROOT


%postun

%changelog
* Sat Jul 5 2014 Daniel B. <daniel@firewall-services.com> 0.1.5-1
- Small fixes in authhttpldap plugin

* Tue May 6 2014 Daniel B. <daniel@firewall-services.com> 0.1.4-1
- Add missing plugin.info.txt file for the authhttpldap plugin

* Thu Dec 5 2013 Daniel B. <daniel@firewall-services.com> 0.1.3-1
- Push php memory limit to 128M

* Fri Nov 22 2013 Daniel B. <daniel@firewall-services.com> 0.1.2-1
- Fix a typo which prevent transparent SSL redirection

* Wed May 15 2013 Daniel B. <daniel@firewall-services.com> 0.1.1-1
- Use the new auth plugins to be compatible with dokuwiki 2013-05-10

* Wed May 15 2013 Daniel B. <daniel@firewall-services.com> 0.1.0-1
- Import in GIT

* Mon Dec 19 2011 Daniel B. <daniel@firewall-services.com> 0.1-2
- Follow symlinks so fck media browser works

* Fri Jul 08 2011 Daniel B. <daniel@firewall-services.com> 0.1-1
- initial release
