# Contributing to the fmi-standard.org website

Please take a moment to review this document in order to make the contribution process easy and effective for everyone involved.  
Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project.
In return, they should reciprocate that respect in addressing your issue or assessing patches and features.

## Feature requests

Feature requests are welcome. But take a moment to find out whether your idea fits with the scope and aims of the project.
It's up to *you* to make a strong case to convince the project's developers of the merits of this feature.
Please provide as much detail and context as possible.

## Pull requests

Good pull requests - patches, improvements, new features - are a fantastic help.
They should remain focused in scope and avoid containing unrelated commits.

If you only want to make small changes you can [edit files](https://help.github.com/articles/editing-files-in-your-repository/) and [open pull requests](https://help.github.com/articles/creating-a-pull-request) directly from your browser.
Please chose an expressive name for your branch like `add-my-news-post` (not ~~`patch-x`~~).

If you plan bigger changes you can [fork](https://guides.github.com/activities/forking/) and [clone](https://help.github.com/articles/cloning-a-repository/) the repository to your local machine.

*Please ask first* before embarking on any significant pull request (e.g. implementing features, refactoring code, porting to a different language),
otherwise you risk spending a lot of time working on something that the project's developers might not want to merge into the project.

## Commit messages

Please follow [the seven rules of a great Git commit message](https://chris.beams.io/posts/git-commit/) when committing your changes:

- Separate subject from body with a blank line
- Limit the subject line to 50 characters
- Capitalize the subject line
- Do not end the subject line with a period
- Use the imperative mood in the subject line
- Wrap the body at 72 characters
- Use the body to explain what and why vs. how

For example:

```
Summarize changes in around 50 characters or less

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of the commit and the rest of the text as the body. The
blank line separating the summary from the body is critical (unless
you omit the body entirely); various tools like `log`, `shortlog`
and `rebase` can get confused if you run the two together.

Explain the problem that this commit is solving. Focus on why you
are making this change as opposed to how (the code explains that).
Are there side effects or other unintuitive consequences of this
change? Here's the place to explain them.

Further paragraphs come after blank lines.

 - Bullet points are okay, too

 - Typically a hyphen or asterisk is used for the bullet, preceded
   by a single space, with blank lines in between, but conventions
   vary here

If the commit it related to an issue, put references to them at the
bottom, like this:

Resolves: #123
See also: #456, #789
```

## Updating the tools list

The [tools page](https://fmi-standard.org/tools/) is the central location to find and get information about tools that support FMI.
The page is generated from [tools.json](assets/tools.json).
To add, edit or remove a tool from the list, update the respective entry and make a [pull request](#pull-requests).
Please respect the rules below when editing the file.

### Format

| Column         | Description                                                             | Example / valid values
|----------------|-------------------------------------------------------------------------|-----------------------
| name           | The tool name that appears in the tools list                            | `"Example Sim"`
| license        | License (commercial or [OSI approved](https://opensource.org/licenses)) | `"commercial"`, `"osi"`
| url            | Link to the tool's homepage                                             | `"https://example.com/example-sim/"`
| logo           | filename of the tool's logo                                             | `"example-sim.svg"`
| vendor         | Name of the tool vendor                                                 | `"Example Company"`
| vendorUrl      | Link to the vendor's homepage                                           | `"https://example.com/"`
| description    | A [description](#tool-description) of the tool                          | `"Run simulations in the cloud in real time"`
| features       | Reserved for future use                                                 | `[]`
| platforms      | Supported platforms                                                     | `["macOS", "Linux", "Windows"]`
| interfaces     | Supported interfaces                                                    | `["GUI", "CLI", "library"]`
| fmiVersions    | Supported FMI versions                                                  | `["1.0", "2.0", "3.0"]`
| fmuExport      | Supported interface types for FMU export                                | `["CS", "ME", "SE"]`
| fmuImport      | Supported interface types for FMU import                                | `["CS", "ME", "SE"]`

Example:

```json
{
    "name": "Example Sim",
    "license": "commercial",
    "url": "https://example.com/example-sim/",
    "logo": "example-sim.svg",
    "vendor": "Example Company",
    "vendorURL": ""https://example.com/",
    "description": "Run simulations in the cloud in real time",
    "features": [],
    "platforms": [
        "macOS",
        "Linux",
        "Windows"
    ],
    "interfaces": [
        "GUI",
        "CLI"
    ],
    "fmiVersions": [
        "2.0",
        "3.0"
    ],
    "fmuExport": [
        "CS"
    ],
    "fmuImport": [
        "CS"
    ]
}
```

The optional logo must be added to `/assets/images` as a PNG or SVG.
By submitting a logo the committer agrees that the logo is dispayed on the tools page.

### Tool Description

The description field should

- be a short description of the tool
- not repeat information that is in the table (supported platforms, FMI types and versions, vendor and license)
- have no dot (`.`) at the end if it's only one sentence
- be neutral and not use biased additions like ~~leading~~, ~~innovative~~, ~~flexible~~ or buzzwords (~~performance~~, ~~next generation~~)
- not contain hyperlinks or markup

## Adding a news post

To create a post, add a file to the `_posts` directory with the following format:

```
YEAR-MONTH-DAY-title.MARKUP
```

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. The date determines the placement in the news chronology and must not be in the future in order to be listed. `title` should not be longer than 50 characters and only contain lower case characters (`a-z`), digits (`0-9`) and hyphens (`-`).

The file name determines the [permalink](https://en.wikipedia.org/wiki/Permalink) to the post and must not be changed after it has been merged into `master`. E.g. the post

```
2018-09-04-modelica-conference-2019-regensburg-germany.md
```

can be accessed as

```
https://fmi-standard.org/news/2018/09/04/modelica-conference-2019-regensburg-germany.html
```

You typically write posts in [Markdown](https://daringfireball.net/projects/markdown/) (`.md`), however HTML (`.html`) is also supported.

All blog post files must begin with a front matter that sets the title, category and layout:

```markdown
---
title: FMI at the 13th Modelica Conference 2019 in Regensburg, Germany
categories: [news]
layout: post
---

The [13th International Modelica Conference](https://modelica.org/events/modelica2019) will be held at [OTH Regensburg](https://www.oth-regensburg.de/en.html), Germany, March 4–6, 2019.

The scope of the conference includes FMI in Modelica and non-Modelica applications and tools.
```

To include images, downloads or other files along with a post place them in the `assets` directory and reference them using the following markdown syntax:

```markdown
... which is shown in the screenshot below:
![My helpful screenshot](/assets/screenshot.jpg)
```

Linking to a PDF for readers to download:

```markdown
... you can [get the PDF](/assets/mydoc.pdf) directly.
```

## Building the website locally

1. Clone the repository, change into the directory and pull the changes
   ```
   git clone https://github.com/modelica/fmi-standard.org.git
   cd fmi-standard.org
   git pull
   ```

2. Install [Docker](https://www.docker.com/get-started)

3. Build the site and make it available on a local server

   Linux, Mac:
   ```
   docker run --volume="$PWD:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve --incremental
   ```
   
   Windows:
   ```
   docker run --volume="%cd%:/srv/jekyll" -p 4000:4000 -it jekyll/jekyll:4.2.0 jekyll serve --incremental
   ```

   Now browse to [http://localhost:4000](http://localhost:4000)

4. Before you push your changes, build and check your commit for syntax errors and broken links:

   Linux, Mac:
   ```
   docker run -v $PWD/_site:/site 18fgsa/html-proofer /site --only-4xx
   ```
   Windows:
   ```
   docker run -v %cd%/_site:/site 18fgsa/html-proofer /site --only-4xx
   ```
