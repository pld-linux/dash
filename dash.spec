Summary:	POSIX-compliant implementation of /bin/sh
Summary(pl):	Zgodna z POSIX implementacja /bin/sh
Name:		dash
Version:	0.5.3
Release:	0.1
License:	GPL v2+
Group:		Applications/Shells
Source0:	http://gondor.apana.org.au/~herbert/dash/files/%{name}-%{version}.tar.gz
# Source0-md5:	1a3cd6669459be4344ec55ec9d4914f8
URL:		http://gondor.apana.org.au/~herbert/dash/
Requires(post):	grep
Requires(preun):	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir			/bin
%define		_shell			%{_bindir}/%{name}

%description
DASH is a POSIX-compliant implementation of /bin/sh that aims to be as
small as possible. It does this without sacrificing speed where
possible. In fact, it is significantly faster than bash (the GNU
Bourne-Again SHell) for most tasks.

DASH is a direct descendant of the NetBSD version of ash (the Almquist
SHell)

%description -l pl
DASH to zgodna z POSIX implementacja /bin/sh, której celem jest jak
najmniejszy rozmiar. Dokonano tego bez po¶wiêcania szybko¶ci je¶li to
mo¿liwe. W rzeczywisto¶ci jest dash jest znacz±co szybszy od basha
(GNU Bourne-Again SHell) przy wiêkszo¶ci zadañ.

DASH to bezpo¶redni nastêpca wersji NetBSD asha (pow³oki Almquist
SHell).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -f /etc/shells ]; then
	umask 022
	echo '%{_shell}' > /etc/shells
else
	grep -q '^%{_shell}$' /etc/shells || echo '%{_shell}' >> /etc/shells
fi

%preun
if [ "$1" = "0" ]; then
	%{__sed} -i -e '/^%(echo %{_shell} | sed -e 's,/,\\/,g')$/d' /etc/shells
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/dash
%{_mandir}/man1/dash.1*
