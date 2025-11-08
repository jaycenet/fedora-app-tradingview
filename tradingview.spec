Name:           tradingview-desktop
Version:        2.8.1
Release:        1%{?dist}
Summary:        TradingView Desktop for Linux

License:        Proprietary
URL:            https://www.tradingview.com/desktop/
Source0:        tradingview-desktop.deb

BuildArch:      x86_64
Requires:       libappindicator-gtk3, gtk3, nss

%description
TradingView Desktop is a standalone application for TradingView with improved performance,
workspace management, and native notifications.

%prep
%autosetup -c -T
cp %{SOURCE0} .

%build
# Nothing to build

%install
mkdir -p %{buildroot}/opt/tradingview
# Convert the deb to a tarball and extract
alien --to-tgz tradingview-desktop.deb
tar xf tradingview-desktop*.tgz -C %{buildroot}/opt/tradingview --strip-components=2

# Create desktop entry
mkdir -p %{buildroot}/usr/share/applications
cat > %{buildroot}/usr/share/applications/tradingview.desktop <<EOF
[Desktop Entry]
Name=TradingView
Exec=/opt/tradingview/tradingview
Icon=/opt/tradingview/resources/app/icon.png
Type=Application
Categories=Finance;Office;
EOF

%files
/opt/tradingview
/usr/share/applications/tradingview.desktop

%changelog
* Sat Nov 08 2025 Jayce <jayce.net@gmail.com> - 2.8.1-1
- Initial RPM build from official .deb package
