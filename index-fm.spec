#define snapshot 20200312
#define commit 295eb66010df1361349f72fdb96353125acfb52c

# index-fm's build system seems to miss various library headers for some reason
%global optflags %{optflags} -isystem %{_includedir}/KF5/KIOFileWidgets -isystem %{_includedir}/KF5/KBookmarks -isystem %{_includedir}/qt5/QtXml -isystem %{_includedir}/KF5/Solid

Name:		index-fm
Version:	2.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	File manager for Plasma Mobile
Source0:	https://invent.kde.org/maui/index-fm/-/archive/v%{version}/index-fm-v%{version}.tar.bz2
Patch0:		index-2.0-compile.patch
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(MauiKit)
BuildRequires:  cmake(MauiKitFileBrowsing)

%description
File manager for Plasma Mobile

%prep
%if 0%{?snapshot:1}
%autosetup -p1 -n %{name}-master-%{commit}
%else
%autosetup -p1 -n %{name}-v%{version}
%endif
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/index
%{_datadir}/applications/org.kde.index.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/org.kde.index.appdata.xml
%{_datadir}/knotifications5/org.kde.index.notifyrc
