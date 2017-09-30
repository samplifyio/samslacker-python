# Install
`pip install samslacker-python`

# Configurate
```
import samslacker
samslacker.token = "private token"
samslacker.project = "projectid"
```

# Fire event with parameters
`samslacker.event("Account Created", { "email": "hello@world.com" })`
