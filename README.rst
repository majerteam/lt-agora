========
LT Agora
========
:Info: See `github <http://github.com/LateralThoughts/lt-agora>`_ for the latest source.
:Author: Olivier Girardot <o.girardot@lateral-thoughts.com>

Goals
-----
The goal of the projet is to provide an online democratic plateform to take decision altogether and keep traces of the whereabouts of these decisions.

With Agora, you can :

* Create new proposals for the community to vote;
* Vote **+1**, **0**, or **-1** on any proposal;
* Connect with your google apps account, restricting users by domain ex: **@lateral-thoughts.com**
* Comment on any proposal and be notified by mail;
* Closes automatically any proposal where everyone voted **+1** or **0**;
* RESTFull open APIs to handle users, decisions and votes;
* Upload documents to decisions and make them available for download.

Setting up
----------
You need to have Python 2.7+ installed, and virtualenv, 

* Clone project;
* Create a new virtualenv;
* execute **pip install -r requirements.txt** to fetch dependencies;
* Test database is already bundled, so then all you need is to execute **./manage.py runserver** to run local dev server;

A few env variables are needed to configure the projet properly :

* AGORA_GOOGLE_CLIENT_ID : google api console client id for app
* AGORA_GOOGLE_CLIENT_SECRET : google secret api key for app
* AGORA_EMAIL_HOST : for the server to use for smtp
* AGORA_EMAIL_HOST_USER
* AGORA_EMAIL_HOST_PASSWORD
* AGORA_EMAIL_PORT
* AGORA_EMAIL_USE_TLS ("True" or "False")

License
-------
Project is licensed under AGPL.

Contact
-------
You can contact us at : contact (at) lateral-thoughts.com if you need any help.
