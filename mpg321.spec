Summary:	Mpg123-clone
Name:		mpg321
Version:	0.3.2
Release:	2
Group:		Sound
License:	GPLv2+
URL:		https://sourceforge.net/projects/mpg321
Source:		http://downloads.sourceforge.net/%{name}/%{name}_%{version}.orig.tar.gz
Patch0:		mpg321-help.patch
Patch1:		mpg321-0.2.12-fix-str-fmt.patch
Patch2:		mpg321-0.2.11-set-channel-mapping.patch
BuildRequires:	mad-devel >= 0.13 
BuildRequires:	libao-devel >= 0.8.0
BuildRequires:	libid3tag-devel
BuildRequires:	libalsa-devel

%description
mpg321 is a Free clone of mpg123, a command-line MP3 player. It is designed to
be a drop-in replacement for mpg123, and therefore its interface has been
designed around that of mpg123, without using any of its code. mpg321 has been
designed for use with frontends such as gqmpeg, although it is just as useful
on the command-line. Unlike mpg123, it supports ESD and ALSA output without
recompiling, and it does all MP3 decoding with only fixed-point math by using
the mad MPEG audio decoder library.


%prep
%setup -qn %{name}-%{version}-orig
%patch0 -p0
%patch1 -p0
%patch2 -p1
# Fix wrong-file-end-of-line-encoding
sed -i 's/\r//' NEWS

%build
%configure2_5x --enable-mpg123-symlink=no # Uncomment option once mainstream.
%make

%install
%makeinstall_std

%files
%doc BUGS AUTHORS HACKING NEWS README* THANKS TODO
%{_mandir}/man1/*
%{_bindir}/*


%changelog
* Tue Apr 10 2012 Johnny A. Solbu <solbu@mandriva.org> 0.3.2-1
+ Revision: 790117
- Update BuildRequires
- New version
- Spec cleanup
- Don't ship COPYING, license doesn't require it

* Fri Jul 16 2010 Funda Wang <fwang@mandriva.org> 0.2.12-1mdv2011.0
+ Revision: 554412
- new version 0.2.12

* Tue May 11 2010 Pascal Terjan <pterjan@mandriva.org> 0.2.11-3mdv2010.1
+ Revision: 544471
- Set a channel mapping to avoid crash on recent libao (#59019)

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 0.2.11-2mdv2010.1
+ Revision: 528369
- rebuild

* Sun Nov 15 2009 Funda Wang <fwang@mandriva.org> 0.2.11-1mdv2010.1
+ Revision: 466207
- new version 0.2.11

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.2.10-10mdv2009.0
+ Revision: 252961
- rebuild

* Tue Mar 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.10-8mdv2008.1
+ Revision: 189862
- fix #37847 (mpg321 doesn't list pulseaudio output)

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.2.10-7mdv2008.1
+ Revision: 170988
- rebuild
- summary is not licence tag
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix spacing at top of description

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 0.2.10-6mdv2008.1
+ Revision: 140963
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Jan 11 2007 Götz Waschk <waschk@mandriva.org> 0.2.10-6mdv2007.0
+ Revision: 107459
- Import mpg321

* Thu Jan 11 2007 Götz Waschk <waschk@mandriva.org> 0.2.10-6mdv2007.1
- Rebuild

* Fri Oct 07 2005 Lenny Cartier <lenny@mandriva.com> 0.2.10-5mdk
- rebuild

* Fri Jul 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.2.10-4mdk
- rebuild

