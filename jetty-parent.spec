Name:           jetty-parent
Version:        32
Release:        1
Summary:        Jetty parent POM file
Group:		Development/Java

License:        ASL 2.0 or EPL
URL:            https://www.eclipse.org/jetty/
Source0:        https://repo1.maven.org/maven2/org/eclipse/jetty/%{name}/%{version}/%{name}-%{version}.pom
# rpmlint config file (fedpkg lint will use this)
Source1:        jetty-parent.rpmlintrc
Source2:        https://www.eclipse.org/legal/epl/epl-v10.html
Source3:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildSystem:	maven
BuildOption:	validate


Requires:       javapackages-filesystem

%description
Jetty parent POM file

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE2} %{SOURCE3} .

%files -f .mfiles
%doc epl-v10.html LICENSE-2.0.txt
