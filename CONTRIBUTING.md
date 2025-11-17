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
The page is generated from [tools.json](static/assets/tools.json).
To add, edit or remove a tool from the list, update the respective entry and make a [pull request](#pull-requests).
Please respect the rules below when editing the file.

### Format

| Column           | Description                                                             | Example / valid values
|------------------|-------------------------------------------------------------------------|-----------------------
| name             | The tool name that appears in the tools list                            | `"Example Sim"`
| license          | License (commercial or [OSI approved](https://opensource.org/licenses)) | `"commercial"`, `"osi"`
| url              | Link to the tool's homepage                                             | `"https://example.com/example-sim/"`
| logo             | filename of the tool's logo (or company's logo)                         | `"example-sim.svg"`
| vendor           | Name of the tool vendor                                                 | `"Example Company"`
| vendorURL        | Link to the vendor's homepage                                           | `"https://example.com/"`
| examplesURL      | Link to the tool's example FMUs and compatibility information           | `"https://github.com/example/example-sim/"`
| description      | A [description](#tool-description) of the tool                          | `"Run simulations in the cloud in real time"`
| features         | Reserved for future use                                                 | `[]`
| platforms        | Supported platforms                                                     | `["macOS", "Linux", "Windows"]`
| interfaces       | Supported interfaces                                                    | `["GUI", "CLI", "library"]`
| fmiVersions      | Supported FMI versions                                                  | `["1.0", "2.0", "3.0"]`
| fmuExport        | Supported interface types for FMU export                                | `["CS", "ME", "SE"]`
| fmuImport        | Supported interface types for FMU import                                | `["CS", "ME", "SE"]`
| layeredStandards | Supported layered standards                                             | `["BUS", "XCP"]`

Example:

```json
{
    "name": "Example Sim",
    "license": "commercial",
    "url": "https://example.com/example-sim/",
    "logo": "example-sim.svg",
    "vendor": "Example Company",
    "vendorURL": "https://example.com/",
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
    ],
    "layeredStandards": [
        "BUS"
    ]
}
```

The optional logo must be added to `/assets/images/logos` as a PNG or SVG.
By submitting a logo the committer agrees that the logo is dispayed on the tools page.

### Tool Description

The description field should

- be a short description of the tool
- not repeat information that is in the table (supported platforms, FMI types and versions, vendor and license)
- have no dot (`.`) at the end if it's only one sentence
- be neutral and not use biased additions like ~~leading~~, ~~innovative~~, ~~flexible~~ or buzzwords (~~performance~~, ~~next generation~~)
- not contain hyperlinks or markup

### Compatibility information

FMU exporting and importing tools provide information to their users on how they have validated their FMI support.
Providing and maintaining this information is in the responsibility of the tool vendors. 
On the tools page of the FMI Webpage, a link to a repository or webpage of the tool vendor is provided as defined in `examplesURL`.
Tool vendors are encouraged to clearly mark this webpage as provided by them and not by the Modelica Association or the FMI Project, e.g., by prominently placing their logo on this page.

#### Exporting tools

* List the importing tools (including version information), with which the FMUs from this exporter have been imported and simulated successfully.
This could be (free or commercial) tools available to the tool vendor of the exporting tool. Or the tests could be performed by third parties (users, tool vendors of importing tools). 
* optionally proivde additional information needed to reproduce the results of the importers (e.g., compiler flags)
* Encouragement to provide example FMUs and any information needed to run this FMU and check expected results
  * Check the FMUs with at least one of the available checkers before uploading (see https://fmi-standard.org/validation/) and document this.
  * The folder structure can be chosen by the vendor to match the capabilities of the tool, e.g. by tool version. Each FMU and and files corresponding to it should be provided in a separate subfolder.
 _[It is possible to structure your repository according to FMI versions, FMI interface types (ME, CS, SE), platforms (consider to provide source code FMUs), but this not mandatory as this information is contained in the modelDescription.xml of each FMU]_

**Files to submit*** per exported FMU stored on the repository:

- `{Model_Name}.fmu`: The FMU.

- `{Model_Name}_ref.csv`: Reference solution as computed by the exporting tool.
It is recommended to limit the file to at most 10 of the important variables.
The solution must contain StartTime and EndTime as specified in {Model_Name}_ref.opt.

- `{Model_Name}_in.csv`: optional input signals in case the FMU has inputs.
The variables in this file must match the input variables defined in the modelDescription.xml.
If intermediate values are required for continuous signals, linear interpolation is to be applied.

- `{Model_Name}_ref.opt`: Options used to create reference output and to guide comparing against, CSV format: 

```
// required elements:
StartTime, 0.0              // in seconds
StopTime, 1.0               // in seconds
StepSize, 0.01              // in seconds, 0.0 for variable step solver
RelTol, 0.0001
// optional elements:
AbsTol, 0.001
SolverType, FixedStep       // predefined: FixedStep, VariableStep
OutputIntervalLength, 0.1   // reference data provided with this time spacing in seconds
```

- Readme.txt: provide information on what the FMU represents and which features of FMI can be tested with it.
 
Observe the naming conventions given here, including case.
We recommend keeping {Model_Name} short to avoid path length restriction problems on Windows.


#### Importing tools

* List exporting tools (including version information), from which FMUs have been successfully imported and simulated.
It is recommended to
  * list these FMUs and/or provide links to the repository of the exporting tool where they can be downloaded.
  * provide additional information needed to reproduce the results of the importers (e.g., compiler flags).

#### CSV Rules for inout and result files for compatibility information

CSV as input, output and reference file format is convenient as many tools support CSV import and export.
However, CSV is not restrictive enough to allow easy exchange of time-based signals.
Here we will declare a number of additional restrictions on top of the CSV format to ease handling:

- Separator: comma (`,`): separators may only be used between elements, not the end of a line

- Numbers must be unquoted and specified in the format used for floating point literals as in the C programming language (without the type suffix).

- All numeric cell entries contain numbers, labels for enumerations are not allowed (it would require readers to have access to the FMU information).
Boolean values should be expressed as `0` and `1`.
Binary values and strings are represented as for start values in the modeldescription.xml.
Arrays are serialized as for start values in the modelDescription.xml with space (` `) as separator.

- The first column contains the time.
The values in time must be monotonically increasing.

- The first line contains the variable names quoted with double quotes (`"`)

- All variable names are exactly the same as defined in the modelDescription.xml (no additional variables are allowed)

- Starting with line 2, data is supplied (no units in line 2, no comments allowed)

- A CSV file should not be larger than 1 Megabyte.

**Example:**
```
"time","xnum,"bin","arrayof3x2","s"
0.0,0,AA22BB33,1 2 3 4 5 6,"string1"
1.0,1,BB11FF4433,2 3 4 5 6 7,"string2"
```

### FMI tools forum

Tool vendors and other organizations that have a tool listed on the FMI website can get access to the GitHub Repository "FMI Tools Forum" (github.com/modelica/FMI-tools-forum).
This is a private repositry for the exchange between tool vendors. It is intended to exchange and solve problems with FMI implementations in a more protected area.
If you have a tool listed on the FMI Tools page and want to get access, please send an email to contact@fmi-standard.org providing your GitHub user name.

## Adding a news post

To create a post, add a file to `/content/news/` with the following format:

```
YEAR-MONTH-DAY-title.MARKUP
```

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. The date determines the placement in the news chronology and must not be in the future in order to be listed. `title` should not be longer than 50 characters and only contain lower case characters (`a-z`), digits (`0-9`) and hyphens (`-`).

The file name determines the [permalink](https://en.wikipedia.org/wiki/Permalink) to the post and must not be changed after it has been merged into `main`.
E.g. the post

```
2018-09-04-modelica-conference-2019-regensburg-germany.md
```

can be accessed as

```
https://fmi-standard.org/news/2018-09-04-modelica-conference-2019-regensburg-germany.html
```

You typically write posts in [Markdown](https://daringfireball.net/projects/markdown/) (`.md`), however HTML (`.html`) is also supported.

All blog post files must begin with a front matter that sets the title and date:

```markdown
---
title: FMI at the 13th Modelica Conference 2019 in Regensburg, Germany
date: 2014-07-25
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

## Serve the website locally

1. [Install Hugo extended version](https://gohugo.io/getting-started/installing/)
2. [Add a SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)
3. Clone the repo `git clone --recurse-submodules git@github.com:modelica/fmi-standard.org.git`
4. Change into the repository folder `cd fmi-standard.org`
5. Run `hugo serve` and browse to [http://localhost:1313](http://localhost:1313/)
