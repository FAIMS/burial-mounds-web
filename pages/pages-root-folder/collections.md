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
 <li class="tabs-title is-active"><a data-tabs-target="#panel1" href="#panel1" aria-selected="true">Map</a></li>
 {%- for category in site.categories -%}
 {%- capture category_name -%}{{ category | first }}{%- endcapture-%}
 {%- assign index = forloop.index -%}
 {%- capture index -%}{{index | plus:1}}{%- endcapture -%}
  <li class="tabs-title ">
    <a data-tabs-target="panel{{ index }}" href="#panel{{ index }}"> {{ category_name }} </a>
  </li>
 {%- endfor -%}
</ul>
<div class="tabs-content" data-tabs-content="category-tabs">

  <div class="tabs-panel is-active" id="panel1">
    <div id="home_page_map"></div>
  </div>
{%- for category in site.categories -%}
 {%- capture category_name -%}{{ category | first }}{%- endcapture-%}
 {%- assign index = forloop.index -%}
 {%- capture index -%}{{index | plus:1}}{%- endcapture -%}

  <div class="tabs-panel"  id="panel{{ index }}">
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
