Summary:	MATE Desktop calculator
Summary(pl.UTF-8):	Kalkulator dla środowiska MATE Desktop
Name:		mate-calc
Version:	1.28.0
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://pub.mate-desktop.org/releases/1.28/%{name}-%{version}.tar.xz
# Source0-md5:	3492897f5c92b556df8ee9715db6db48
URL:		https://wiki.mate-desktop.org/mate-desktop/applications/mate-calc/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libmpc-devel
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mate-common
BuildRequires:	mpfr-devel >= 4.0.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.50.0
Requires:	gtk+3 >= 3.22
Requires:	mpfr >= 4.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-calc is a powerful graphical calculator with financial, logical
and scientific modes. It uses a multiple precision package to do its
arithmetic to give a high degree of accuracy. mate-calc is a fork of
gnome-calc.

%description -l pl.UTF-8
mate-calc to graficzny kalkulator o bogatych możliwościach, z trybami
finansowym, logicznym i naukowym. Wykorzystuje pakiet wielokrotnej
precyzji w celu zapewnienia arytmentyki o dużym stopniu dokładności.
mate-calc jest odgałęzieniem programu gnome-calc.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules
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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{es_ES,frp,ie,ku_IQ,pms}
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/{frp,ie,ku_IQ,pms}

%find_lang %{name} --with-mate

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README.md
%attr(755,root,root) %{_bindir}/mate-calc
%attr(755,root,root) %{_bindir}/mate-calc-cmd
%attr(755,root,root) %{_bindir}/mate-calculator
%{_mandir}/man1/mate-calc.1*
%{_mandir}/man1/mate-calc-cmd.1*
%{_datadir}/metainfo/mate-calc.appdata.xml
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_desktopdir}/mate-calc.desktop
