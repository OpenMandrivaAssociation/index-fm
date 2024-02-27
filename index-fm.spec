#define snapshot 20220107

# index-fm's build system seems to miss various library headers for some reason
%global optflags %{optflags} -isystem %{_includedir}/KF5/KIOFileWidgets -isystem %{_includedir}/KF5/KBookmarks -isystem %{_includedir}/qt5/QtXml -isystem %{_includedir}/KF5/Solid

Name:		index-fm
Version:	3.1.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	File manager for Plasma Mobile
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/index-fm/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/index-fm-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/index-fm-%{snapshot}.tar.bz2}
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitFileBrowsing3)

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
%{_datadir}/knotifications5/org.kde.index.notifyrc
