---
title: Publications
permalink: /publications/
entries_layout: grid
image: assets/images/johan-van-wambeke-_2VioFUgQVg-unsplash.jpg
---

Airworthiness gems for the price of a coffee.

Thanks for your patience while this page loads ... 

{% assign pubs = site.data.gumroad %}
<script src="https://gumroad.com/js/gumroad-embed.js"></script>

<div class="entries-{{ page.entries_layout | default: 'list' }}">
  {%- for pub in pubs -%}
    <article class="entry">
      <div class="gumroad-product-embed"><a href="{{ pub.short_url }}">Loading...</a></div>
    </article>
  {%- endfor -%}
</div>
