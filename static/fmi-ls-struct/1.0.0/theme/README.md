# Modelica Association Asciidoctor Theme

Common [Asciidoctor](https://asciidoctor.org/) theme for specifications by the [Modelica Association](https://modelica.org).

## Building the Specification Document

To build the specification document clone the repository recursively

```sh
git clone --recursive git://github.com/modelica/fmi-standard/
```

change into the directory

```sh
cd fmi-standard
```

and run asciidoctor

```sh
sudo docker run --rm -it -v $PWD:/documents/ asciidoctor/docker-asciidoctor asciidoctor --base-dir /documents/docs --failure-level WARN --verbose docs/index.adoc
```
