# Microsoft 365 Monitoring by HTTP

# Item list

| Item name | Key | Type | Description |
| -------------- | ----------- | ----------- |  ----------- |
| Microsoft365 - Organization data | azureAD.organization.data | Script | Use **https://graph.microsoft.com/v1.0/organization** API to temporarily store data used by dependent items and/or discovery |
| Microsoft365 - Json Health data | microsoft365.health.data | Script | Use **https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews** API to temporarily store data about service health used by dependent items or discovery |
| Microsoft365 - Json Licence Data | microsoft365.licence.data | Script | Use **https://graph.microsoft.com/v1.0/subscribedskus** API to temporarily store data about license consumption |
| Microsoft365 - Public Endpoints Data | microsoft365.publicendpoints.data | HTTP Agent | Use **https://endpoints.office.com/endpoints/worldwide** public API to get changes on Microsoft365 public endpoints |
| Microsoft365 - Json Applications data | entraID.application.data | Script | Use **https://graph.microsoft.com/v1.0/applications** API to temporarily store data about registered applications |

# Discovery list

| Discovery name | Key         | Description        |
| -------------- | ----------- | ----------- |
| Microsoft 365 - Check Health - Discovery  |  microsoft365.checkHealth.discovery  | Make a discovery based on **microsoft365.health.data** master item  |
| Microsoft 365 - Check Licence - Discovery |  microsoft365.checkLicence.discovery | Make a discovery based on **microsoft365.licence.data** master item |
| Microsoft365 - Public Endpoints - Discovery - TCP - Required - Allow | microsoft365.publicendpoints.discovery.tcp.required.allow | Make a discovery on **microsoft365.publicendpoints.data** and look for network flow of the following type: **TCP, Allowed and Required**. Allow endpoints are required for connectivity to specific Office 365 services and features, but are not as sensitive to network performance and latency as those in the Optimize category. |
| Microsoft365 - Public Endpoints - Discovery - TCP - Optimize - Allow | microsoft365.publicendpoints.discovery.tcp.required.optimize | Make a discovery on **microsoft365.publicendpoints.data** and look for network flow of the following type: **TCP, Optimize and Required**. Optimize endpoints are required for connectivity to every Office 365 service and represent over 75% of Office 365 bandwidth, connections, and volume of data. |
| Microsoft Entra - Application Discovery | entraID.application.discovery | Make a discovery on **entraID.application.data** to identify registered applications and their secrets, including expiration dates. |

# Required Microsoft 365 Permissions

To use this template, the following Microsoft 365 API permissions must be granted to the application registered in Azure AD:

## Delegated Permissions
- **Directory.Read.All**: To read organization data.
- **Reports.Read.All**: To access usage reports and health data.
- **User.Read.All**: To read user profiles.

## Application Permissions
- **Organization.Read.All**: To access organization-level data.
- **ServiceHealth.Read.All**: To read service health and announcements.
- **License.Read.All**: To access license information.
- **Application.Read.All**: To read registered applications and their secrets.

# Configuration Parameters

The following parameters must be configured in the Zabbix template:

| Parameter Name | Description |
| -------------- | ----------- |
| `{$ZABBIXAPPID}` | The Application (client) ID of the Azure AD app registration. |
| `{$ZABBIXAPPSECRET}` | The client secret of the Azure AD app registration. |
| `{$TENANTID}` | The Directory (tenant) ID of the Azure AD tenant. |

Ensure these values are securely stored and updated in the Zabbix template macros.


