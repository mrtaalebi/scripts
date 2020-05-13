apt update
sleep 1
apt install -y squid3


tee << EOF > /etc/squid/squid.conf

auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwords
auth_param basic realm proxy
acl authenticated proxy_auth REQUIRED
http_access allow authenticated

#acl all src 0.0.0.0/0
#http_access allow all

# Choose the port you want. Below we set it to default 3128.
http_port 0.0.0.0:$RANDOM

EOF

tee << EOF > /etc/squid/passwords
asghar:UF69MhJNpfQTE
EOF

systemctl restart squid

echo 'done successfully'
