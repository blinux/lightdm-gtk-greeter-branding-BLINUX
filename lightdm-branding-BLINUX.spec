#-
# Copyright 2014 Emmanuel Vadot <elbarto@bocal.org>
# All rights reserved
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted providing that the following conditions 
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

Name:		lightdm-branding-BLINUX
Version:        1.1
Release:        0
License:        BSD-2-Clause
Summary:        BLINUX LightDM Branding
BuildArch:      noarch
Source0:        %{name}-%{version}.tgz
Vendor:         Bocal
Url:            http://www.bocal.org
Group:          User Interface/X
Packager:       Emmanuel Vadot <elbarto@bocal.org>

%description
LightDM Background and configuration files for BLINUX

%prep
%setup

%build
rm -fr %{buildroot};
mkdir -p %{buildroot}%{_sysconfdir}/lightdm/;
mkdir -p %{buildroot}/usr/share/pixmaps/;

%install
cp lightdm.conf %{buildroot}%{_sysconfdir}/lightdm/;
cp lightdm-gtk-greeter.conf %{buildroot}%{_sysconfdir}/lightdm/;
cp bocal_logo.png %{buildroot}/usr/share/pixmaps/;

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/lightdm/lightdm.conf
%config %{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf
/usr/share/pixmaps/bocal_logo.png

%changelog
* Mon Aug 04 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.1-0
- Update config files

* Sun Aug 03 2014 Emmanuel Vadot <elbarto@bocal.org> - 1.0-0
- Initial package creation
