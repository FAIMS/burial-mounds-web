---
# Usee the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: page
title: Collections
header:
  image_fullwidth: /images/mq_banner/mqBanner.png
  background-color: #EFC94C

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
permalink: /collections/
---






<ul class="tabs" data-tabs id="category-tabs">

{% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}


<li class="tabs-title {% if forloop.first %} is-active {% endif %}" ><a data-tabs-target="panel{{forloop.index}}" href="#panel{{ forloop.index }}" {% if forloop.first %} aria-selected="true" {% endif %}>{{ category_name }}</a></li>
{% endfor %}
</ul>

<div class="tabs-content" data-tabs-content="category-tabs">
{% for category in site.categories %}
    {% capture category_name %}{{ category | first }}{% endcapture %}
<div class="tabs-panel {% if forloop.first %} is-active {% endif %}" id="panel{{ forloop.index }}">
<!-- <img style="width:100%" src="/images/collection{{forloop.index}}.jpg"/> -->
<ul>
	{% for post in site.categories[category_name] %}
    <article class="archive-item">

      <li><a href="{{ post.url }}">{{post.title}}</a></li>
</article>
    {% endfor %}
</ul>    
</div>
{% endfor %}
</div>
