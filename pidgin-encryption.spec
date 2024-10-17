Name:       pidgin-encryption
Version:    3.1
Release:    3
Summary:    Pidgin extension, to use end to end encryption
Group:      Networking/Instant messaging
License:    GPLv2
Url:        https://pidgin-encrypt.sourceforge.net/

Source0:    http://sourceforge.net/projects/pidgin-encrypt/files/Releases/%version/pidgin-encryption-%version.tar.gz
Patch1:     pidgin-encryption-new_glib-fix.patch

BuildRequires:  nss-devel
BuildRequires:  nspr-devel
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pidgin-devel

Requires:   pidgin

# Not sure what to do with these ?
#Obsoletes: gaim-encryption gaim-encrypt
#Provides:  gaim-encryption gaim-encrypt

%description
This Pidgin plug-in allows you to encrypt the message,
only if the person on the other end use the same plug-in.

%prep
%setup -q
%patch1 -p1
chmod 0644 README

%build
#(peroyvind) glib/gstdio.h doesn't exist in older releases
export LD_LIBRARY_PATH=/usr/X11R6/%{_lib}
%configure2_5x
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/pidgin/encrypt.{l,}a

%find_lang %name

%files -f %name.lang
%doc NOTES CHANGELOG TODO README WISHLIST
%{_libdir}/pidgin/encrypt.so
%{_datadir}/pixmaps/pidgin-encryption/*
