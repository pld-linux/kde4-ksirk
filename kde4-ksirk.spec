%define		_state		stable
%define		orgname		ksirk
%define		qtver		4.8.0

Summary:	Ksirk
Name:		kde4-%{orgname}
Version:	4.12.2
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b1b4279a9a4bd6aa7ca959126f8b2ae6
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qca-devel >= 2.0.1
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksirk.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post			-p /sbin/ldconfig
%postun			-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksirk
%attr(755,root,root) %{_bindir}/ksirkskineditor
%attr(755,root,root) %ghost %{_libdir}/libiris_ksirk.so.?
%attr(755,root,root) %{_libdir}/libiris_ksirk.so.*.*.*
%{_desktopdir}/kde4/ksirk.desktop
%{_datadir}/apps/ksirk
%{_datadir}/config.kcfg/ksirksettings.kcfg
%{_iconsdir}/*/*/apps/ksirk.png
%{_desktopdir}/kde4/ksirkskineditor.desktop
%{_datadir}/apps/ksirkskineditor
%{_datadir}/config.kcfg/ksirkskineditorsettings.kcfg
%{_datadir}/config/ksirk.knsrc
%{_kdedocdir}/en/ksirkskineditor
