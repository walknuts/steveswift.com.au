# Steve Swift Pty Ltd Jekyll website

Jekyll source files for building the
[steveswift.com.au](https://steveswift.com.au/) website.

Based on the [Basically Basic
theme](https://github.com/mmistakes/jekyll-theme-basically-basic) by [Michael
Rose](https://github.com/mmistakes/jekyll-theme-basically-basic).

## Howto

- to add an image inline in a page,
  1. upload an image file (e.g. `my-image.jpg`) to the
     [`assets/images/`](https://github.com/walknuts/steveswift.com.au/tree/master/assets/images)
     folder, then
  2. insert `![alt-text goes here]({{site.baseurl}}/{% link
  assets/images/my-image.jpg %})` into the place where you want the image to
  show up (replacing the `alt-text goes here` and `my-image.jpg` parts as
  appropriate)

- to change the [hero
  image](https://mmistakes.github.io/jekyll-theme-basically-basic/layout/layout-hero-image/)
  for a page,
  1. add the file to
     [`assets/images`](https://github.com/walknuts/steveswift.com.au/tree/master/assets/images)
     as in step 1 of the previous howto, then
  2. change the [front matter](https://jekyllrb.com/docs/front-matter/) so that
     the `image` key contains the correct (full) path, e.g. `image: assets/images/my-image.jpg`

- to add a new "news item", create a new file in the
  [`_posts`](https://github.com/walknuts/steveswift.com.au/tree/master/_posts)
  folder (follow the naming convention of the other files in there), then use
  starting content something like this:

  ```md
  ---
  title: "Onward and upward: exciting news from Steve Swift Pty. Ltd."
  ---

  The text of the news item (and any images, subheadings, etc.) starts here.
  ```

## Getting help

This theme's main docs are
[here](https://github.com/mmistakes/jekyll-theme-basically-basic/tree/master#structure)
and the demo site is [here](). In addition, the demo site has a bunch of
[posts](https://mmistakes.github.io/jekyll-theme-basically-basic/posts/) which
actually explain how to do certain things , and there's a [tags
index](https://mmistakes.github.io/jekyll-theme-basically-basic/tags/) for that
as well.

For more general help, there's the [main Jekyll
docs](https://jekyllrb.com/docs/front-matter/) or the [GitHub pages
docs](https://docs.github.com/en/pages). Or, you know, just ask
[Ben](https://github.com/benswift/).
