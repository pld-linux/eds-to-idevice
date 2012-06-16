Summary:	Tool to copy contacts to iDevices
Name:		eds-to-idevice
Version:	0.5
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://people.freedesktop.org/~teuf/eds-to-idevice/%{name}-%{version}.tar.bz2
# Source0-md5:	66a6810c0a888506b832af6ce63f1db5
URL:		http://cfergeau.blogspot.fr/2011/03/transferring-contacts-to-idevice.html
BuildRequires:	evolution-data-server-devel
BuildRequires:	glib2-devel
BuildRequires:	libimobiledevice-devel >= 1.1
BuildRequires:	libplist-devel >= 1.4
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eds-to-idevice is a commandline tool to transfer contacts stored in
evolution-data-server addressbooks to an iDevice from Apple. It uses
libebook for the communication with evolution-data-server and
libimobiledevice to communicate with iDevices.

This tool isn't a synchronization tool, it makes no attempt at
matching contacts from evolution with contacts from the iDevice. If
you try to copy contacts that are already present on the iDevice, they
will likely be duplicated.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS=$(pkg-config --cflags glib-2.0)
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/eds-to-idevice
