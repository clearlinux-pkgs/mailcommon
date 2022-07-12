#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : mailcommon
Version  : 22.04.3
Release  : 45
URL      : https://download.kde.org/stable/release-service/22.04.3/src/mailcommon-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/mailcommon-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/mailcommon-22.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-3.0
Requires: mailcommon-data = %{version}-%{release}
Requires: mailcommon-lib = %{version}-%{release}
Requires: mailcommon-license = %{version}-%{release}
Requires: mailcommon-locales = %{version}-%{release}
BuildRequires : akonadi-contacts-dev
BuildRequires : akonadi-dev
BuildRequires : akonadi-mime-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gpgme-dev
BuildRequires : gpgme-extras
BuildRequires : grantlee-dev
BuildRequires : grantleetheme-dev
BuildRequires : karchive-dev
BuildRequires : kcompletion-dev
BuildRequires : kconfig-dev
BuildRequires : kconfigwidgets-dev
BuildRequires : kcontacts-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kiconthemes-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kio-dev
BuildRequires : kitemmodels-dev
BuildRequires : kitemviews-dev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : ktextwidgets-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : kxmlgui-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : mailimporter-dev
BuildRequires : messagelib-dev
BuildRequires : phonon-dev
BuildRequires : pimcommon-dev
BuildRequires : syntax-highlighting-dev

%description
No detailed description available

%package data
Summary: data components for the mailcommon package.
Group: Data

%description data
data components for the mailcommon package.


%package dev
Summary: dev components for the mailcommon package.
Group: Development
Requires: mailcommon-lib = %{version}-%{release}
Requires: mailcommon-data = %{version}-%{release}
Provides: mailcommon-devel = %{version}-%{release}
Requires: mailcommon = %{version}-%{release}

%description dev
dev components for the mailcommon package.


%package lib
Summary: lib components for the mailcommon package.
Group: Libraries
Requires: mailcommon-data = %{version}-%{release}
Requires: mailcommon-license = %{version}-%{release}

%description lib
lib components for the mailcommon package.


%package license
Summary: license components for the mailcommon package.
Group: Default

%description license
license components for the mailcommon package.


%package locales
Summary: locales components for the mailcommon package.
Group: Default

%description locales
locales components for the mailcommon package.


%prep
%setup -q -n mailcommon-22.04.3
cd %{_builddir}/mailcommon-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657589059
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657589059
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mailcommon
cp %{_builddir}/mailcommon-22.04.3/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/mailcommon/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
cp %{_builddir}/mailcommon-22.04.3/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/mailcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
cp %{_builddir}/mailcommon-22.04.3/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/mailcommon/8287b608d3fa40ef401339fd907ca1260c964123
cp %{_builddir}/mailcommon-22.04.3/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/2a638514c87c4923c0570c55822620fad56f2a33
cp %{_builddir}/mailcommon-22.04.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/mailcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb
cp %{_builddir}/mailcommon-22.04.3/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/6091db0aead0d90182b93d3c0d09ba93d188f907
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/mailcommon/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/mailcommon-22.04.3/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/mailcommon-22.04.3/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/mailcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
pushd clr-build
%make_install
popd
%find_lang libmailcommon

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/mailcommon.categories
/usr/share/qlogging-categories5/mailcommon.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/MailCommon/MailCommon/AccountConfigOrderDialog
/usr/include/KF5/MailCommon/MailCommon/AddTagDialog
/usr/include/KF5/MailCommon/MailCommon/BackupJob
/usr/include/KF5/MailCommon/MailCommon/CollectionExpiryPage
/usr/include/KF5/MailCommon/MailCommon/CollectionExpiryWidget
/usr/include/KF5/MailCommon/MailCommon/CollectionGeneralPage
/usr/include/KF5/MailCommon/MailCommon/CollectionGeneralWidget
/usr/include/KF5/MailCommon/MailCommon/CollectionTemplatesWidget
/usr/include/KF5/MailCommon/MailCommon/CollectionViewWidget
/usr/include/KF5/MailCommon/MailCommon/CryptoUtils
/usr/include/KF5/MailCommon/MailCommon/DBusOperators
/usr/include/KF5/MailCommon/MailCommon/ExpireCollectionAttribute
/usr/include/KF5/MailCommon/MailCommon/FavoriteCollectionOrderProxyModel
/usr/include/KF5/MailCommon/MailCommon/FavoriteCollectionWidget
/usr/include/KF5/MailCommon/MailCommon/FilterAction
/usr/include/KF5/MailCommon/MailCommon/FilterActionDict
/usr/include/KF5/MailCommon/MailCommon/FilterImporterAbstract
/usr/include/KF5/MailCommon/MailCommon/FilterImporterBalsa
/usr/include/KF5/MailCommon/MailCommon/FilterImporterClawsMail
/usr/include/KF5/MailCommon/MailCommon/FilterImporterExporter
/usr/include/KF5/MailCommon/MailCommon/FilterImporterPathCache
/usr/include/KF5/MailCommon/MailCommon/FilterLog
/usr/include/KF5/MailCommon/MailCommon/FilterManager
/usr/include/KF5/MailCommon/MailCommon/FolderCollectionMonitor
/usr/include/KF5/MailCommon/MailCommon/FolderJob
/usr/include/KF5/MailCommon/MailCommon/FolderRequester
/usr/include/KF5/MailCommon/MailCommon/FolderSelectionDialog
/usr/include/KF5/MailCommon/MailCommon/FolderSettings
/usr/include/KF5/MailCommon/MailCommon/FolderTreeView
/usr/include/KF5/MailCommon/MailCommon/FolderTreeWidget
/usr/include/KF5/MailCommon/MailCommon/FolderTreeWidgetProxyModel
/usr/include/KF5/MailCommon/MailCommon/ItemContext
/usr/include/KF5/MailCommon/MailCommon/JobScheduler
/usr/include/KF5/MailCommon/MailCommon/KMFilterDialog
/usr/include/KF5/MailCommon/MailCommon/MDNStateAttribute
/usr/include/KF5/MailCommon/MailCommon/MailFilter
/usr/include/KF5/MailCommon/MailCommon/MailInterfaces
/usr/include/KF5/MailCommon/MailCommon/MailKernel
/usr/include/KF5/MailCommon/MailCommon/MailUtil
/usr/include/KF5/MailCommon/MailCommon/RedirectDialog
/usr/include/KF5/MailCommon/MailCommon/ResourceReadConfigFile
/usr/include/KF5/MailCommon/MailCommon/SearchPattern
/usr/include/KF5/MailCommon/MailCommon/SearchPatternEdit
/usr/include/KF5/MailCommon/MailCommon/SearchRule
/usr/include/KF5/MailCommon/MailCommon/SearchRuleStatus
/usr/include/KF5/MailCommon/MailCommon/SendMdnHandler
/usr/include/KF5/MailCommon/MailCommon/SnippetTreeView
/usr/include/KF5/MailCommon/MailCommon/SnippetWidget
/usr/include/KF5/MailCommon/MailCommon/SnippetsManager
/usr/include/KF5/MailCommon/MailCommon/SnippetsModel
/usr/include/KF5/MailCommon/MailCommon/Tag
/usr/include/KF5/MailCommon/MailCommon/TagWidget
/usr/include/KF5/MailCommon/mailcommon/accountconfigorderdialog.h
/usr/include/KF5/MailCommon/mailcommon/addtagdialog.h
/usr/include/KF5/MailCommon/mailcommon/backupjob.h
/usr/include/KF5/MailCommon/mailcommon/collectionexpirypage.h
/usr/include/KF5/MailCommon/mailcommon/collectionexpirywidget.h
/usr/include/KF5/MailCommon/mailcommon/collectiongeneralpage.h
/usr/include/KF5/MailCommon/mailcommon/collectiongeneralwidget.h
/usr/include/KF5/MailCommon/mailcommon/collectiontemplateswidget.h
/usr/include/KF5/MailCommon/mailcommon/collectionviewwidget.h
/usr/include/KF5/MailCommon/mailcommon/cryptoutils.h
/usr/include/KF5/MailCommon/mailcommon/dbusoperators.h
/usr/include/KF5/MailCommon/mailcommon/expirecollectionattribute.h
/usr/include/KF5/MailCommon/mailcommon/favoritecollectionorderproxymodel.h
/usr/include/KF5/MailCommon/mailcommon/favoritecollectionwidget.h
/usr/include/KF5/MailCommon/mailcommon/filteraction.h
/usr/include/KF5/MailCommon/mailcommon/filteractiondict.h
/usr/include/KF5/MailCommon/mailcommon/filterimporterabstract.h
/usr/include/KF5/MailCommon/mailcommon/filterimporterbalsa.h
/usr/include/KF5/MailCommon/mailcommon/filterimporterclawsmail.h
/usr/include/KF5/MailCommon/mailcommon/filterimporterexporter.h
/usr/include/KF5/MailCommon/mailcommon/filterimporterpathcache.h
/usr/include/KF5/MailCommon/mailcommon/filterlog.h
/usr/include/KF5/MailCommon/mailcommon/filtermanager.h
/usr/include/KF5/MailCommon/mailcommon/foldercollectionmonitor.h
/usr/include/KF5/MailCommon/mailcommon/folderjob.h
/usr/include/KF5/MailCommon/mailcommon/folderrequester.h
/usr/include/KF5/MailCommon/mailcommon/folderselectiondialog.h
/usr/include/KF5/MailCommon/mailcommon/foldersettings.h
/usr/include/KF5/MailCommon/mailcommon/foldertreeview.h
/usr/include/KF5/MailCommon/mailcommon/foldertreewidget.h
/usr/include/KF5/MailCommon/mailcommon/foldertreewidgetproxymodel.h
/usr/include/KF5/MailCommon/mailcommon/itemcontext.h
/usr/include/KF5/MailCommon/mailcommon/jobscheduler.h
/usr/include/KF5/MailCommon/mailcommon/kmfilterdialog.h
/usr/include/KF5/MailCommon/mailcommon/mailcommon_export.h
/usr/include/KF5/MailCommon/mailcommon/mailcommonsettings_base.h
/usr/include/KF5/MailCommon/mailcommon/mailfilter.h
/usr/include/KF5/MailCommon/mailcommon/mailinterfaces.h
/usr/include/KF5/MailCommon/mailcommon/mailkernel.h
/usr/include/KF5/MailCommon/mailcommon/mailutil.h
/usr/include/KF5/MailCommon/mailcommon/mdnstateattribute.h
/usr/include/KF5/MailCommon/mailcommon/pop3settings.h
/usr/include/KF5/MailCommon/mailcommon/redirectdialog.h
/usr/include/KF5/MailCommon/mailcommon/resourcereadconfigfile.h
/usr/include/KF5/MailCommon/mailcommon/searchpattern.h
/usr/include/KF5/MailCommon/mailcommon/searchpatternedit.h
/usr/include/KF5/MailCommon/mailcommon/searchrule.h
/usr/include/KF5/MailCommon/mailcommon/searchrulestatus.h
/usr/include/KF5/MailCommon/mailcommon/sendmdnhandler.h
/usr/include/KF5/MailCommon/mailcommon/snippetsmanager.h
/usr/include/KF5/MailCommon/mailcommon/snippetsmodel.h
/usr/include/KF5/MailCommon/mailcommon/snippettreeview.h
/usr/include/KF5/MailCommon/mailcommon/snippetwidget.h
/usr/include/KF5/MailCommon/mailcommon/tag.h
/usr/include/KF5/MailCommon/mailcommon/tagwidget.h
/usr/include/KF5/MailCommon/mailcommon_export.h
/usr/include/KF5/MailCommon/mailcommon_version.h
/usr/lib64/cmake/KF5MailCommon/KF5MailCommonConfig.cmake
/usr/lib64/cmake/KF5MailCommon/KF5MailCommonConfigVersion.cmake
/usr/lib64/cmake/KF5MailCommon/KF5MailCommonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5MailCommon/KF5MailCommonTargets.cmake
/usr/lib64/libKF5MailCommon.so
/usr/lib64/qt5/mkspecs/modules/qt_MailCommon.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5MailCommon.so.5
/usr/lib64/libKF5MailCommon.so.5.20.3
/usr/lib64/qt5/plugins/designer/mailcommonwidgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mailcommon/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/mailcommon/2a638514c87c4923c0570c55822620fad56f2a33
/usr/share/package-licenses/mailcommon/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/mailcommon/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/mailcommon/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/mailcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4
/usr/share/package-licenses/mailcommon/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/mailcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/mailcommon/c085897bc39e05746ffd2d889a6e84ff1b7ae2d9
/usr/share/package-licenses/mailcommon/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/mailcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libmailcommon.lang
%defattr(-,root,root,-)

