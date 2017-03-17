# Nagios_plugins

Put the chtest.py plugin on client machine along with other plugins in /nagios/libexec/
e.g: /usr/local/nagios/libexec/chtest.py

On client side replace nrpe.cfg with the sample nrpe.cfg
path: /nagios/etc/nrpe.cfg
e.g: /usr/local/nagios/etc/nrpe.cfg
Edits:
    add monitoring server's ip address in line which contains "allowed_hosts= "
    
on monitoring server edit the nagios.cfg
Edit:
    uncomment cfg_dir=/usr/local/nagios/etc/servers
    place the servers folder along with the client configuration in /nagios/etc/     (e.g: /usr/local/nagios/etc/servers/clients.cfg)
replace the commands.cfg with sample commands.cfg in usr/local/nagios/etc/objects/commands.cfg

 
