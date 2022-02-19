---
title: Publications
permalink: /publications/
image: assets/images/johan-van-wambeke-_2VioFUgQVg-unsplash.jpg
---

Airworthiness gems for the price of a coffee.

{% assign pubs = site.data.gumroad %}

<div class="entries-grid">
  {%- for pub in pubs -%}
    <article class="entry">
      <h3 class="entry-title">{{ pub.name }}</h3>
      <a href="{{ pub.short_url }}">
        <div style="overflow: hidden; padding-top: 75%; background: url({{pub.preview_url }}) no-repeat center; background-size: contain;"></div>
      </a>
      <div class="entry-excerpt">
        {{ pub.description }}
      </div>
    </article>
  {%- endfor -%}
</div>
