# Microsoft 365 Monitoring by HTTP

# Item list

| Item name | Key | Type | Description |
| -------------- | ----------- | ----------- |  ----------- |
| Microsoft365 - Organization data | azureAD.organization.data | Script | Use **https://graph.microsoft.com/v1.0/organization** API to temporary store data used by dependant items and/or discovery |
| Microsoft365 - Json Health data | microsoft365.health.data | Script | Use **https://graph.microsoft.com/v1.0/admin/serviceAnnouncement/healthOverviews** API to temporary store data about services health use by dependant item/or discovery |
| Microsoft365 - Json Licence Data | microsoft365.licence.data | Script | Use **https://graph.microsoft.com/v1.0/subscribedskus** API to temporary store data about licence consumption |
| Microsoft365 - Public Endpoints Data | microsoft365.publicendpoints.data | Script | Use **https://endpoints.office.com/endpoints/worldwide** public API to get change on Microsoft365 public endpoint |


# Discovery list

| Discovery name | key         | Description        |
| -------------- | ----------- | ----------- |
| Microsoft 365 - Check Health - Discovery  |  microsoft365.checkHealth.discovery  | Make a discovery based on **microsoft365.health.data** master item  |
| Microsoft 365 - Check Licence - Discovery |  microsoft365.checkLicence.discovery | Make a discovery based on **microsoft365.licence.data** master item |
| Microsoft365 - Public Endpoints - Discovery - TCP - Required - Allow | microsoft365.publicendpoints.discovery.tcp.required.allow | Make a discovery on **microsoft365.publicendpoints.data** and look for network flow of following type : **TCP, Allowed and Required**. Allow endpoints are required for connectivity to specific Office 365 services and features, but are not as sensitive to network performance and latency as those in the Optimize category. The overall network footprint of these endpoints from the standpoint of bandwidth and connection count is also smaller. These endpoints are dedicated to Office 365 and are hosted in Microsoft datacenters. They represent a broad set of Office 365 micro-services and their dependencies (on the order of ~100 URLs) and are expected to change at a higher rate than those in the Optimize category. Not all endpoints in this category are associated with defined dedicated IP subnets. | 
| Microsoft365 - Public Endpoints - Discovery - TCP - Optimize - Allow | microsoft365.publicendpoints.discovery.tcp.required.optimize |Make a discovery on **microsoft365.publicendpoints.data** and look for network flow of following type : **TCP, Optimize and Required**. ptimize endpoints are required for connectivity to every Office 365 service and represent over 75% of Office 365 bandwidth, connections, and volume of data. These endpoints represent Office 365 scenarios that are the most sensitive to network performance, latency, and availability. All endpoints are hosted in Microsoft datacenters. The rate of change to the endpoints in this category is expected to be much lower than for the endpoints in the other two categories. This category includes a small (on the order of ~10) set of key URLs and a defined set of IP subnets dedicated to core Office 365 workloads such as Exchange Online, SharePoint Online, Skype for Business Online, and Microsoft Teams. |


