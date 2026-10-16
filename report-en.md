---
title: Model Token Price Comparison (English report)
permalink: /README.html
---
{% capture report %}{% include_relative README.md %}{% endcapture %}{{ report | replace: "](README.md)", "](README.html)" | replace: "](README.zh-CN.md)", "](README.zh-CN.html)" }}
