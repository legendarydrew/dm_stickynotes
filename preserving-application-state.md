> "Managing state... is the process of retaining user or application-related data over the duration of a number of
> requests.
>
> "HTTP is a stateless protocol. Being stateless, there is no requirement placed on HTTP (Web) Servers to retain
> information
> about each request or user. By default, multiple requests from the same user are treated as a series of independent and
> isolated
> transactions. In fact, the server has no concept of a "user" as such."
>
> https://www.learnrazorpages.com/razor-pages/state-management

To maintain state between multiple requests and responses, a server will typically create a session, identified by a session ID. The session ID is passed to the client's (user's) browser, which would then be sent back to the server with future requests.

A similar approach is used when managing logged-in users: upon authentication, a hashed token will be generated that will identify which user is represented by the browser.

Both the session and token are preserved (kept "alive") by the server for a set amount of time or until destroyed, after which they will have to be recreated.

Session IDs and tokens can be passed to the client through different methods:

- *Cookies*: these are sent by the server and stored by the browser;
- *URL parameters*: the server adds the session ID/token to the URL as a parameter;
- *Headers*: the server provides a session ID/token through a response's header parameters;
- *Hidden form fields:* HTML returned from the server includes a hidden form field for the session ID/token.

The browser should pass the session ID or token back to the server using one of these methods:

- *Request headers*: the browser adds a cookie, session ID or token to the request's header;
- *URL parameter*: the browser adds the session ID or token to the request's URL as a parameter;
- *Form field*: the session ID/token is sent to the server through a POST request, as part of a form.flake8