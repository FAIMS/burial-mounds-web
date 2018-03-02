---
#
#   You have to options to include a search. Use the built-in
#   lunr.js which is perfect for small sites or use the
#   search include for google search
#
#   {% include google_search %}
#
#
permalink: /search/
layout: page
title: "Search"
sitemap: false
---
{% include search %}

<ul id="search-results" class="side-nav"></ul>

<script>
  window.store = {
    {% for post in site.posts %}
      "{{ post.url | slugify }}": {
        "title": "{{ post.title | xml_escape }}",
        "author": "{{ post.author | xml_escape }}",
        "category": "{{ post.category | xml_escape }}",
        "content": {{ post.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ post.url | xml_escape | absolute_url }}"
      },
    {% endfor %}
    {% for page in site.pages %}
      "{{ page.url | slugify }}": {
        "title": "{{ page.title | xml_escape }}",
        "author": "{{ page.author | xml_escape }}",
        "category": "{{ page.category | xml_escape }}",
        "content": {{ page.content | strip_html | strip_newlines | jsonify }},
        "url": "{{ page.url | xml_escape | absolute_url }}"
      }
      {% unless forloop.last %},{% endunless %}
    {% endfor %}
  };
</script>
<script src="{{ "/assets/js/lunr.min.js" | absolute_url }}"></script>
<script src="{{ "/assets/js/search.js" | absolute_url }}"></script>
