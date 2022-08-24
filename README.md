# mailto

A Python library to encode mailto-URLs in HTML 

This library can help you if you're using Django
for creating webapps and wanting to add a mailto-URL.

This project is still on run, please run at your own risk.

# how to use

clone this repository:

```
git clone https://github.com/Fukuro192/mailto.git
```

then on python import and use the principal function:

```python
>>> import mailto
>>> mailto.mailto_href("name1@example.com", cc="name2@example.com")
'mailto:name1@example.com?cc=name2@example.com'
```

you can use `mailto_href` directly to set the `href`-attribute like so:

```html
<a href="{{your_mailto_result_here}}">Send a Mail</a>
```