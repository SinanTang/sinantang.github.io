# Blog Migration Analysis: Jekyll to Modern Stack

**Date**: September 2025
**Current Stack**: Jekyll + GitHub Pages
**Evaluation Focus**: Ghost CMS and alternatives

## Executive Summary

After thorough analysis, **Ghost CMS is not recommended** for this migration due to fundamental incompatibilities with GitHub Pages and your requirement for a simple markdown-based workflow. Instead, I recommend migrating to a modern static site generator (Astro, Hugo, or Eleventy) that maintains your current simplicity while offering professional features.

## Current Site Analysis

### Site Statistics
- **Total Posts**: 98 (2017-2023)
- **Languages**: Mixed Chinese/English content
- **URL**: https://sinantang.github.io/
- **Hosting**: GitHub Pages (free)
- **Theme**: Custom Jekyll theme (appears to be based on NexT)

### Technical Stack
```
Framework: Jekyll 3.x
Markdown Processor: Kramdown
Syntax Highlighter: Rouge
Deployment: GitHub Pages
Domain: Custom domain via CNAME
```

### Content Structure
```
_posts/           # 98 blog posts in YYYY-MM-DD-title.md format
assets/
  ├── images/     # Blog images and assets
  ├── css/        # Stylesheets
  ├── js/         # JavaScript files
  └── fonts/      # Web fonts
_includes/        # Jekyll partials
_layouts/         # Page templates
_sass/           # Sass stylesheets
about/           # About page
```

## Ghost CMS Evaluation

### Why Ghost Fails Your Requirements

#### 1. **GitHub Pages Incompatibility**
- Ghost requires Node.js runtime environment
- GitHub Pages only serves static files
- Would require complex workarounds:
  ```
  Local Ghost → Static Generator → Manual Export → Git Commit → GitHub Pages
  ```

#### 2. **Workflow Complexity**
Your current workflow:
```
Write Markdown → Git Commit → PR → Auto Deploy
```

Ghost workflow would be:
```
Run Ghost Server → Write in Ghost Editor → Export Static Site →
Process with GSSG → Fix URLs → Commit → PR → Deploy
```

#### 3. **Feature Loss in Static Export**
When converting Ghost to static:
- ❌ Comments system
- ❌ Search functionality
- ❌ Member subscriptions
- ❌ Newsletter features
- ❌ Dynamic routing
- ❌ API access

#### 4. **Maintenance Overhead**
- Need to maintain local Ghost installation
- Database management
- Regular Ghost updates
- Static export tool maintenance
- URL structure mismatches

### Ghost Static Site Generator (GSSG) Limitations
- Tool hasn't been updated recently
- Requires manual intervention for images
- URL structure incompatibilities
- No automatic GitHub Pages deployment
- Complex redirect management needed

## Recommended Alternative: Modern SSG

### Top Recommendations

#### 1. **Astro** (Highly Recommended)
```yaml
Pros:
  - Excellent performance (100/100 Lighthouse scores)
  - Native markdown support with MDX
  - Component islands architecture
  - Rich ecosystem of themes
  - GitHub Pages deployment guide
  - Active development (2025)

Cons:
  - Newer framework (less established)
  - JavaScript/Node.js based
```

#### 2. **Hugo** (Best for Speed)
```yaml
Pros:
  - Blazing fast build times (< 1ms per page)
  - Single binary, no dependencies
  - Excellent markdown support
  - Many professional themes
  - GitHub Actions support
  - Mature and stable

Cons:
  - Go templating learning curve
  - Less flexible than JS-based SSGs
```

#### 3. **Eleventy (11ty)** (Best for Flexibility)
```yaml
Pros:
  - Zero client-side JavaScript by default
  - Multiple templating languages
  - Easy Jekyll migration path
  - GitHub Pages compatible
  - Simple and flexible

Cons:
  - Smaller theme ecosystem
  - Configuration can be complex
```

## Migration Strategy

### Phase 1: Preparation
- [ ] Backup current site completely
- [ ] Document custom features/modifications
- [ ] Audit all 98 posts for special formatting
- [ ] List all image dependencies

### Phase 2: Content Migration

#### Files to Keep
| Path | Description | Action |
|------|-------------|--------|
| `_posts/*.md` | All 98 blog posts | Convert frontmatter |
| `assets/images/` | Blog images | Copy as-is |
| `about/index.md` | About page | Update frontmatter |
| `CNAME` | Custom domain | Keep if exists |

#### Files to Deprecate
| Path | Description | Replacement |
|------|-------------|------------|
| `_includes/` | Jekyll partials | New theme components |
| `_layouts/` | Page templates | New theme layouts |
| `_sass/` | Stylesheets | New theme styles |
| `_site/` | Build output | New build folder |
| `Gemfile*` | Ruby deps | package.json or config |
| `_config.yml` | Jekyll config | New SSG config |

### Phase 3: Implementation Steps

```markdown
## Stage 1: Setup New SSG
**Goal**: Working local environment
**Success Criteria**: Can build and preview site locally
**Tests**:
  - [ ] Homepage loads
  - [ ] Sample post renders
  - [ ] Images display correctly

## Stage 2: Content Migration
**Goal**: All posts migrated
**Success Criteria**: All 98 posts render correctly
**Tests**:
  - [ ] Chinese posts display correctly
  - [ ] English posts display correctly
  - [ ] Images load from correct paths
  - [ ] Links work

## Stage 3: Theme & Styling
**Goal**: Professional appearance
**Success Criteria**: Clean, modern design
**Tests**:
  - [ ] Responsive on mobile
  - [ ] Fast loading times
  - [ ] Accessible navigation

## Stage 4: GitHub Pages Deployment
**Goal**: Automated deployment
**Success Criteria**: Push to main deploys site
**Tests**:
  - [ ] GitHub Action runs successfully
  - [ ] Site accessible at github.io URL
  - [ ] Custom domain works (if applicable)

## Stage 5: Polish & Optimize
**Goal**: Production-ready site
**Success Criteria**: Better than current site
**Tests**:
  - [ ] SEO meta tags present
  - [ ] RSS feed works
  - [ ] 404 page exists
  - [ ] Performance scores > 90
```

## Frontmatter Conversion Examples

### Current Jekyll Format
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

### Astro Format
```yaml
---
title: 隐喻的世界：浅谈语言对思维的反向塑造
pubDate: 2017-02-26
categories: ["Linguistics"]
tags: ["reading", "philosophy", "Linguistics"]
layout: ../../layouts/BlogPost.astro
---
```

### Hugo Format
```yaml
---
title: "隐喻的世界：浅谈语言对思维的反向塑造"
date: 2017-02-26
categories: ["Linguistics"]
tags: ["reading", "philosophy", "Linguistics"]
---
```

## GitHub Actions Deployment

### Example for Astro
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v1
        with:
          path: ./dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v1
```

## Decision Matrix

| Criteria | Ghost + Static | Astro | Hugo | Eleventy | Stay Jekyll |
|----------|---------------|-------|------|----------|-------------|
| GitHub Pages Compatible | ❌ Complex | ✅ | ✅ | ✅ | ✅ |
| Simple Workflow | ❌ | ✅ | ✅ | ✅ | ✅ |
| Modern Features | ✅ | ✅ | ✅ | ✅ | ❌ |
| Performance | ❓ | ✅✅ | ✅✅✅ | ✅✅ | ✅ |
| Theme Options | ✅✅ | ✅✅ | ✅✅ | ✅ | ✅ |
| Learning Curve | High | Medium | Low | Low | None |
| Maintenance | High | Low | Very Low | Low | Low |
| Future Proof | ✅ | ✅✅ | ✅✅ | ✅ | ❌ |

## Final Recommendation

**Do not migrate to Ghost** for a GitHub Pages hosted site. Instead:

1. **If you want modern features with great DX**: Choose **Astro**
2. **If you want maximum speed and simplicity**: Choose **Hugo**
3. **If you want flexibility and JavaScript**: Choose **Eleventy**
4. **If current setup works well**: Consider staying with Jekyll but updating the theme

All recommended options maintain your desired workflow:
- Write in Markdown
- Commit to Git
- Automatic deployment via GitHub Pages
- Zero hosting costs
- Low maintenance

## Next Steps

1. **Choose your SSG** based on the evaluation above
2. **Test migration** with 5-10 posts first
3. **Select a professional theme** from the SSG's ecosystem
4. **Set up GitHub Actions** for automated deployment
5. **Migrate incrementally** to avoid disruption

## Resources

### Astro
- [Official Docs](https://astro.build)
- [GitHub Pages Deploy Guide](https://docs.astro.build/en/guides/deploy/github/)
- [Blog Theme Gallery](https://astro.build/themes/?categories%5B%5D=blog)

### Hugo
- [Official Docs](https://gohugo.io)
- [GitHub Pages Guide](https://gohugo.io/hosting-and-deployment/hosting-on-github/)
- [Theme Gallery](https://themes.gohugo.io/)

### Eleventy
- [Official Docs](https://www.11ty.dev)
- [GitHub Pages Tutorial](https://www.11ty.dev/docs/deployment/#github-pages)
- [Starter Projects](https://www.11ty.dev/docs/starter/)

---

*Document prepared for blog migration planning. All recommendations based on September 2025 analysis of current Jekyll site and available technologies.*