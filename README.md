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
# client that uses our app
$ curl '127.0.0.1:5000?username=natalia&company=acme'
$ curl '127.0.0.1:5000?username=natalia&company=acme&local_time='$(date --rfc-3339=seconds | sed 's/ /T/')

# admin
$ curl '127.0.0.1:5000/admin?company=acme'
```

You can validate the policy at: https://play.openpolicyagent.org/

## NOtes


```
package acme

plan_features := [
    "a", "b", "c", "d"
]

group_power = features  {
    features := [
        "a", "c"
    ]
   input.session.teams[_] == "admin"    
}


group_hr = features  {
    features := [
        "a", "b"
    ]
   input.session.teams[_] == "hr"    
}

group_reviewer = features  {
    features := [
        "d"
    ]
   input.session.teams[_] == "reviewer"    
}
```

## Reference:

- https://www.martinfowler.com/articles/feature-toggles.html
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication
- https://docs.djangoproject.com/en/3.0/topics/auth/
- https://github.com/rocket-internet-berlin/RocketBucket
- https://livebook.manning.com/book/microservices-security-in-action/g-open-policy-agent/v-7/22
- https://www.openpolicyagent.org/docs/latest/external-data/
- https://kubernetes.io/docs/reference/access-authn-authz/rbac/
