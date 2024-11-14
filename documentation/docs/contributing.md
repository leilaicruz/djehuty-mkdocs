# Contributing

This chapter outlines how to set up an instance of d͡jehuty with the goal
of modifying its source code. Or in other words: this is the developer
setup.

## Setting up a development environment

First, we need to obtain the latest version of the source code:

``` bash
$ git clone https://github.com/4TUResearchData/djehuty.git
```

Next, we need to create a somewhat isolated Python environment:

``` bash
$ python -m venv djehuty-env
$ . djehuty-env/bin/activate
[env]$ cd djehuty
[env]$ pip install -r requirements.txt
```

And finally, we can install d͡jehuty in the virtual environment to make
the d͡jehuty command available:

``` bash
[env]$ sed -e 's/@VERSION@/0.0.1/g' pyproject.toml.in > pyproject.toml
[env]$ pip install --editable .
```

If all went well, we will now be able to run d͡jehuty:

``` bash
[env]$ djehuty --help
```

## Configuring d͡jehuty

Invoking d͡jehuty web starts the web interface of d͡jehuty. On what port
it makes itself available can be configured in its configuration file.
An example of a configuration file can be found in . We will use the
example configuration as the basis to configure it for the development
environment.

``` bash
[env]$ cp etc/djehuty/djehuty-example-config.xml config.xml
```

In the remainder of the chapter we will assume a value of 1͡27.0.0.1 for
b͡ind-address and a value of 8͡080 for p͡ort.

### Modifications to the example configuration for developers

The chapter describes each configuration option for d͡jehuty. The
remainder of sections here contain a fast-path through configuring
d͡jehuty for use in a development setup.

#### Live reload

The d͡jehuty program can be configured to automatically reload itself
when a change is detected by setting l͡ive-reload to 1͡.

#### Configuring authentication with ORCID

The d͡jehuty program does not have Identity Provider (IdP) capabilities,
so in order to log into the system we must configure an external IdP.
With an [ORCID](https://orcid.org) account comes the ability to set up
an OAuth endpoint. Go to
[developer-tools](https://orcid.org/developer-tools) at
[orcid.org](https://orcid.org). When setting up the OAuth at ORCID,
choose h͡ttp://127.0.0.1:8080/login as redirect URI.

Modify the following bits to reflect the settings obtained from ORCID.

``` xml
<authentication>
    <orcid>
      <client-id>APP-XXXXXXXXXXXXXXXX</client-id>
      <client-secret>XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX</client-secret>
      <endpoint>https://orcid.org/oauth</endpoint>
    </orcid>
  </authentication>
```

To limit who can log into a development system, accounts are not
automatically created for ORCID as IdP. So we need to configure who can
log in by creating a record in the p͡rivileges section of the
configuration file.

This is also a good moment to configure additional privileges for your
account. In the following snippet, configure the ORCID with which you
will log into the system in the o͡rcid argument.

``` xml
<privileges>
    <account email="you@example.com" orcid="0000-0000-0000-0001">
      <may-administer>1</may-administer>
      <may-impersonate>1</may-impersonate>
      <may-review>1</may-review>
    </account>
  </privileges>
```

### Invoking d͡jehuty

Once we’ve configured d͡jehuty for development use, we can start the web
interface by running:

``` bash
[env]$ djehuty web --initialize --config-file=config.xml
```

The -͡-initialize option creates the internal account record and
associates the specified ORCID with it. We only need to run d͡jehuty with
the -͡-initialize option once.

By now, we should be able to visit d͡jehuty through a web browser at
[localhost:8080](http://127.0.0.1:8080), unless configured differently.
We should be able to log in through ORCID, and access all features of
d͡jehuty.

## Navigating the source code

In this section, we trace the path from invoking d͡jehuty to responding
to a HTTP request.

### Starting point

Because d͡jehuty is installable as a Python package, we can find the
starting point for running d͡jehuty in p͡yproject.toml. It reads:

    [project.scripts]
    djehuty = djehuty.ui:main

So, we start our tour at in the procedure called m͡ain.

### How d͡jehuty initializes

The m͡ain procedure calls m͡ain_inner, which handles the command-line
arguments. When invoking d͡jehuty, we usually invoke d͡jehuty **web**,
which is handled by the following snippet:

``` python
import djehuty.web.ui as web_ui
...
if args.command == "web":
    web_ui.main (args.config_file, True, args.initialize,
                 args.extract_transactions_from_log,
                 args.apply_transactions)
```

So, the entry-point for the w͡eb subcommand is found in
s͡rc/djehuty/web/ui.py at the m͡ain procedure.

This procedure essentially sets up an instance of A͡piServer (found in
s͡rc/djehuty/web/wsgi.py and uses w͡erkzeug’s r͡un_simple to start the web
server.

### Translating URI paths to internal procedures

An instance of the A͡piServer is passed along in werkzeug’s r͡un_simple
procedure. Werkzeug calls the instance directly, which is handled by the
\_͡\_call\_\_ procedure of the A͡piServer class. The \_͡\_call\_\_
procedure invokes its w͡sgi instance, which is configured as following:

``` python
self.wsgi = SharedDataMiddleware(self.__respond, self.static_roots)
```

The \_͡\_respond procedure calls \_͡\_dispatch_request

In \_͡\_dispatch_request, the requested URI is translated into the
procedure name using the u͡rl_map. So, except for static resources in the
s͡rc/djehuty/web/resources folder and pre-configured static pages, URIs
are handled by a procedure in the A͡piServer instance.

A mapping between a URI and the procedure that is executed to handle the
request to that URI can be found in the u͡rl_map defined in the A͡piServer
class in .

### Diving into the code that displays the homepage

As an example, in the u͡rl_map, we can find the following line:

``` python
R("/", self.ui_home),
```

In this case, s͡elf is a reference to an instance of the A͡piServer class,
so we look for a procedure called u͡i_home inside the A͡piServer class.
Some code editors have a feature to “go to definition” which helps
navigating.

The u͡i_home gathers the summary numbers from the SPARQL endpoint with
the following line:

``` python
summary_data = self.db.repository_statistics()
```

And a list of the latest datasets with the following line:

``` python
records = self.db.latest_datasets_portal(30)
```

It then passes that information to the \_͡\_render_template procedure
which renders the in the folder. The Jinja [^1] package is used to
interpret the template.

``` python
return self.__render_template (request, "portal.html",
                               summary_data = summary_data,
                               latest = records, ...)
```

### Database communication

In the u͡i_home procedure, we found a call to the
s͡elf.db.repository_statistics procedure. To find out by hand where that
procedure can be found, we can look for the place where s͡elf.db is
assigned a value:

``` python
self.db = database.SparqlInterface()
```

And from there look up where d͡atabase comes from:

``` python
from djehuty.web import database
```

From which we can conclude that it can be found in .

In the r͡epository_statistics procedure, we find a call to
s͡elf.\_\_query_from_template followed by a call to \_͡\_run_query which
takes the output of the former procedure as its input.

As the name implies, \_͡\_run_query sends the query to the SPARQL
endpoint and retrieves the results by putting them in a list of Python
dictionaries.

The s͡elf.\_\_query_from_template procedure takes one parameter, which is
the name of the template file (minus the extension) that contains a
SPARQL query. These templates can be found in the folder.

[^1]:
