---
# Usee the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: page
title: Collection
header:
  image_fullwidth: /images/mq_banner/mqBanner.png
  background-color: #EFC94C

collection_page: true
#xclude_from_search: true
#search: false
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
#callforaction:
#  url: https://tinyletter.com/feeling-responsive
#  text: Inform me about new updates and features ›
#  style: alert
permalink: /collection/
---

<ul class="tabs" data-tabs id="category-tabs">
{%- assign javascript_google_map = site.data.additional_config.javascript_google_map -%}
  {%- if javascript_google_map == true -%}
 <li class="tabs-title is-active"><a data-tabs-target="#panel1" href="#panel1" aria-selected="true">Map</a></li>
 {%- endif -%}

 {%- for category in site.categories -%}
 {%- capture category_name -%}{{ category | first }}{%- endcapture-%}
 {%- assign index = forloop.index -%}
  {%- if javascript_google_map == true -%}
 {%- capture index -%}{{index | plus:1}}{%- endcapture -%}
 {%- endif -%}

  <li class="tabs-title {% if javascript_google_map == false %} {% if forloop.first %} is-active {% endif %}  {% endif %}">
    <a data-tabs-target="panel{{ index }}" href="#panel{{ index }}"> {{ category_name }} </a>
  </li>
 {%- endfor -%}
</ul>
<div class="tabs-content" data-tabs-content="category-tabs">
  {%- if javascript_google_map == true -%}
  <div class="tabs-panel is-active" id="panel1">
    <div id="home_page_map"></div>
  </div>
 {%- endif -%}
{%- for category in site.categories -%}
 {%- capture category_name -%}{{ category | first }}{%- endcapture-%}
 {%- assign index = forloop.index -%}
  {%- if javascript_google_map == true -%}
 {%- capture index -%}{{index | plus:1}}{%- endcapture -%}
 {%- endif -%}
  <div class="tabs-panel {% if javascript_google_map == false %} {% if forloop.first %} is-active {% endif %}  {% endif %}"  id="panel{{ index }}">
  <!-- <img style="width:100%" src="/images/collection{{forloop.index}}.jpg"/> -->
  <ul>
	 {%- for post in site.categories[category_name] reversed -%}
    <article class="archive-item">
      <li><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></li>
    </article>
  {%- endfor -%}
  </ul>
</div>
{%- endfor -%}
</div>
