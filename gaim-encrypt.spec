%define encrypt_version	3.0beta8
%define	rel	0.beta8.1
%define release %mkrel %{rel}

# (Abel) Now that gaim has stabilized API, we can relax the requirement
# a little bit; though it's still desirable to build the plugin with
# latest version of gaim
%define gaim_epoch		1
%define gaim_version		2.0.0
%define min_gaim_version	1:2.0.0

%if %{mdkversion} < 1010
        %define __libtoolize /bin/true
%endif

Summary:	Gaim extension, to use end to end encryption
Name:		gaim-encrypt
#Version:	%{gaim_version}_%{encrypt_version}
Version:	%{gaim_version}_3.0
Release:	%release
Group: 		Networking/Instant messaging
License:	GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://gaim-encryption.sourceforge.net/
Source0:	http://prdownload.sourceforge.net/gaim-encryption/gaim-encryption-%{encrypt_version}.tar.bz2
BuildRequires:  libnss-devel
BuildRequires:  nspr-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gaim-devel = %{gaim_epoch}:%{gaim_version}
Requires:	gaim >= %{min_gaim_version}
Obsoletes:	gaim-encryption
Provides:	gaim-encryption = %{gaim_version}-%{release}

%description
This gaim plugin allows you to encrypt the message, 
only if the person on the other end use the same plugin.

%prep
%setup -q -n gaim-encryption-%encrypt_version
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
rm -rf %{buildroot}%{_libdir}/gaim/encrypt.{l,}a

%find_lang gaim-encryption

%files -f gaim-encryption.lang
%defattr(-,root,root)
%doc NOTES CHANGELOG TODO README WISHLIST
%{_libdir}/gaim/encrypt.so
%{_datadir}/pixmaps/gaim/gaim-encryption/crypto.png

%clean
rm -rf %{buildroot}


