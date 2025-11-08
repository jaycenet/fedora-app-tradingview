Name:           tradingview-desktop
Version:        2.13.0
Release:        1%{?dist}
Summary:        TradingView Desktop for Linux

License:        Proprietary
URL:            https://www.tradingview.com/desktop/
Source0:        https://tvd-packages.tradingview.com/ubuntu/stable/pool/multiverse/t/tradingview/jammy/tradingview-%{version}-1_amd64.deb

BuildArch:      x86_64
Requires:       libappindicator-gtk3, gtk3, nss, wget, alien

%description
TradingView Desktop is a standalone application for TradingView with improved performance,
workspace management, and native notifications.

%prep
%autosetup -c -T

# Télécharge la version exacte du .deb depuis TradingView
echo "Téléchargement de TradingView Desktop %{version}..."
wget -O tradingview-desktop.deb %{SOURCE0}

%build
# Rien à compiler

%install
mkdir -p %{buildroot}/opt/tradingview

# Convertit le .deb en archive tar.gz et l’extrait
alien --to-tgz tradingview-desktop.deb
tar xf tradingview-desktop*.tgz -C %{buildroot}/opt/tradingview --strip-components=2

# Crée le raccourci d'application
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
* Sat Nov 08 2025 ChatGPT <you@example.com> - 2.13.0-1
- RPM build for TradingView Desktop 2.13.0 with automatic .deb download
