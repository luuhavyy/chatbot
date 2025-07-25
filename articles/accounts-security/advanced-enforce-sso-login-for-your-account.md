Article URL: https://support.optisigns.com/hc/en-us/articles/360061576673-advanced-enforce-sso-login-for-your-account

# Advanced: Enforce SSO login for your account

### In this article, we'll explain how to enforce SSO logins for your
OptiSigns account.

  * Setting Up Basic SSO Enforcement (Microsoft, Facebook, Google)
  * Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google Workspace)

By default, OptiSigns allows the use of Google, Facebook, or Microsoft
accounts to access the OptiSigns portal:

However, some organizations have requirements to enforce SSO login for two-
factor authentication and password protection purposes. OptiSigns supports
this through Microsoft Entra ID and Google GSuite, as well as various SAML
options requiring custom branding.

* * *

## Setting Up Basic SSO Enforcement

To set up basic SSO enforcement, go to the **Preferences** page in your
OptiSigns portal:

You'll find the **Enforce Account SSO** option under the "General" section,
right at the top of the page.

Clicking on this will display several drop down options:

Selecting either option will require any users logging on to OptiSigns to do
so with their Google or Microsoft account. If a user tries to log in in any
other way, they'll receive this error:

For more information, see our guide on **[User
Management](https://support.optisigns.com/hc/en-
us/articles/360046356113-Advanced-Security-Managing-User-
Roles#AddingorInviting)**.

**Notes:** You will have to use the official <https://app.optisigns.com/> to
log in to enforce SSO. You cannot use a custom domain with Enforce SSO, as the
custom domain URL does not have an SSO login.

* * *

## Setting Up SAML SSO Enforcement (MS Entra ID, Okta, OneLogin, Google
Workspace)

**NOTE:** This feature is available to **Pro Plus** , **Engage** , and
**Enterprise** plan users.  
---  
  
Setting up SAML SSO enforcement requires setting up a subdomain, then
configuring your settings on your client of choice.

We have numerous articles covering this process, as well as general best
practices:

  * [**SAML Integration Strategy and Best Practices**](https://support.optisigns.com/hc/en-us/articles/4407128433299-SAML-integration-strategy-best-practice)
  * [**Microsoft Entra ID SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4407252213395-How-to-Set-Up-SAML-2-0-with-OptiSigns-and-MS-Entra-ID-formerly-Azure-AD)
  * [**Okta SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4404590815635-How-to-set-up-SAML-2-0-with-OptiSigns-and-Okta)
  * [**OneLogin SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4407386819731-How-to-set-up-SAML-2-0-with-OptiSigns-and-OneLogin)
  * [**Google Workspace SAML 2.0 SSO Setup**](https://support.optisigns.com/hc/en-us/articles/4407493404307-How-to-set-up-SAML-2-0-with-OptiSigns-and-Google-Workspace)

Please follow one of these guides to set up SSO via SAML.

### **That's all!**

OptiSigns is the leader in [digital signage
software](https://www.optisigns.com/). If you have any additional questions or
any feedback about OptiSigns, feel free to reach out to our support team at
[support@optisigns.com](mailto:support@optisigns.com).

