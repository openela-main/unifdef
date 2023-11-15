Summary: Tool for removing ifdef'd lines
Name: unifdef
Version: 2.10
Release: 21%{?dist}
License: BSD
URL: http://dotat.at/prog/unifdef/
Source0: http://dotat.at/prog/unifdef/unifdef-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires: pkgconfig

%description
Unifdef is useful for removing ifdefed lines from a file while otherwise
leaving the file alone. Unifdef acts on #ifdef, #ifndef, #else, and #endif
lines, and it knows only enough about C and C++ to know when one of these
is inactive because it is inside a comment, or a single or double quote.

%prep
%setup -q

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d -m0755 $RPM_BUILD_ROOT%{_bindir}
install -p -m0755 unifdef $RPM_BUILD_ROOT%{_bindir}/unifdef
install -p -m0755 unifdefall.sh $RPM_BUILD_ROOT%{_bindir}/unifdefall.sh

install -d -m0755 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m0644 unifdef.1 $RPM_BUILD_ROOT%{_mandir}/man1/unifdef.1


%files
%{_bindir}/unifdef
%{_bindir}/unifdefall.sh
%{_mandir}/man1/unifdef.1.gz


%changelog
* Tue Apr 25 2023 Michael Catanzaro <mcatanzaro@redhat.com> - 2.10-21
- Rebuild so distrobaker notices this package
  Resolves: #2180560

* Tue Apr 18 2023 Michael Catanzaro <mcatanzaro@redhat.com> - 2.10-20
- Import from Fedora. Sorry, cannot keep the changelog history.
