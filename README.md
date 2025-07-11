# Zabbix - Microsoft 365 Monitoring

Repository for Zabbix Microsoft 365 Monitoring

Include the following monitoring capabilities:
* Licenses
* Service Health
* Azure AD Synchronization
* Registered Applications and Secrets
* Public Endpoints

## Pre-requisites

### Azure Permissions

You must create an Azure AD application with the following permissions:

### Delegated Permissions

| Permission           | Description                             |
|---------------------|-----------------------------------------|
| Directory.Read.All  | To read organization data.              |
| Reports.Read.All    | To access usage reports and health data.|
| User.Read.All       | To read user profiles.                  |

### Application Permissions

| Permission              | Description                                      |
|------------------------|--------------------------------------------------|
| Application.Read.All   | To read registered applications and their secrets.|
| Organization.Read.All  | To access organization-level data and license informations.|
| Directory.Read.All     | To access directory-level data.                   |
| ServiceHealth.Read.All | To access service status information data.       |

### On Zabbix server (or Zabbix proxy)

* Validated with Zabbix version 7.2.10 and above.
* Ensure the Zabbix server or proxy has internet access to query Microsoft Graph API endpoints.

## How to install

1. **Create Azure AD Application**
   - Register an application in Azure AD.
   - Assign the required permissions listed above.
   - Generate a client secret and note the Application (client) ID, Directory (tenant) ID, and client secret.
   - Ensure the Azure AD application has the following permissions for EntraID monitoring from the table above.
   - These permissions are required to monitor registered applications and detect secret expiration dates.

2. **Add Template to Zabbix**
   - Import the `template_microsoft_365_by_http.yaml` file from the appropriate version folder (e.g., `6.4.0` or `7.2.0`).

3. **Attach Template to Host**
   - Link the template to the host where you want to monitor Microsoft 365.

4. **Configure Host Macros**
   - Add the following macros to the host:
     - `{$TENANTID}`: Directory (tenant) ID of the Azure AD tenant.
     - `{$ZABBIXAPPID}`: Application (client) ID of the Azure AD app registration.
     - `{$ZABBIXAPPSECRET}`: Client secret of the Azure AD app registration.

6. **Verify Data Collection**
   - Ensure the Zabbix server or proxy can successfully query the Microsoft Graph API and collect data.
