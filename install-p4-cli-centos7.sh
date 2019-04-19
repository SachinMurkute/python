#!/usr/bin/env bash

#
# P4 CLIENT
# Script source: https://gist.github.com/ssmythe/193681fe70b5af289881

echo "p4-cli: Install p4 yum repo"
cat > /etc/yum.repos.d/perforce.repo <<EOF
[perforce]
name=Perforce
baseurl=http://package.perforce.com/yum/rhel/7/x86_64/
enabled=1
gpgcheck=1
EOF

echo "p4-cli: Install p4 yum repo signing key"
rpm --import http://package.perforce.com/perforce.pubkey

echo "p4-cli: Install p4"
yum -y install helix-cli
