%define name nethserver-dokuwiki
%define version 1.2.5
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
Requires: dokuwiki >= 20180422
Requires: nethserver-httpd
Requires: nethserver-rh-php71-php-fpm
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
%{genfilelist} $RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%clean
rm -rf $RPM_BUILD_ROOT


%postun

%changelog
* Tue Jun 19 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.5-1.ns7
- Probe starttls for remote samba AD authentication

* Mon Jun 04 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.4-1.ns7
- Avoid apache vhost collision
- better definition of ssl certificate

* Sun May 13 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.3-1.ns7
- Typo on the apache URL path

* Tue May 8 2018  stephane de labrusse <stephdl@de-labrusse.fr> 1.2.2-1.ns7
- Subscribe to nethserver-sssd-save event 

* Sat May 5 2018 stephane de labrusse <stephdl@de-labrusse.fr> 1.2.1-1.ns7
- SambaAD uses self bind
- Users cannot change their password with openldap

* Tue May 1 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-1.ns7
- use nethserver-rh-php71-php-fpm for dokuwiki-20180422

* Mon Oct 02 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.5-1.ns7
- corrected typo in local.protected.php
 
* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.4-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.3-1.ns7
- Template expansion on trusted-network

* Thu Mar 16 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.2-2.ns7
- Changed DocumentRoot to DomainName property

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-2.ns7
- GPL license

* Sat Mar 11 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-1.ns7
- Certificates for virtualhost added

* Thu Dec 1 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0-1.ns7
- First release to NS7

* Sat Apr 9 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- set a document root is an option accessible by a property

* Tue Mar 22 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release to Nethserver
