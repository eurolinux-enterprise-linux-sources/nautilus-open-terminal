# This can be safely commented out at next point release,
# changes should only use %gitver when it's defined. Sorry
# for the mess.
%global gitver 32a1da0160

Name:           nautilus-open-terminal
Version:        0.20
Release:        3%{?dist}
Summary:        Nautilus extension for an open terminal shortcut

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://download.gnome.org/sources/%{name}/
Source0:        http://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	intltool
# need extensions
BuildRequires:	nautilus-devel

# https://bugzilla.redhat.com/show_bug.cgi?id=653289
# Icon missing from Open in Terminal menu entry
Patch0:         nautilus-open-terminal-0.19-restoreicon.patch
BuildRequires:  autoconf automake libtool GConf2-devel

Requires(pre): GConf2
Requires(post): GConf2
Requires(preun): GConf2

%description
The nautilus-open-terminal extension provides a right-click "Open
Terminal" option for nautilus users who prefer that option.

%prep
%setup -q
%patch0 -p1 -b .restoreicon

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/nautilus/extensions-3.0/*.{l,}a

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT

%pre
if [ "$1" -gt 1 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
              %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi

%post
export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
gconftool-2 \
	    --makefile-install-rule \
	    %{_sysconfdir}/gconf/schemas/%{name}.schemas >/dev/null || :

%preun
if [ "$1" -eq 0 ]; then
  export GCONF_CONFIG_SOURCE=`gconftool-2 --get-default-source`
  gconftool-2 --makefile-uninstall-rule \
              %{_sysconfdir}/gconf/schemas/%{name}.schemas > /dev/null || :
fi


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS TODO
%config(noreplace) %{_sysconfdir}/gconf/schemas/*
%{_libdir}/nautilus/extensions-3.0/*.so*

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.20-3
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20-2
- Mass rebuild 2013-12-27

* Wed Feb 27 2013 Kalev Lember <kalevlember@gmail.com> - 0.20-1
- Update to 0.20

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 0.19-7
- Rebuilt for libgnome-desktop-3 3.7.3 soname bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  8 2012 Paul W. Frields <stickster@gmail.com> - 0.19-5
- Rebuild for new libgnome-desktop

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.19-3
- Rebuild for new libpng

* Mon Jun 27 2011 Paul W. Frields <stickster@gmail.com> - 0.19-2
- Rebuild against newer gnome-desktop3

* Tue Feb 22 2011 Cosimo Cecchi <cosimoc@redhat.com> - 0.19-1
- Update to 0.19

* Fri Feb 10 2011 Matthias Clasen <mclasen@redhat.com>
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-0.5.32a1da0160git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 0.19-0.4.32a1da0160git
- Rebuild against newer gtk

* Fri Jan 28 2011 Bastien Nocera <bnocera@redhat.com> 0.19-0.3.32a1da0160git
- Port to GTK+ 3.x

* Wed Dec 22 2010 Paul W. Frields <stickster@gmail.com> - 0.19-0.2.32a1da0160git%{?dist}
- Fix missing icon problem (#653289)

* Fri Mar 12 2010 Paul W. Frields <stickster@gmail.com> - 0.19-0.1.32a1da0160git
- Use upstream master HEAD for added translations (#570464)

* Sun Jan 17 2010 Matthias Clasen <mclasen@redhat.com> - 0.18-2
- Rebuild

* Mon Jan  4 2010 Matthias Clasen <mclasen@redhat.com> - 0.18-1
- Update to 0.18

* Tue Aug 11 2009 Matthias Clasen <mclasen@redhat.com> - 0.17-1
- Update to 0.17

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Paul W. Frields <stickster@gmail.com> - 0.13-1
- Update to upstream 0.13

* Thu May 21 2009 Paul W. Frields <stickster@gmail.com> - 0.12-1
- Update to upstream 0.12

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-11
- Rebuild against new gnome-desktop

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-10
- Rebuild against latest gnome-desktop

* Wed Jun  4 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-4
- Rebuild against latest gnome-desktop
- Remove the support for Fedora < 6, since "10" < "6"

* Fri May  9 2008 Paul W. Frields <stickster@gmail.com> - 0.9-3
- Use latest automake in spec

* Fri Apr  4 2008 Paul W. Frields <stickster@gmail.com> - 0.9-2
- Handle GConf schema installation

* Fri Feb 29 2008 Matthias Clasen <mclasen@redhat.com> - 0.9-1
- Update to 0.9

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8-4
- Autorebuild for GCC 4.3

* Mon Jan 24 2008 Josh Boyer <jwboyer@gmail.com> - 0.8-2
- Grab SVN snapshot to fix extension directory and building against newer
  nautilus

* Sat Sep 22 2007 Paul W. Frields <stickster@gmail.com> - 0.8-2
- Fix download and source URIs

* Fri Aug 17 2007 Paul W. Frields <stickster@gmail.com> - 0.8-1
- Update License tag
- Update to version 0.8
- Include patch to silence truth value warning

* Sat Aug 28 2006 Paul W. Frields <stickster@gmail.com> - 0.7-3
- Include BR: intltool for mass FC6 rebuild

* Wed Aug 16 2006 Paul W. Frields <stickster@gmail.com> - 0.7-2
- Handle splitting of nautilus and nautilus-extensions

* Tue Aug  1 2006 Paul W. Frields <stickster@gmail.com> - 0.7-1
- Update to version 0.7

* Fri Jun 16 2006 Paul W. Frields <stickster@gmail.com> - 0.6-4
- Fix BuildRequires, adding gettext

* Fri Feb 17 2006 Paul W. Frields <stickster@gmail.com> - 0.6-3
- FESCo mandated rebuild

* Thu Feb  2 2006 Paul W. Frields <stickster@gmail.com> - 0.6-2
- Remove superfluous docs (#179289, thanks Brian Pepple)

* Sat Oct  8 2005 Paul W. Frields <stickster@gmail.com> - 0.6-1
- Update to version 0.6

* Sat Aug 20 2005 Paul W. Frields <stickster@gmail.com> - 0.4-7
- Push release for new build

* Wed Aug 17 2005 Paul W. Frields <stickster@gmail.com> - 0.4-6
- Rebuild against new cairo
- Include <gtk/gtk.h> and remove unused variable (#166346)

* Sun Jul 17 2005 Paul W. Frields <stickster@gmail.com> - 0.4-5
- Add libtoolize to fix multilib problem (#163463)

* Fri Jul 15 2005 Paul W. Frields <stickster@gmail.com> - 0.4-4
- Use find_lang and scriptlets per official guidelines

* Thu Jul 14 2005 Paul W. Frields <stickster@gmail.com> - 0.4-3
- Remove .a and .la devel files from build

* Thu Jul 14 2005 Paul W. Frields <stickster@gmail.com> - 0.4-2
- Use dist tag and update BuildRequires

* Wed Jul 13 2005 Paul W. Frields <stickster@gmail.com> - 0.4-1
- Initial version

