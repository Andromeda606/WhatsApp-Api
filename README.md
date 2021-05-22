# WhatsApp-Api
WhatsApp Unofficial Api via Python Selenium

# Setup

```
python -m pip install -r requirements.txt
```

# How to use
Here is an example

```Python
import WhatsApp
a = WhatsApp("TEST", r"GECKODRIVER PATH")
print(a.login(showImg=False))
print(a.send_message("NUMBER", "THIS IS TEST MESSAGE"))
```

