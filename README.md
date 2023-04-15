# zabbix-microsoft365-monitoring

Repository for Zabbix Microsoft 365 Monitoring

Include following monitoring :
* Licences
* Service Health
* Azure AD Synchronization

## Pre-requisites

### Azure Permissions

You must create an Azure AD application with following permissions :
* Organization.Read.All (granted as application)
* ServiceHealth.Read.All (granted as application)

### On Zabbix server (or Zabbix proxy)

* Perl must be installed with requests module