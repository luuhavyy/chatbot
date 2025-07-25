Article URL: https://support.optisigns.com/hc/en-us/articles/4403616315539-how-to-approve-optisigns-as-enterprise-app-on-microsoft-azure-for-powerbi-calendar-etc-access

# How to approve OptiSigns as Enterprise App on Microsoft Azure (for PowerBI, Calendar, etc. access)

With OptiSigns, you can use PowerBI, Microsoft Outlook Calendar, OneDrive app
to integrate your Dashboard, calendar or content from your OneDrive on to your
digital signage screens.

In this article we will cover:

1) OptiSigns User/Admin: How to send request approval for OptiSigns to access
your PowerBI, Calendar, etc.

2) Microsoft Azure Admin: How to approve the request.

Let's dive in.

#### **1) OptiSigns User/Admin: How to send request approval for OptiSigns to
access your PowerBI, Calendar, etc.**

If you are using a work account from your organization, sometimes, your
organization's Admin have set security workflow so that apps like OptiSigns
will need to be reviewed by your Microsoft Azure Admin before granting access
to your organization resources (like PowerBI, Calendar, OneDrive).

In OptiSigns, when click Log In with Microsoft account, it will prompt a
window like below.

If you click "Request approval", this will send an email to your Microsoft
Azure Admin to review and approve.

Please enter something meaningful so that they know who you are and what you
want to use OptiSigns for. For example:

_"We are looking to use OptiSigns Digital Signage to display PowerBI KPI
Dashboard on big screens TVs in breakroom & common areas. As Digital Signage
use case, OptiSigns only read, display assets, OptiSigns will not modify,
move, delete objects."_

Then click "Request Approval"

Your admin will be notified by Microsoft Azure automatically, but it's usually
a good idea to send them an email as well. **You can send your Admin a link to
this article and refer to section #2 below for how to review & approve.**

If some times have past, and the Request Approval Expires (by default it's 30
days, but it could be different based on your organization's settings)

You can repeat this whole process again to send a new request.

#### **2) Microsoft Azure Admin: How to approve the request.**

As Microsoft Azure Admin, you will receive an email when a user request a 3rd
party app like OptiSigns to access your organization resources.

You can click "Review request" to review.

Or you can log in to Azure portal -> "Azure Active Directory" -> "Enterprise
applications" -> "Admin consent requests".

You will see pending approval request there.

Click "Review permission & consent"

Review the permissions requested by OptiSigns. OptiSigns, as a digital signage
application, only reads and displays assets. It will not modify, move, or
delete objects. See our [Privacy Policy](https://www.optisigns.com/privacy-
policy) for more information.

Click **Accept:**

**That's all!** You have reviewed and approve OptiSigns to be used as
Enterprise App in your organization.

You can notify your users who made the request that they can start using the
requested app (Power BI, OneDrive, or Calendar) with OptiSigns now.

If users want to use more than 1 app (i.e. Power BI and OneDrive, then you
will need to approve more than 1 time).

### Why does using Office 365, PowerBI, or other Microsoft App require giving
OptiSigns Admin permission to use?

OptiSigns uses Microsoft APIs for integration. In order for our integrations
to work, the integration has to be approved by an administrator to be allowed
in the Azure tenant. This is the same across all integrations using Microsoft
APIs.

This administrator access is only needed for first time access. Once the
OptiSigns app is approved for use in the Azure tenant, other users can use
OptiSigns directly.

**References:**

[Configure the admin consent workflow - Azure Active Directory | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/configure-admin-consent-workflow)

[Quickstart: Configure properties for an application in your Azure Active Directory (Azure AD) tenant | Microsoft Docs](https://docs.microsoft.com/en-us/azure/active-directory/manage-apps/add-application-portal-configure)

If you have any additional questions, concerns or any feedback about
OptiSigns, feel free to reach out to our support team at
[support@optisigns.com](mailto:support@optisigns.com)

