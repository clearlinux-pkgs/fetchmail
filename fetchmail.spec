#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE412B156EFF3855A (mandree@FreeBSD.org)
#
Name     : fetchmail
Version  : 6.4.26
Release  : 25
URL      : https://sourceforge.net/projects/fetchmail/files/branch_6.4/fetchmail-6.4.26.tar.xz
Source0  : https://sourceforge.net/projects/fetchmail/files/branch_6.4/fetchmail-6.4.26.tar.xz
Source1  : https://sourceforge.net/projects/fetchmail/files/branch_6.4/fetchmail-6.4.26.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: fetchmail-bin = %{version}-%{release}
Requires: fetchmail-license = %{version}-%{release}
Requires: fetchmail-locales = %{version}-%{release}
Requires: fetchmail-man = %{version}-%{release}
Requires: procmail
BuildRequires : bison
BuildRequires : flex
BuildRequires : openssl-dev
BuildRequires : procmail

%description
Fetchmail is a free, full-featured, robust, and well-documented remote
mail retrieval and forwarding utility intended to be used over
on-demand TCP/IP links (such as SLIP or PPP connections).  It
retrieves mail from remote mail servers and forwards it to your local
(client) machine's delivery system, so it can then be be read by
normal mail user agents such as mutt, elm, pine, (x)emacs/gnus, or mailx.
Comes with an interactive GUI configurator suitable for end-users.

%package bin
Summary: bin components for the fetchmail package.
Group: Binaries
Requires: fetchmail-license = %{version}-%{release}

%description bin
bin components for the fetchmail package.


%package license
Summary: license components for the fetchmail package.
Group: Default

%description license
license components for the fetchmail package.


%package locales
Summary: locales components for the fetchmail package.
Group: Default

%description locales
locales components for the fetchmail package.


%package man
Summary: man components for the fetchmail package.
Group: Default

%description man
man components for the fetchmail package.


%prep
%setup -q -n fetchmail-6.4.26
cd %{_builddir}/fetchmail-6.4.26

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640620333
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1640620333
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fetchmail
cp %{_builddir}/fetchmail-6.4.26/m4-local/ac-archive-license.txt %{buildroot}/usr/share/package-licenses/fetchmail/8534c1a6b8958dc54d9478b5195976bc3fb98f6a
%make_install
%find_lang fetchmail
## install_append content
rm -rf %{buildroot}/usr/lib/python*
rm -rf %{buildroot}/usr/bin/fetchmailconf
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/fetchmail

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fetchmail/8534c1a6b8958dc54d9478b5195976bc3fb98f6a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/fetchmail.1
/usr/share/man/man1/fetchmailconf.1

%files locales -f fetchmail.lang
%defattr(-,root,root,-)

