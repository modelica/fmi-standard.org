# FMI Website

Sources of the new fmi-standard.org website

## Tools list

The [tools page](https://fmi-standard.org/tools/) is generated from [_data/tools.csv](_data/tools.csv). To add, edit or remove a tool from the table update the respective line and push your changes.

## News

To create a post, add a file to the `_posts` directory with the following format:

```
YEAR-MONTH-DAY-title.MARKUP
```

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file.
For example, the following are examples of valid post filenames:

```
2018-05-22-fmi-forum-japan.md
2018-09-04-modelica-conference-2019.md
```

You typically write posts in [Markdown](https://daringfireball.net/projects/markdown/) (`.md`), however HTML (`.html`) is also supported.  
All blog post files must begin with a front matter that sets the title:

```markdown
---
title: FMI at the 13th Modelica Conference 2019
---

The [13th International Modelica Conference](https://modelica.org/events/modelica2019) will be held at [OTH Regensburg](https://www.oth-regensburg.de/en.html), Germany, March 4–6, 2019.

The scope of the conference includes FMI in Modelica and non-Modelica applications and tools.
```

To include images, downloads or other files along with a post place them in the `assets` directory and reference them using the following markdown syntax:

```markdown
... which is shown in the screenshot below:
![My helpful screenshot]("/assets/screenshot.jpg")
```

Linking to a PDF for readers to download:

```markdown
... you can [get the PDF]("/assets/mydoc.pdf") directly.
```

## Build the website locally

1. Install a full [Ruby development environment](https://www.ruby-lang.org/en/downloads/)

2. Install Jekyll and [bundler](https://jekyllrb.com/docs/ruby-101/#bundler) [gems](https://jekyllrb.com/docs/ruby-101/#gems)
   ```
   gem install jekyll bundler
   ```

3. [Download](https://github.com/modelica/fmi-standard.org/archive/master.zip) and extract the sources  
   *or*  
   clone the repository, change into the directory and pull the changes
   ```
   git clone https://github.com/modelica/fmi-standard.org.git
   cd fmi-website
   git pull
   ```

4. Build the site and make it available on a local server
   ```
   jekyll serve --livereload
   ```

5. Now browse to [http://localhost:4000](http://localhost:4000)
