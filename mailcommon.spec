#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: 3d985eb
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : mailcommon
Version  : 24.02.0
Release  : 82
URL      : https://download.kde.org/stable/release-service/24.02.0/src/mailcommon-24.02.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.02.0/src/mailcommon-24.02.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.02.0/src/mailcommon-24.02.0.tar.xz.sig
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
BuildRequires : kcontacts-dev
BuildRequires : kidentitymanagement-dev
BuildRequires : kimap-staticdev
BuildRequires : kmailtransport-dev
BuildRequires : kmime-dev
BuildRequires : kpimtextedit-dev
BuildRequires : libkdepim-dev
BuildRequires : libkleo-dev
BuildRequires : mailimporter-dev
BuildRequires : messagelib-dev
BuildRequires : phonon-dev
BuildRequires : pimcommon-dev
BuildRequires : qt6base-dev
BuildRequires : qt6webengine-dev
BuildRequires : syntax-highlighting-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n mailcommon-24.02.0
cd %{_builddir}/mailcommon-24.02.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710433805
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake .. -DQT_MAJOR_VERSION=6
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710433805
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mailcommon
cp %{_builddir}/mailcommon-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/mailcommon/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/mailcommon/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/2a638514c87c4923c0570c55822620fad56f2a33 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/mailcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/mailcommon/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/mailcommon/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/mailcommon-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/mailcommon/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/mailcommon-%{version}/metainfo.yaml.license %{buildroot}/usr/share/package-licenses/mailcommon/7ff5a7dd2c915b2b34329c892e06917c5f82f3a4 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libmailcommon6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/mailcommon.categories
/usr/share/qlogging-categories6/mailcommon.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KPim6/MailCommon/MailCommon/AccountConfigOrderDialog
/usr/include/KPim6/MailCommon/MailCommon/AddTagDialog
/usr/include/KPim6/MailCommon/MailCommon/BackupJob
/usr/include/KPim6/MailCommon/MailCommon/CollectionExpiryPage
/usr/include/KPim6/MailCommon/MailCommon/CollectionExpiryWidget
/usr/include/KPim6/MailCommon/MailCommon/CollectionGeneralPage
/usr/include/KPim6/MailCommon/MailCommon/CollectionGeneralWidget
/usr/include/KPim6/MailCommon/MailCommon/CollectionTemplatesWidget
/usr/include/KPim6/MailCommon/MailCommon/CollectionViewWidget
/usr/include/KPim6/MailCommon/MailCommon/CryptoUtils
/usr/include/KPim6/MailCommon/MailCommon/DBusOperators
/usr/include/KPim6/MailCommon/MailCommon/EntityCollectionOrderProxyModel
/usr/include/KPim6/MailCommon/MailCommon/ExpireCollectionAttribute
/usr/include/KPim6/MailCommon/MailCommon/FavoriteCollectionOrderProxyModel
/usr/include/KPim6/MailCommon/MailCommon/FavoriteCollectionWidget
/usr/include/KPim6/MailCommon/MailCommon/FilterAction
/usr/include/KPim6/MailCommon/MailCommon/FilterActionDict
/usr/include/KPim6/MailCommon/MailCommon/FilterImporterAbstract
/usr/include/KPim6/MailCommon/MailCommon/FilterImporterBalsa
/usr/include/KPim6/MailCommon/MailCommon/FilterImporterClawsMail
/usr/include/KPim6/MailCommon/MailCommon/FilterImporterExporter
/usr/include/KPim6/MailCommon/MailCommon/FilterImporterPathCache
/usr/include/KPim6/MailCommon/MailCommon/FilterLog
/usr/include/KPim6/MailCommon/MailCommon/FilterManager
/usr/include/KPim6/MailCommon/MailCommon/FolderCollectionMonitor
/usr/include/KPim6/MailCommon/MailCommon/FolderJob
/usr/include/KPim6/MailCommon/MailCommon/FolderRequester
/usr/include/KPim6/MailCommon/MailCommon/FolderSelectionDialog
/usr/include/KPim6/MailCommon/MailCommon/FolderSettings
/usr/include/KPim6/MailCommon/MailCommon/FolderTreeView
/usr/include/KPim6/MailCommon/MailCommon/FolderTreeWidget
/usr/include/KPim6/MailCommon/MailCommon/FolderTreeWidgetProxyModel
/usr/include/KPim6/MailCommon/MailCommon/ItemContext
/usr/include/KPim6/MailCommon/MailCommon/JobScheduler
/usr/include/KPim6/MailCommon/MailCommon/KMFilterDialog
/usr/include/KPim6/MailCommon/MailCommon/MDNWarningJob
/usr/include/KPim6/MailCommon/MailCommon/MailFilter
/usr/include/KPim6/MailCommon/MailCommon/MailInterfaces
/usr/include/KPim6/MailCommon/MailCommon/MailKernel
/usr/include/KPim6/MailCommon/MailCommon/MailUtil
/usr/include/KPim6/MailCommon/MailCommon/RedirectDialog
/usr/include/KPim6/MailCommon/MailCommon/ResourceReadConfigFile
/usr/include/KPim6/MailCommon/MailCommon/SearchPattern
/usr/include/KPim6/MailCommon/MailCommon/SearchPatternEdit
/usr/include/KPim6/MailCommon/MailCommon/SearchRule
/usr/include/KPim6/MailCommon/MailCommon/SearchRuleStatus
/usr/include/KPim6/MailCommon/MailCommon/SnippetTreeView
/usr/include/KPim6/MailCommon/MailCommon/SnippetWidget
/usr/include/KPim6/MailCommon/MailCommon/SnippetsManager
/usr/include/KPim6/MailCommon/MailCommon/SnippetsModel
/usr/include/KPim6/MailCommon/MailCommon/Tag
/usr/include/KPim6/MailCommon/MailCommon/TagWidget
/usr/include/KPim6/MailCommon/mailcommon/accountconfigorderdialog.h
/usr/include/KPim6/MailCommon/mailcommon/addtagdialog.h
/usr/include/KPim6/MailCommon/mailcommon/backupjob.h
/usr/include/KPim6/MailCommon/mailcommon/collectionexpirypage.h
/usr/include/KPim6/MailCommon/mailcommon/collectionexpirywidget.h
/usr/include/KPim6/MailCommon/mailcommon/collectiongeneralpage.h
/usr/include/KPim6/MailCommon/mailcommon/collectiongeneralwidget.h
/usr/include/KPim6/MailCommon/mailcommon/collectiontemplateswidget.h
/usr/include/KPim6/MailCommon/mailcommon/collectionviewwidget.h
/usr/include/KPim6/MailCommon/mailcommon/cryptoutils.h
/usr/include/KPim6/MailCommon/mailcommon/dbusoperators.h
/usr/include/KPim6/MailCommon/mailcommon/entitycollectionorderproxymodel.h
/usr/include/KPim6/MailCommon/mailcommon/expirecollectionattribute.h
/usr/include/KPim6/MailCommon/mailcommon/favoritecollectionorderproxymodel.h
/usr/include/KPim6/MailCommon/mailcommon/favoritecollectionwidget.h
/usr/include/KPim6/MailCommon/mailcommon/filteraction.h
/usr/include/KPim6/MailCommon/mailcommon/filteractiondict.h
/usr/include/KPim6/MailCommon/mailcommon/filterimporterabstract.h
/usr/include/KPim6/MailCommon/mailcommon/filterimporterbalsa.h
/usr/include/KPim6/MailCommon/mailcommon/filterimporterclawsmail.h
/usr/include/KPim6/MailCommon/mailcommon/filterimporterexporter.h
/usr/include/KPim6/MailCommon/mailcommon/filterimporterpathcache.h
/usr/include/KPim6/MailCommon/mailcommon/filterlog.h
/usr/include/KPim6/MailCommon/mailcommon/filtermanager.h
/usr/include/KPim6/MailCommon/mailcommon/foldercollectionmonitor.h
/usr/include/KPim6/MailCommon/mailcommon/folderjob.h
/usr/include/KPim6/MailCommon/mailcommon/folderrequester.h
/usr/include/KPim6/MailCommon/mailcommon/folderselectiondialog.h
/usr/include/KPim6/MailCommon/mailcommon/foldersettings.h
/usr/include/KPim6/MailCommon/mailcommon/foldertreeview.h
/usr/include/KPim6/MailCommon/mailcommon/foldertreewidget.h
/usr/include/KPim6/MailCommon/mailcommon/foldertreewidgetproxymodel.h
/usr/include/KPim6/MailCommon/mailcommon/itemcontext.h
/usr/include/KPim6/MailCommon/mailcommon/jobscheduler.h
/usr/include/KPim6/MailCommon/mailcommon/kmfilterdialog.h
/usr/include/KPim6/MailCommon/mailcommon/mailcommon_export.h
/usr/include/KPim6/MailCommon/mailcommon/mailcommonsettings_base.h
/usr/include/KPim6/MailCommon/mailcommon/mailfilter.h
/usr/include/KPim6/MailCommon/mailcommon/mailinterfaces.h
/usr/include/KPim6/MailCommon/mailcommon/mailkernel.h
/usr/include/KPim6/MailCommon/mailcommon/mailutil.h
/usr/include/KPim6/MailCommon/mailcommon/mdnwarningjob.h
/usr/include/KPim6/MailCommon/mailcommon/pop3settings.h
/usr/include/KPim6/MailCommon/mailcommon/redirectdialog.h
/usr/include/KPim6/MailCommon/mailcommon/resourcereadconfigfile.h
/usr/include/KPim6/MailCommon/mailcommon/searchpattern.h
/usr/include/KPim6/MailCommon/mailcommon/searchpatternedit.h
/usr/include/KPim6/MailCommon/mailcommon/searchrule.h
/usr/include/KPim6/MailCommon/mailcommon/searchrulestatus.h
/usr/include/KPim6/MailCommon/mailcommon/snippetsmanager.h
/usr/include/KPim6/MailCommon/mailcommon/snippetsmodel.h
/usr/include/KPim6/MailCommon/mailcommon/snippettreeview.h
/usr/include/KPim6/MailCommon/mailcommon/snippetwidget.h
/usr/include/KPim6/MailCommon/mailcommon/tag.h
/usr/include/KPim6/MailCommon/mailcommon/tagwidget.h
/usr/include/KPim6/MailCommon/mailcommon_version.h
/usr/lib64/cmake/KPim6MailCommon/KPim6MailCommonConfig.cmake
/usr/lib64/cmake/KPim6MailCommon/KPim6MailCommonConfigVersion.cmake
/usr/lib64/cmake/KPim6MailCommon/KPim6MailCommonTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KPim6MailCommon/KPim6MailCommonTargets.cmake
/usr/lib64/libKPim6MailCommon.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKPim6MailCommon.so.6.0.0
/V3/usr/lib64/qt6/plugins/designer/mailcommon6widgets.so
/usr/lib64/libKPim6MailCommon.so.6
/usr/lib64/libKPim6MailCommon.so.6.0.0
/usr/lib64/qt6/plugins/designer/mailcommon6widgets.so

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
/usr/share/package-licenses/mailcommon/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/mailcommon/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libmailcommon6.lang
%defattr(-,root,root,-)

