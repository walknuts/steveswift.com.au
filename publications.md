---
title: Publications
permalink: /publications/
image: assets/images/jerry-zhang-BvuZn3FhEdU-unsplash.jpg
---

Airworthiness gems for the price of a coffee.

_This page may take a little while to load all the details... thanks for your patience._

{% assign pubs = site.data.gumroad %}
<script src="https://gumroad.com/js/gumroad-embed.js"></script>

<div class="entries-grid">
  {%- for pub in pubs -%}
    <article class="entry">
      <div class="gumroad-product-embed"><a href="{{ pub.short_url }}">Loading...</a></div>
    </article>
  {%- endfor -%}
</div>
