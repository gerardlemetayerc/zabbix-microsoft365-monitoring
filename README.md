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
    * Supervision for Azure AD synchronization and licences
* *ServiceHealth.Read.All* (granted as application)
    * Supervision for service healths

### On Zabbix server (or Zabbix proxy)

* Validated with Zabbix version 6.4

## How to install

1. Create Azure AD application with correct permissions
2. Add template into Zabbix
3. Attach template to host wich you want to add items and triggers
4. On host, add following macro : tenantID, zabbixAppId, ZabbixAppSecret (wich obviously match tenantID, App Secret and App ID...)