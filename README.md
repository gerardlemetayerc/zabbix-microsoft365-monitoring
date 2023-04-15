# Zabbix - Microsoft 365 Monitoring

Repository for Zabbix Microsoft 365 Monitoring

Include following monitoring :
* Licences
* Service Health
* Azure AD Synchronization

## Pre-requisites

### Azure Permissions

You must create an Azure AD application with following permissions :
* *Organization.Read.All* (granted as application) 
** Supervision for Azure AD synchronzation and licences
* *ServiceHealth.Read.All* (granted as application)
** Supervision for service healths

### On Zabbix server (or Zabbix proxy)

* Perl must be installed with requests module
* Validated with Zabbix version 6.4

## How to install

1. Deploy script externalScript/checkMicrosoftGraph.py into Zabbix server external script repo
2. Create Azure AD application with correct permissions
3. Add template into Zabbix
4. Attach template to host wich you want to add items and triggers