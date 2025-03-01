#define snapshot 20220107

# index-fm's build system seems to miss various library headers for some reason
%global optflags %{optflags} -isystem %{_includedir}/KF6/KIOFileWidgets -isystem %{_includedir}/KF6/KBookmarks -isystem %{_includedir}/qt6/QtXml -isystem %{_includedir}/KF6/Solid

Name:		index-fm
Version:	4.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	File manager for Plasma Mobile
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/index-fm/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/index-fm-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/index-fm-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitFileBrowsing4)

%description
File manager for Plasma Mobile

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang index-fm

%files -f index-fm.lang
%{_bindir}/index
%{_datadir}/applications/org.kde.index.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.kde.index.appdata.xml
%{_datadir}/knotifications6/org.kde.index.notifyrc
