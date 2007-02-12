Summary:	POSIX-compliant implementation of /bin/sh
Summary(pl.UTF-8):   Zgodna z POSIX implementacja /bin/sh
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

%description -l pl.UTF-8
DASH to zgodna z POSIX implementacja /bin/sh, której celem jest jak
najmniejszy rozmiar. Dokonano tego bez poświęcania szybkości jeśli to
możliwe. W rzeczywistości jest dash jest znacząco szybszy od basha
(GNU Bourne-Again SHell) przy większości zadań.

DASH to bezpośredni następca wersji NetBSD asha (powłoki Almquist
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
