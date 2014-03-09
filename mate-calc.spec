#
# Conditional build:
%bcond_with	gtk3	# use GTK+ 3.x instead of 2.x

Summary:	MATE Desktop calculator
Summary(pl.UTF-8):	Kalkulator dla środowiska MATE Desktop
Name:		mate-calc
Version:	1.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.8/%{name}-%{version}.tar.xz
# Source0-md5:	8a22d9a65599163fa94d240fab5c15f2
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	bison
BuildRequires:	desktop-file-utils
BuildRequires:	flex
BuildRequires:	glib2-devel >= 1:2.30
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.18.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	mate-common
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.30
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.18.0}
%{?with_gtk3:Requires:	gtk+3 >= 3.0.0}
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
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules \
	%{?with_gtk3:--with-gtk=3.0}
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

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/cmn

%find_lang %{name} --with-mate --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/mate-calc
%attr(755,root,root) %{_bindir}/mate-calc-cmd
%attr(755,root,root) %{_bindir}/mate-calculator
%{_mandir}/man1/mate-calc.1*
%{_mandir}/man1/mate-calc-cmd.1*
%{_datadir}/glib-2.0/schemas/org.mate.calc.gschema.xml
%{_datadir}/mate-calc
%{_desktopdir}/mate-calc.desktop
