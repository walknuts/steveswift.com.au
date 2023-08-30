---
title: Papers
permalink: /papers/
image: assets/images/jerry-zhang-BvuZn3FhEdU-unsplash.jpg
---

Airworthiness gems, freely available to all. [Send me an
email](mailto:{{site.email}}) if you'd like a copy of any of these
presentations.

{% assign pubs = site.data.gumroad %}

<div class="entries-list">
  {%- for pub in pubs -%}
    <article class="entry">
    <img style="margin-bottom: 1em;" src="{{ pub.name | slugify | append: '.jpg' | prepend: '/assets/images/papers/' | prepend: site.baseurl }}">
    {{ pub.description }}
    </article>
  {%- endfor -%}
</div>
