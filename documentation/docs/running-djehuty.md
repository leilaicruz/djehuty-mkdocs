# Configuring 

Now that is installed, it’s a good moment to look into its run-time
configuration options. All configuration can be done through a
configuration file, for which an example is available at .

## Essential options

|                            |                                                                                                                                                                                                                                                         |
|:---------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Option**                 | **Description**                                                                                                                                                                                                                                         |
| b͡ind-address               | The address to bind a TCP socket on.                                                                                                                                                                                                                    |
| p͡ort                       | The port to bind a TCK socket on.                                                                                                                                                                                                                       |
| b͡ase-url                   | The URL on which the instance will be available to the outside world.                                                                                                                                                                                   |
| a͡llow-crawlers             | Set to 1 to allow crawlers in the r͡obots.txt, otherwise set to 0.                                                                                                                                                                                       |
| p͡roduction                 | Performs extra checks before starting. Enable this when running a production instance.                                                                                                                                                                  |
| l͡ive-reload                | When set to 1, it reloads Python code on-the-fly. We recommend to set it to 0 when running in production.                                                                                                                                               |
| d͡ebug-mode                 | When set to 1, it will display backtraces and error messages in the web browser. When set to 0, it will only show backtraces and error messages in the web browser.                                                                                     |
| u͡se-x-forwarded-for        | When running d͡jehuty behind a reverse-proxy server, use the HTTP header X͡-Forwarded-For to log IP address information.                                                                                                                                  |
| d͡isable-collaboration      | When set to 1, it disables the “collaborators” feature.                                                                                                                                                                                                 |
| a͡llowed-depositing-domains | When unset, any authenticated user may deposit data. Otherwise, this option limits the ability to deposit to users with an e-mail address of the listed domain names.                                                                                   |
| c͡ache-root                 | d͡jehuty can cache query responses to lower the load on the database server. Specify the directory where to store cache files. This element takes an attribute c͡lear-on-start, and when set to 1, it will remove all cache files on start-up of d͡jehuty. |
| p͡rofile-images-root        | Users can upload a profile image in d͡jehuty. This option should point to a filesystem directory where these profile images can be stored.                                                                                                               |
| d͡isable-2fa                | Accounts with privileges receive a code by e-mail as a second factor when logging in. Setting this option to 1 disables the second factor authentication.                                                                                               |
| s͡andbox-message            | Display a message on the top of every page.                                                                                                                                                                                                             |
| n͡otice-message             | Display a message on the main page.                                                                                                                                                                                                                     |
| m͡aintenance-mode           | When set to 1, all HTTP requests result in the displayment of a maintenance message. Use this option while backing up the database, or when performing major updates.                                                                                   |

## Configuring the Database

The d͡jehuty program stores its state in a SPARQL 1.1 compliant RDF
store. Configuring the connection details is done in the r͡df-store node.

|                   |                                                                                                                                                                                                                                         |
|:------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Option**        | **Description**                                                                                                                                                                                                                         |
| s͡tate-graph       | The graph name to store triplets in.                                                                                                                                                                                                    |
| s͡parql-uri        | The URI at which the SPARQL 1.1 endpoint can be reached. When the s͡parql-uri begins with b͡db://, followed by a path to a filesystem directory, it will use the BerkeleyDB back-end, for which the Python package needs to be installed. |
| s͡parql-update-uri | The URI at which the SPARQL 1.1 Update endpoint can be reached (in case it is different from the s͡parql-uri.                                                                                                                            |

## Audit trails and database reconstruction

The d͡jehuty program can keep an audit log of all database modifications
made by itself from which a database state can be reconstructed. Whether
d͡jehuty keeps such an audit log can be configured with the following
option:

|                        |                                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Option**             | **Description**                                                                                                                                                                                                                                                                                                                                                                     |
| e͡nable-query-audit-log | When set to 1, it writes every SPARQL query that modifies the database in the web logs. This can be replayed to reconstruct the database at a later time. Setting this option to 0 disables this feature. This element takes an attribute t͡ransactions-directory that should specify an empty directory to which transactions can be written that are extracted from the audit log. |

### Reconstructing the database from the query audit log

Each query that modifies the database state while the query audit logs
are enabled can be extracted from the query audit log using the
-͡-extract-transactions-from-log command-line option. A timestamp to
specify the starting point to extract from can be specified as an
argument. The following example displays its use:

``` bash
djehuty web --config-file=config.xml --extract-transactions-from-log="YYYY-MM-DD HH:MM:SS"
```

This will create a file for each query in the folder specified in the
t͡ransactions-directory attribute.

To replay the extracted transactions, use the a͡pply-transactions
command-line option:

``` bash
djehuty web --config-file=config.xml --apply-transactions
```

When a query cannot be executed, the command stops, allowing to fix or
remove the query to-be-replayed. Invoking the -͡-apply-transactions
command a second time will continue replaying where the previous run
stopped.

## Configuring storage

Storage locations can be configured with the s͡torage node. When
configuring multiple locations, d͡jehuty attempts to find a file by
looking at the first configured location, and in case it cannot find the
file there, it will look at the second configured location, and so on,
until it has tried each storage location.

This allows for moving files between storage systems transparently
without requiring specific interactions with d͡jehuty other than having
the files made available as a POSIX filesystem.

One use-case that suits this mechanism is letting uploads write to fast
online storage and later move the uploaded files to a slower but less
costly storage.

|            |                                                                             |
|:-----------|:----------------------------------------------------------------------------|
| **Option** | **Description**                                                             |
| l͡ocation   | A filesystem path to where files are stored. This is a repeatable property. |

## Configuring an identity provider

Ideally, d͡jehuty makes use of an external identity provider. d͡jehuty can
use SAML2.0, ORCID, or an internal identity provider (for testing and
development purposes only).

This section will outline the configuration options for each identity
provision mechanism.

### SAML2.0

For SAML 2.0, the configuration can be placed in the s͡aml section under
a͡uthentication. That looks as following:

``` xml
<authentication>
  <saml version="2.0">
    <!-- Configuration goes here. -->
  </saml>
</authentication>
```

The options outlined in the remainder of this section should be placed
where the example shows .

|                   |                                                                                                                                             |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| **Option**        | **Description**                                                                                                                             |
| s͡trict            | When set to 1, SAML responses must be signed. **Never disable ‘strict’ mode in a production environment.**                                  |
| d͡ebug             | Increases logging verbosity for SAML-related messages.                                                                                      |
| a͡ttributes        | In this section the attributes provided by the identity provider can be aligned to the attributes d͡jehuty expects.                          |
| s͡ervice-provider  | The d͡jehuty program fulfills the role of service provider. In this section the certificate and service provider metadata can be configured. |
| i͡dentity-provider | In this section the certificate and single-sign-on URL of the identity provider can be configured.                                          |
| s͡ram              | In this section, SURF Research Access Management-specific attributes can be configured.                                                     |

#### The a͡ttributes configuration

To create account and author records and to authenticate a user, d͡jehuty
stores information provided by the identity provider. Each identity
provider may provide this information using different attributes.
Therefore, the translation from attributes used by d͡jehuty and
attributes given by the identity provider can be configured. The
following attributes must be configured.

|              |                                       |
|:-------------|:--------------------------------------|
| **Option**   | **Description**                       |
| f͡irst-name   | A user’s first name.                  |
| l͡ast-name    | A user’s last name.                   |
| c͡ommon-name  | A user’s full name.                   |
| e͡mail        | A user’s e-mail address.              |
| g͡roups       | The attribute denoting groups.        |
| g͡roup-prefix | The prefix for each group short name. |

As an example, the attributes configuration for SURFConext looks like
this:

``` xml
<attributes>
  <first-name>urn:mace:dir:attribute-def:givenName</first-name>
  <last-name>urn:mace:dir:attribute-def:sn</last-name>
  <common-name>urn:mace:dir:attribute-def:cn</common-name>
  <email>urn:mace:dir:attribute-def:mail</email>
</attributes>
```

And for SURF Research Access Management (SRAM), the attributes
configuration looks like this:

``` xml
<attributes>
  <first-name>urn:oid:2.5.4.42</first-name>
  <last-name>urn:oid:2.5.4.4</last-name>
  <common-name>urn:oid:2.5.4.3</common-name>
  <email>urn:oid:0.9.2342.19200300.100.1.3</email>
  <groups>urn:oid:1.3.6.1.4.1.5923.1.1.1.7</groups>
  <group-prefix>urn:mace:surf.nl:sram:group:[organisation]:[service]</group-prefix>
</attributes>
```

#### The s͡ram configuration

When using SURF Research Access Management (SRAM), d͡jehuty can persuade
SRAM to send an invitation to anyone inside or outside the institution
to join the SRAM collaboration that provides access to the d͡jehuty
instance. To do so, the following attributes must be configured.

|                        |                                                   |
|:-----------------------|:--------------------------------------------------|
| **Option**             | **Description**                                   |
| o͡rganization-api-token | An organization-level API token.                  |
| c͡ollaboration-id       | The UUID of the collaboration to invite users to. |

#### The s͡ervice-provider configuration

|                  |                                                                                                                                                        |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Option**       | **Description**                                                                                                                                        |
| x͡509-certificate | Contents of the public certificate without whitespacing.                                                                                               |
| p͡rivate-key      | Contents of the private key belonging to the x͡509-certificate to sign messages with.                                                                   |
| m͡etadata         | This section contains metadata that may be displayed by the identity provider to users before authorizing them.                                        |
| d͡isplay-name     | The name to be displayed by the identity provider when authorizing the user to the service.                                                            |
| u͡rl              | The URL to the service.                                                                                                                                |
| d͡escription      | Textual description of the service.                                                                                                                    |
| o͡rganization     | This section contains metadata to describe the organization behind the service.                                                                        |
| n͡ame             | The name of the service provider’s organization.                                                                                                       |
| u͡rl              | The URL to the web page of the organization.                                                                                                           |
| c͡ontact          | A repeatable section to list contact persons and their roles within the organization. The role can be configured by setting the t͡ype attribute.        |
| f͡irst-name       | The first name of the contact person.                                                                                                                  |
| l͡ast-name        | The last name of the contact person.                                                                                                                   |
| e͡mail            | The e-mail address of the contact person. Note that some identity providers prefer functional e-mail addresses (e.g. support@... instead of jdoe@...). |

### ORCID

[ORCID.org](https://orcid.org) plays a key role in making researchers
findable. Its identity provider service can be used by d͡jehuty in two
ways:

1.  As primary identity provider to log in and deposit data;

2.  As additional identity provider to couple an author record to its
    ORCID record.

When another identity provider is configured in addition to ORCID, that
identity provider will be used as primary and ORCID will only be used to
couple author records to the author’s ORCID record.

To configure ORCID, the configuration can be placed in the o͡rcid section
under a͡uthentication. That looks as following:

``` xml
<authentication>
  <orcid>
    <!-- Configuration goes here. -->
  </orcid>
</authentication>
```

Then the following parameters can be configured:

|               |                                       |
|:--------------|:--------------------------------------|
| **Option**    | **Description**                       |
| c͡lient-id     | The client ID provided by ORCID.      |
| c͡lient-secret | The client secret provided by ORCID.  |
| e͡ndpoint      | The URL to the ORCID endpoint to use. |

## Configuring an e-mail server

On various occassions, d͡jehuty will attempt to send an e-mail to either
an author, a reviewer or an administrator. To be able to do so, an
e-mail server must be configured from which the instance may send
e-mails.

The configuration is done under the e͡mail node, and the following items
can be configured:

|                |                                                                                                                                                             |
|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Option**     | **Description**                                                                                                                                             |
| s͡erver         | Address of the e-mail server without protocol specification.                                                                                                |
| p͡ort           | The port the e-mail server operates on.                                                                                                                     |
| s͡tarttls       | When 1, d͡jehuty attempts to use StartTLS.                                                                                                                   |
| u͡sername       | The username to authenticate with to the e-mail server.                                                                                                     |
| p͡assword       | The password to authenticate with to the e-mail server.                                                                                                     |
| f͡rom           | The e-mail address used to send e-mail from.                                                                                                                |
| s͡ubject-prefix | Text to prefix in the subject of all e-mails sent from the instance of d͡jehuty. This can be used to distinguish a test instance from a production instance. |

## Configuring DOI registration

When publishing a dataset or collection, d͡jehuty can register a
persistent identifier with DataCite. To enable this feature, configure
it under the d͡atacite node. The following parameters can be configured:

|               |                                                |
|:--------------|:-----------------------------------------------|
| **Option**    | **Description**                                |
| a͡pi-url       | The URL of the API endpoint of DataCite.       |
| r͡epository-id | The repository identifier given by DataCite.   |
| p͡assword      | The password to authenticate with to DataCite. |
| p͡refix        | The DOI prefix to use when registering a DOI.  |

## Configuring Handle registration

Each uploaded file can be assigned a persistent identifier using the
Handle system. To enable this feature, configure it under the h͡andle
node. The following parameters can be configured:

|             |                                                                                   |
|:------------|:----------------------------------------------------------------------------------|
| **Option**  | **Description**                                                                   |
| u͡rl         | The URL of the API endpoint of the Handle system implementor.                     |
| c͡ertificate | Certificate to use for authenticating to the endpoint.                            |
| p͡rivate-key | The private key paired with the certificate used to authenticate to the endpoint. |
| p͡refix      | The Handle prefix to use when registering a handle.                               |
| i͡ndex       | The index to use when registering a handle.                                       |

## Configuring IIIF support

When publishing images, d͡jehuty can enable the IIIF Image API for the
images. It uses l͡ibvips and p͡yvips under the hood to perform image
manipulation. The following parameters can be configured:

|                 |                                                                                                                      |
|:----------------|:---------------------------------------------------------------------------------------------------------------------|
| **Option**      | **Description**                                                                                                      |
| e͡nable-iiif     | Enable support for the IIIF image API. This requires the p͡yvips package to be available in the run-time environment. |
| i͡iif-cache-root | The directory to store the output of IIIF Image API requests to avoid re-computing the image.                        |

## Customizing looks

With the following options, the instance can be branded as necessary.

|                         |                                                                                                                               |
|:------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| **Option**              | **Description**                                                                                                               |
| s͡ite-name               | Name for the instance used in the title of a browser window and as default value in the publisher field for new datasets.     |
| s͡ite-description        | Description used as a meta-tag in the HTML output.                                                                            |
| s͡ite-shorttag           | Used as keyword and as Git remote name.                                                                                       |
| s͡upport-email-address   | E-mail address used in e-mails sent to users in automated messages.                                                           |
| c͡ustom-logo-path        | Path to a PNG image file that will be used as logo on the website.                                                            |
| c͡ustom-favicon-path     | Path to an ICO file that will be used as favicon.                                                                             |
| s͡mall-footer            | HTML that will be used as footer for all pages except for the main page.                                                      |
| l͡arge-footer            | HTML that will be used as footer on the main page.                                                                            |
| s͡how-portal-summary     | When set to 1, it shows the repository summary of number of datasets, authors, collections, files and bytes on the main page. |
| s͡how-institutions       | When set to 1, it shows the list of institutions on the main page.                                                            |
| s͡how-science-categories | When set to 1, it shows the subjects (categories) on the main page.                                                           |
| s͡how-latest-datasets    | When set to 1, it shows the list of latest published datasets on the main page.                                               |
| c͡olors                  | Colors used in the HTML output. See section <a href="#sec:customize-colors" data-reference-type="ref"                         
                           data-reference="sec:customize-colors">1.10.1</a>.                                                                              |

### Customizing colors

The following options can be configured in the c͡olors section.

|                          |                                                         |
|:-------------------------|:--------------------------------------------------------|
| **Option**               | **Description**                                         |
| p͡rimary-color            | The main background color to use.                       |
| p͡rimary-foreground-color | The main foreground color to use.                       |
| p͡rimary-color-hover      | Color to use when hovering a link.                      |
| p͡rimary-color-active     | Color to use when a link is clicked.                    |
| p͡rivilege-button-color   | The background color of buttons for privileged actions. |
| f͡ooter-background-color  | Color to use in the footer.                             |

## Configuring privileged users

By default an authenticated user may deposit data. But users can have
additional roles; for example: a dataset reviewer, a technical
administrator or a quota reviewer.

Such additional roles are configured in terms of privileges. The
following privileges can be configured in the p͡rivileges section:

|                                 |                                                                                                                       |
|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| **Option**                      | **Description**                                                                                                       |
| m͡ay-administer                  | Allows access to perform maintenance tasks, view accounts and view reports on restricted and embargoed datasets.      |
| m͡ay-run-sparql-queries          | Allows to run arbitrary SPARQL queries on the database.                                                               |
| m͡ay-impersonate                 | Allows to log in to any account and therefore perform any action as that account.                                     |
| m͡ay-review                      | Allows to see which datasets are sent for review, and allows to perform reviews.                                      |
| m͡ay-review-quotas               | Allows access to see requests for storage quota increases and approve or decline them.                                |
| m͡ay-review-integrity            | Allows access to an API call that provides statistics on the accessibility of files on the filesystem.                |
| m͡ay-process-feedback            | Accounts with this privilege will receive e-mails with the information entered into the feedback form by other users. |
| m͡ay-receive-email-notifications | This “privilege” can be used to disable sending any e-mails to an account by setting it to 0͡. The default is 1͡.       |

To enable a privilege for an account, set the value of the desired
privilege to 1͡. Privileges are disabled by default, except for
m͡ay-receive-email-notifications which defaults to 1͡.

``` xml
<privileges>
    <account email="you@example.com" orcid="0000-0000-0000-0001">
      <may-administer>1</may-administer>
      <may-run-sparql-queries>1</may-run-sparql-queries>
      <may-impersonate>1</may-impersonate>
      <may-review>0</may-review>
      <may-review-quotas>0</may-review-quotas>
      <may-review-integrity>0</may-review-integrity>
      <may-process-feedback>0</may-process-feedback>
      <may-receive-email-notifications>1</may-receive-email-notifications>
    </account>
  </privileges>
```
