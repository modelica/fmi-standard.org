# Run project localy
## Requirements
1. Open Terminal.
2. Check whether you have Ruby 2.1.0 or higher installed:
  
  ```
  ruby --version
  ruby 2.X.X
  ```
3. If you don't have Ruby installed, install Ruby 2.0.0 or higher.

4. Install Bundler:
  
  ```
  gem install bundler
  # Installs the Bundler gem
  ```

5. Run Bundler:

  ```
  bundle
  ```

## Install
```
git clone git@github.com:modelica/fmi-standard.org.git
bundle exec jekyll serve
```
You should get:
```
Configuration file: /www/sites/fmi-standard/public/_config.yml
            Source: /www/sites/fmi-standard/public
       Destination: /www/sites/fmi-standard/public/_site
      Generating... 
                    done.
 Auto-regeneration: enabled for '/www/sites/fmi-standard/public'
Configuration file: /www/sites/fmi-standard/public/_config.yml
    Server address: http://0.0.0.0:4000/fmi-standard.org/
  Server running... press ctrl-c to stop.
```
Webpage is on URL `http://localhost:4000/fmi-standard.org/`

# Project structure
* `_data` - text content
 * `[page_name]`
   * `[section_name]`
     * `section.yml` - contain title of section
      * `[box_name].yml` - text content, more is [below](#write-content)
* `_includes` - parts templates
* `_layout` - layout templates
* `_posts`
 * `news` - news
   * `YYYY-MM-DD-title.md` - write news in [markdown](https://daringfireball.net/projects/markdown/syntax)
* `_sass` - styles soures
* `_site` - compiled webpage
* `assets` - assets files
* `css`- stylesheet prepared to compilation 
* `pages` - webpage structure
* `_congfig.yml` - site settings
* `Gemfile` - gem config
* `Gemfile.lock`

# Write content
Text content is in in [yml](http://www.yaml.org/spec/1.2/spec.html) files.

You can use this fields:
* `title:` - main box title
* `content:` or use `content: >` when you can't write content inline, content must be indented
  
  You can use [markdown](https://daringfireball.net/projects/markdown/syntax) and [html](http://www.w3schools.com/html)
  If you need two coulmun with subtitles use array:
  ```
  content:
    #first column
    -  
      - title: 
        content: 
      - title: Voting
        content: 
    # second column
    -
      - title: 
        content: 
      - title: 
        content: 
  ```
* `version:` - highlighted information about last release
* `packageLink:` - link for package download, when is filled download button is displayed
* `specificationLink` - link for specification download, when is filled download button is displayed
* `downloads:` - next items to download

  ```
  downloads:
  - text: 
    link: 
  - text: 
    link: 
  - text: 
    link: 
    ```
    
# Deployment
Just push to `master` branch:

`git push origin master`

Updates appear on https://modelica.github.io/fmi-standard.org/

# Resources
[Github Pages](https://pages.github.com)

[Jekylle](https://jekyllrb.com/)

[Markdown](https://daringfireball.net/projects/markdown/syntax)
