---
description: Boilerplate generator for securing an endpoint or function.
---

Add authentication logic to the targeted code:
- Check for a valid JWT token in headers or environment configuration.
- Raise an unauthorized error (401) if authentication fails.
- Log the request user identity.