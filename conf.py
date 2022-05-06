# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'sethdoty.dev'
copyright = '2022, Seth Doty'
author = 'Seth'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
"ablog",
"sphinx.ext.intersphinx",
"sphinx_sitemap",
"sphinx_fontawesome",
"sphinx_panels",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "*import_posts*", "**/pandoc_ipynb/inputs/*", ".nox/*", "README.md"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_extra_path = ["feed.xml"]

def setup(app):
    app.add_css_file("custom.css")

html_sidebars = {
    "index": ["aboutme.html"],
    "about": ["aboutme.html"],
    "blog": ["tagcloud.html", "archives.html"],
    "blog/**": ["postcard.html", "recentposts.html", "archives.html"],
}

html_theme_options = {
    # If you want to configure Twitter or Github social media buttons to show up to the right of your nav bar,
    # you can use the "github_url" and "twitter_url" options:
    "github_url": "https://github.com/sethmdoty/",
    # You can also change the text that is in the search bar before people click on it by setting the
    "search_bar_text": "Search for wisdom...",
    # By default your site will have a search bar in the nav bar, but when we include the about.html,
    # this gets removed to so you can add one to the top "navbar" instead
    "navbar_end": ["navbar-icon-links.html", "search-field.html"]
}
blog_baseurl = 'https://sethdoty.dev'
blog_feed_archives = True

blog_feed_templates = {
      # Use defaults, no templates
      "atom": {},
      # Create content text suitable posting to social media
      "social": {
         # Format tags as hashtags and append to the content
         "content": "{{ title }}{% for tag in post.tags %}"
         " #{{ tag.name|trim()|replace(' ', '') }}"
         "{% endfor %}",
      },
}

# Glob pattern that grabs all posts so you don't need to specify which posts are blog posts in each post
# This pattern facilitates a folder structure such as posts/2020/my-awesome-post.rst
blog_post_pattern = "posts/*/*"

# post_redirect_refresh: Number of seconds (default is 5) that a redirect page waits before refreshing the page
# to redirect to the post.
post_redirect_refresh = 1

# post_auto_image: Index of the image that will be displayed in the excerpt of the post. Default is 0, meaning no
# image. Setting this to 1 will include the first image
post_auto_image = 1

# post_auto_excerpt: Number of paragraphs (default is 1) that will be displayed as an excerpt from the post. Setting
# this 0 will result in displaying no post excerpt in archive pages.
post_auto_excerpt = 3

fontawesome_link_cdn = "https://pro.fontawesome.com/releases/v5.13.0/css/all.css"