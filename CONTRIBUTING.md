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

*Please ask first* before embarking on any significant pull request (e.g. implementing features, refactoring code, porting to a different language),
otherwise you risk spending a lot of time working on something that the project's developers might not want to merge into the project.

Please adhere to the coding conventions used throughout a project (indentation, accurate comments, etc.) and any other requirements (such as test coverage).

Follow this process if you'd like your work considered for inclusion in the project:

1. [Fork](https://help.github.com/articles/fork-a-repo/) the project, clone your fork, and configure the remotes:

  ```bash
  # Clone your fork of the repo into the current directory
  git clone https://github.com/<your-username>/<repo-name>
  # Navigate to the newly cloned directory
  cd <repo-name>
  # Assign the original repo to a remote called "upstream"
  git remote add upstream https://github.com/<upstream-owner>/<repo-name>
  ```

2. If you cloned a while ago, get the latest changes from upstream:

  ```
  git checkout <dev-branch>
  git pull upstream <dev-branch>
  ```

3. Create a new topic branch (off the main project development branch) to contain your feature, change, or fix:

  ```
  git checkout -b <topic-branch-name>
  ```

4. Commit your changes in logical chunks. Please adhere to the above rules when crafting [commit messages](#commit-messages) or your code is unlikely be merged into the main project. Use Git's [interactive rebase](https://help.github.com/articles/about-git-rebase/) feature to tidy up your commits before making them public.

5. Locally merge (or rebase) the upstream development branch into your topic branch:

  ```
  git pull [--rebase] upstream <dev-branch>
  ```

6. Push your topic branch up to your fork:

  ```
  git push origin <topic-branch-name>
  ```

7. [Open a pull request](https://help.github.com/articles/about-pull-requests/) with a clear title and description.

**IMPORTANT**: By submitting a patch, you agree to allow the project owner to license your work under the same license as that used by the project.

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

If you use an issue tracker, put references to them at the bottom,
like this:

Resolves: #123
See also: #456, #789
```

## Updating the tools list

The [tools page](https://fmi-standard.org/tools/) is generated from [_data/tools.csv](_data/tools.csv). To add, edit or remove a tool from the list, update the respective line and push your changes.

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

1. Install a full [Ruby development environment](https://www.ruby-lang.org/en/downloads/)

2. Clone the repository, change into the directory and pull the changes
   ```
   git clone https://github.com/modelica/fmi-standard.org.git
   cd fmi-website
   git pull
   ```

3. Install the Jekyll and [bundler](https://jekyllrb.com/docs/ruby-101/#bundler) [gems](https://jekyllrb.com/docs/ruby-101/#gems) and install the dependencies
   ```
   gem install jekyll bundler
   bundle install
   ```

4. Build the site and make it available on a local server
   ```
   bundle exec jekyll serve
   ```

5. Now browse to [http://localhost:4000](http://localhost:4000)

Before you push you changes, build and check your commit for syntax errors and broken links:

```
bundle exec jekyll build
bundle exec htmlproofer ./_site --only-4xx
```
