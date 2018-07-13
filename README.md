### Pretext
#### (c) Vinsent_ru 2018

Pretxt is a small tool to render a Jinja2 template with values, provided in the YAML config file.
Think of it as a modern variant of an m4 tool.

I've created it because I needed something to conditionally render some long text based on some variables.
For example, I'd like to add 18+ content in the resulting text, but only if an is18plus variable is set to 'true'.

That way I can write my text once, and then easily render it to several different versions based on some conditions. Basically, it's possible to use any Jinja2 features like loops or conditional formatting.

You can try it like this:

```
python3 src/pretxt.py -c config.yaml test.tmpl
```

The rendered file goes to STDOUT, debug messages goes to STDERR

TODO:
- better error handling
