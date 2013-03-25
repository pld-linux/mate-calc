Summary:	MATE Desktop calculator
Name:		mate-calc
Version:	1.5.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.5/%{name}-%{version}.tar.xz
# Source0-md5:	7ad3813ecee2a67ad05702f5f176b05e
URL:		http://mate-desktop.org/
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.30
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	mate-common
BuildRequires:	mate-desktop-devel
BuildRequires:	mate-doc-utils
Requires:	glib2 >= 1:2.26.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-calc is a powerful graphical calculator with financial, logical
and scientific modes. It uses a multiple precision package to do its
arithmetic to give a high degree of accuracy.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-silent-rules \
	--disable-schemas-compile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

desktop-file-install \
	--remove-category="MATE" \
	--add-category="X-Mate" \
	--delete-original \
	--dir=$RPM_BUILD_ROOT%{_desktopdir} \
$RPM_BUILD_ROOT%{_desktopdir}/*.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_bindir}/mate-calc
%attr(755,root,root) %{_bindir}/mate-calc-cmd
%attr(755,root,root) %{_bindir}/mate-calculator
%{_mandir}/man1/mate-calc-cmd.1*
%{_mandir}/man1/mate-calc.1*
%{_desktopdir}/mate-calc.desktop
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_datadir}/mate-calc
