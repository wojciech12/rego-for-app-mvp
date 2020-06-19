## A/B?


## Approch for defining product features ?

Brainstorming:
```
company - [plan] 
            | - feature1 - subfeat
            |           \- subfeat  
            |
            |- feature2 - subfeat
            \- feature3

company - [extras]
           |- featureX - subfeat
           \- feature3 - subfeatAlpha

groupA 
    |- feature1
    \- feature2

groupB 
    |- feature1
    \- feature2

groupX:
    \- featureX - subfeat

groupeAlpha:
    \- feature3 - subfeatAlpha

# to avoid:
userA - subfeatAlpha
```

What can we learn from https://kubernetes.io/docs/reference/access-authn-authz/rbac/?

## Testing

for testing:
```
curl '127.0.0.1:5000?username=natalia&company=acme'
curl '127.0.0.1:5000?username=natalia&company=acme&local_time='$(date --rfc-3339=seconds | sed 's/ /T/')
```

Reference:

- https://www.martinfowler.com/articles/feature-toggles.html
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
- https://docs.djangoproject.com/en/3.0/topics/auth/
- https://github.com/rocket-internet-berlin/RocketBucket
- https://livebook.manning.com/book/microservices-security-in-action/g-open-policy-agent/v-7/22
- https://www.openpolicyagent.org/docs/latest/external-data/
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/
