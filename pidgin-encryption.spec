%define release %mkrel 6

Summary:	Pidgin extension, to use end to end encryption
Name:		pidgin-encryption
Version:	3.0
Release:	%release
Group: 		Networking/Instant messaging
License:	GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://gaim-encryption.sourceforge.net/
Source0:	http://prdownload.sourceforge.net/gaim-encryption/%name-%version.tar.bz2
BuildRequires:  libnss-devel
BuildRequires:  nspr-devel
BuildRequires:	gtk+2-devel
BuildRequires:	pidgin-devel
Requires:	pidgin
Obsoletes:	gaim-encryption gaim-encrypt
Provides:	gaim-encryption gaim-encrypt

%description
This Pidgin plugin allows you to encrypt the message, 
only if the person on the other end use the same plugin.

%prep
%setup -q 
chmod 0644 README

%build
#(peroyvind) glib/gstdio.h doesn't exist in older releases
%if %mdkversion < 1020
mkdir glib
touch glib/gstdio.h
CPPFLAGS="-I`pwd`" \
%endif
export LD_LIBRARY_PATH=/usr/X11R6/%{_lib}
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/pidgin/encrypt.{l,}a

%find_lang %name

%files -f %name.lang
%defattr(-,root,root)
%doc NOTES CHANGELOG TODO README WISHLIST
%{_libdir}/pidgin/encrypt.so
%{_datadir}/pixmaps/pidgin/pidgin-encryption/crypto.png

%clean
rm -rf %{buildroot}
