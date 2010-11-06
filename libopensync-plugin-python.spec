Name: 	 	libopensync-plugin-python
Version: 	0.22
Epoch:		1
Release: 	%{mkrel 6}
Summary: 	Python plugin for OpenSync synchronization framework
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	libopensync-devel < 0.30
BuildRequires:	fam-devel
%py_requires -d
Requires:	libopensync-python = %{epoch}:%{version}
Obsoletes:	multisync-backup
Provides:	multisync-backup
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
files stored on disk.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

# Remove the sample plugin, it just messes up GUIs like multisync
# - AdamW 2008/03
rm -f %{buildroot}%{_libdir}/opensync/python-plugins/*

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
%{_libdir}/opensync/python-plugins

