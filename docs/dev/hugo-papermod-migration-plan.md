# Hugo PaperMod Migration Plan

**Date**: September 2025
**Target Stack**: Hugo + PaperMod Theme
**Current Stack**: Jekyll + Custom Theme

## Why PaperMod?

PaperMod is the most popular Hugo theme with:
- **12,000+ GitHub stars** (actively maintained)
- **Fast performance** (90+ Lighthouse scores)
- **Built-in features**: Dark mode, search, TOC, multilingual support
- **Clean, minimal design** perfect for professional blog
- **Excellent documentation** and community support

## Migration Overview

### Phase 1: Setup & Testing (Day 1)
- [ ] Install Hugo locally
- [ ] Setup new branch `hugo-migration`
- [ ] Initialize Hugo site structure
- [ ] Install PaperMod theme
- [ ] Test with 5 sample posts

### Phase 2: Content Migration (Day 2-3)
- [ ] Convert Jekyll posts to Hugo format
- [ ] Migrate images and assets
- [ ] Setup redirects for URL changes
- [ ] Verify all 98 posts render correctly

### Phase 3: Configuration (Day 4)
- [ ] Configure PaperMod features
- [ ] Setup analytics and newsletter
- [ ] Add custom domain support
- [ ] Configure SEO settings

### Phase 4: Deployment (Day 5)
- [ ] Setup GitHub Actions
- [ ] Test deployment pipeline
- [ ] Switch DNS when ready
- [ ] Archive Jekyll version

## Technical Implementation

### 1. Hugo Installation & Setup

```bash
# Install Hugo (macOS)
brew install hugo

# Create new Hugo site (in new branch)
git checkout -b hugo-migration
hugo new site . --force

# Add PaperMod theme
git submodule add --depth=1 https://github.com/adityatelange/hugo-PaperMod.git themes/PaperMod
```

### 2. Project Structure Transformation

```
Jekyll Structure → Hugo Structure
─────────────────────────────────
_posts/          → content/posts/
assets/images/   → static/images/
about/index.md   → content/about.md
_config.yml      → hugo.yml
index.html       → (handled by theme)
_layouts/        → (replaced by theme)
_includes/       → (replaced by theme)
_sass/          → (replaced by theme)
```

### 3. Frontmatter Conversion

#### Jekyll Format:
```yaml
---
title: 隐喻的世界：浅谈语言对思维的反向塑造
date: 26-02-2017
categories:
- Linguistics
tags:
- reading
- philosophy
- Linguistics
---
```

#### Hugo Format:
```yaml
---
title: "隐喻的世界：浅谈语言对思维的反向塑造"
date: 2017-02-26
draft: false
categories: ["Linguistics"]
tags: ["reading", "philosophy", "Linguistics"]
summary: "「我们讲的语言并不单纯是思维的产物..."
weight: 1
---
```

### 4. Conversion Script

```python
#!/usr/bin/env python3
# convert_jekyll_to_hugo.py

import os
import re
import shutil
from datetime import datetime
from pathlib import Path
import yaml

def convert_post(jekyll_file, hugo_dir):
    """Convert single Jekyll post to Hugo format"""

    # Read Jekyll post
    with open(jekyll_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter and content
    parts = content.split('---', 2)
    if len(parts) >= 3:
        frontmatter = yaml.safe_load(parts[1])
        body = parts[2]
    else:
        return False

    # Convert frontmatter
    hugo_frontmatter = {
        'title': frontmatter.get('title', ''),
        'date': convert_date(jekyll_file.name, frontmatter.get('date')),
        'draft': False,
        'categories': frontmatter.get('categories', []),
        'tags': frontmatter.get('tags', []),
    }

    # Extract summary from content (first paragraph)
    summary = extract_summary(body)
    if summary:
        hugo_frontmatter['summary'] = summary

    # Generate Hugo filename
    date_match = re.match(r'(\d{4}-\d{2}-\d{2})-(.+)\.md', jekyll_file.name)
    if date_match:
        hugo_filename = f"{date_match.group(2)}.md"
    else:
        hugo_filename = jekyll_file.name

    # Write Hugo post
    hugo_path = hugo_dir / hugo_filename
    with open(hugo_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(hugo_frontmatter, f, allow_unicode=True, default_flow_style=False)
        f.write('---\n')
        f.write(process_content(body))

    print(f"✓ Converted: {jekyll_file.name} → {hugo_filename}")
    return True

def convert_date(filename, date_str):
    """Convert Jekyll date to Hugo format"""
    # Try to extract from filename first
    date_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', filename)
    if date_match:
        return f"{date_match.group(1)}-{date_match.group(2)}-{date_match.group(3)}"

    # Fallback to frontmatter date
    if date_str:
        if isinstance(date_str, str):
            # Parse formats like "26-02-2017"
            try:
                dt = datetime.strptime(date_str, '%d-%m-%Y')
                return dt.strftime('%Y-%m-%d')
            except:
                pass
    return datetime.now().strftime('%Y-%m-%d')

def extract_summary(content, max_length=160):
    """Extract first paragraph as summary"""
    lines = content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('!'):
            # Remove markdown formatting
            summary = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
            summary = re.sub(r'[*_`]', '', summary)
            if len(summary) > max_length:
                summary = summary[:max_length] + '...'
            return summary
    return ""

def process_content(content):
    """Process content for Hugo compatibility"""
    # Fix image paths
    content = content.replace('../assets/images/', '/images/')
    content = content.replace('assets/images/', '/images/')

    # Remove Jekyll-specific Liquid tags
    content = re.sub(r'{%.*?%}', '', content)
    content = re.sub(r'{{.*?}}', '', content)

    # Fix any Jekyll-specific markdown extensions
    content = re.sub(r'{:\.([^}]+)}', '', content)
    content = re.sub(r'{:([^}]+)}', '', content)

    return content

def main():
    # Paths
    jekyll_posts = Path('_posts')
    hugo_posts = Path('content/posts')
    jekyll_images = Path('assets/images')
    hugo_images = Path('static/images')

    # Create Hugo directories
    hugo_posts.mkdir(parents=True, exist_ok=True)
    hugo_images.mkdir(parents=True, exist_ok=True)

    # Convert posts
    converted = 0
    failed = 0

    for post in jekyll_posts.glob('*.md'):
        if convert_post(post, hugo_posts):
            converted += 1
        else:
            failed += 1

    # Copy images
    if jekyll_images.exists():
        for img in jekyll_images.glob('*'):
            shutil.copy2(img, hugo_images / img.name)
        print(f"✓ Copied {len(list(jekyll_images.glob('*')))} images")

    print(f"\n📊 Migration Summary:")
    print(f"   Converted: {converted} posts")
    print(f"   Failed: {failed} posts")
    print(f"   Images: {len(list(hugo_images.glob('*')))} files")

if __name__ == '__main__':
    main()
```

### 5. Hugo Configuration (hugo.yml)

```yaml
baseURL: "https://sinantang.github.io/"
title: "SinansNotes"
paginate: 10
theme: "PaperMod"
defaultContentLanguage: "en"
defaultContentLanguageInSubdir: false

enableRobotsTXT: true
buildDrafts: false
buildFuture: false
buildExpired: false
enableEmoji: true
pygmentsUseClasses: true

# Google Analytics
googleAnalytics: "" # Add your tracking ID

minify:
  disableXML: true
  minifyOutput: true

# Menu configuration
menu:
  main:
    - identifier: posts
      name: Posts
      url: /posts/
      weight: 10
    - identifier: about
      name: About
      url: /about/
      weight: 20
    - identifier: archives
      name: Archives
      url: /archives/
      weight: 30
    - identifier: search
      name: Search
      url: /search/
      weight: 40

params:
  env: production
  title: "SinansNotes"
  description: "making a dent in the universe"
  keywords: [Blog, Portfolio, NLP, Technology, Books]
  author: "Sinan"

  defaultTheme: auto # dark, light, auto
  disableThemeToggle: false

  ShowReadingTime: true
  ShowShareButtons: true
  ShowPostNavLinks: true
  ShowBreadCrumbs: true
  ShowCodeCopyButtons: true
  ShowWordCount: false
  ShowRssButtonInSectionTermList: true
  UseHugoToc: true
  disableSpecial1stPost: false
  disableScrollToTop: false
  comments: false
  hidemeta: false
  hideSummary: false
  showtoc: true
  tocopen: false

  assets:
    favicon: "/favicon.ico"
    favicon16x16: "/favicon-16x16.png"
    favicon32x32: "/favicon-32x32.png"
    apple_touch_icon: "/apple-touch-icon.png"

  # Profile mode
  profileMode:
    enabled: true
    title: "Hi, I'm Sinan 👋"
    subtitle: "NLP engineer by day, content creator by night"
    imageUrl: "/images/avatar.jpg"
    imageWidth: 120
    imageHeight: 120
    imageTitle: "Sinan"
    buttons:
      - name: Posts
        url: posts
      - name: About
        url: about

  # Social icons
  socialIcons:
    - name: github
      url: "https://github.com/sinantang"
    - name: email
      url: "mailto:tangsinan92@gmail.com"

  # Search
  fuseOpts:
    isCaseSensitive: false
    shouldSort: true
    location: 0
    distance: 1000
    threshold: 0.4
    minMatchCharLength: 0
    keys: ["title", "permalink", "summary", "content"]

  # For content
  cover:
    hidden: false
    hiddenInList: false
    hiddenInSingle: false

# Output formats for search
outputs:
  home:
    - HTML
    - RSS
    - JSON

# Markup settings
markup:
  highlight:
    anchorLineNos: true
    codeFences: true
    guessSyntax: true
    lineNos: false
    noClasses: false
    style: monokai

# Privacy settings
privacy:
  googleAnalytics:
    anonymizeIP: true
    disable: false
    respectDoNotTrack: true
```

### 6. GitHub Actions Deployment

```yaml
# .github/workflows/hugo.yml
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'
          extended: true

      - name: Build
        env:
          HUGO_ENVIRONMENT: production
          HUGO_ENV: production
        run: |
          hugo --gc --minify --baseURL "https://sinantang.github.io/"

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v3
```

### 7. Additional Features Setup

#### Newsletter Integration (Buttondown)

Create `layouts/partials/extend_footer.html`:
```html
<div class="newsletter-signup">
  <h3>Subscribe to Newsletter</h3>
  <form
    action="https://buttondown.email/api/emails/embed-subscribe/YOUR_BUTTONDOWN_ID"
    method="post"
    target="popupwindow"
    onsubmit="window.open('https://buttondown.email/YOUR_BUTTONDOWN_ID', 'popupwindow')"
  >
    <input type="email" name="email" placeholder="Enter your email" required>
    <input type="hidden" value="1" name="embed"/>
    <input type="submit" value="Subscribe" />
  </form>
</div>
```

#### Analytics Integration

Add to `hugo.yml`:
```yaml
params:
  analytics:
    plausible:
      dataDomain: sinantang.github.io
```

Create `layouts/partials/extend_head.html`:
```html
<script defer data-domain="sinantang.github.io" src="https://plausible.io/js/script.js"></script>
```

## Migration Checklist

### Pre-Migration
- [ ] Backup current Jekyll site
- [ ] Test Hugo locally
- [ ] Review PaperMod documentation
- [ ] Prepare conversion script

### During Migration
- [ ] Run conversion script
- [ ] Verify all posts converted
- [ ] Check image paths
- [ ] Test Chinese content rendering
- [ ] Configure PaperMod features
- [ ] Setup custom domain

### Post-Migration
- [ ] Test all links
- [ ] Verify SEO metadata
- [ ] Setup redirects from old URLs
- [ ] Configure analytics
- [ ] Add newsletter signup
- [ ] Update README
- [ ] Archive Jekyll version

## Rollback Plan

If issues arise:
1. Keep Jekyll site in `jekyll-archive` branch
2. GitHub Pages can point back to Jekyll branch
3. DNS changes can be reverted within minutes

## Expected Benefits

- **Build Speed**: 100x faster (< 1 second vs 30+ seconds)
- **Performance**: 95+ Lighthouse scores
- **Features**: Built-in search, dark mode, TOC
- **Maintenance**: Active development, 12k+ stars
- **Workflow**: Same markdown → git → deploy

## Timeline

- **Day 1**: Setup and testing
- **Day 2-3**: Content migration
- **Day 4**: Configuration and features
- **Day 5**: Deployment and go-live

Total migration time: ~1 week including testing

## Resources

- [PaperMod Demo](https://adityatelange.github.io/hugo-PaperMod/)
- [PaperMod Documentation](https://github.com/adityatelange/hugo-PaperMod/wiki)
- [Hugo Documentation](https://gohugo.io/documentation/)
- [Jekyll to Hugo Migration Guide](https://gohugo.io/tools/migrations/)

---

*This plan provides a complete roadmap for migrating from Jekyll to Hugo with PaperMod theme while preserving all existing content and improving site performance.*