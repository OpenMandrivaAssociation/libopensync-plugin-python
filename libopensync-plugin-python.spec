%define name	libopensync-plugin-python
%define version	0.34
%define release %mkrel 1

Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Python plugin for opensync synchronization tool
License:	LGPLv2+
Group:		Office
URL:		http://www.opensync.org
Source:		 http://www.opensync.org/download/releases/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	opensync-devel >= %{version}
BuildRequires:	fam-devel
BuildRequires:	cmake
%py_requires -d
Obsoletes:	multisync-backup
Provides:	multisync-backup
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This plugin allows applications using OpenSync to synchronise to and from
files stored on disk.

%prep
%setup -q

%build
%cmake
%make
										
%install
rm -rf %{buildroot}
cd build
%makeinstall_std
cd -

%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS
%{_libdir}/opensync/plugins/*
