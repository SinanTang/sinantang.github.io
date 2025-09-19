---
title: How I use Claude Code - Tips for AI-Native Development
date: 2025-09-19
categories:
- AI Development
tags:
- Claude Code
- AI
- Development
- Productivity
---

![Claude Code Presentation](/assets/images/cc-presentation-slides.png){:style="margin:0 auto"}

In the age of AI, I often find myself reflecting on this Chinese proverb: "工欲善其事，必先利其器" (If a technician wants to do good work, she must first sharpen her tools). What strikes me is how profoundly true this has become—perhaps more than ever before in the history of software development. The tools we choose don't just affect our productivity; they fundamentally shape how we think about problems, architect solutions, and collaborate with both humans and AI systems.

I've spent the past several months deep in the trenches with Claude Code, and what I've observed is striking: the productivity gap before and after isn't just incremental—it's 10x or even more. Developers who learn to truly collaborate with AI tools are operating in an entirely different paradigm, solving problems at a different level of abstraction while the AI handles implementation details that would have consumed hours or days of human effort.

This post documents the techniques and patterns I've battle-tested through extensive production and personal use of Claude Code.

## Context Engineering: An Evolution from Prompt Engineering

The AI development community has increasingly adopted the term "context engineering" to describe the practice of structuring information for Large Language Models (LLMs). This approach recognizes that LLMs, similar to human developers, perform better when provided with comprehensive context about the task at hand.

![context_engineering](/assets/images/context.png){:style="margin:0 auto"}

This shift from crafting individual prompts to building persistent, structured context has measurably improved the quality and consistency of generated code for me.

## Configuration Architecture

### User + Project level CLAUDE.md files

Utilizing both global and project-level `CLAUDE.md` files provides an effective method to drastically improve Claude's instruction following capabilities and the code quality it can produce. The global CLAUDE.md acts like the "meta-prompt" establishing high level philosophy and principles, while project-level CLAUDE.md contains specific project knowledge and context.

Global user-level `CLAUDE.md` example:

```markdown
# Engineering Philosophy
## Core Beliefs

- **Simplicity is the ultimate sophistication**
- **Incremental progress over big bangs** - Small changes that compile and pass tests
- Avoid over-engineering - YAGNI (You Aren't Gonna Need It)
- **Learning from existing code** - Study and plan before implementing
- **Clear intent over clever code** - Be boring and obvious

### Simplicity Means

- Single responsibility per function/class
- Avoid premature abstractions
- No clever tricks - choose the boring solution
- If you need to explain it, it's too complex

## Design Principles

- **Defensive programming** - validate inputs, handle edge cases
- **Fail-fast design** - eliminate invalid cases early
- **Separation of concerns** - each module does one thing well
- **Security by default** - never trust user input
```

Experiment and iterate to find the prompt that works best for your use case. Recently I tried out the popular "Linus Torvalds" prompt ([one example](https://gist.github.com/iiiyu/4c8286062c589f3f6d6093cb9fecbe42)) which worked exceptionally well for me and has become a part of my Claude Code meta-prompt.

Project-level `CLAUDE.md` focuses on codebase-specific patterns such as:

```markdown
## Project Structure
repo/
├── src/
│   └── ...
├── tests/                      # Unit test suite
├── e2e_tests/                  # End-to-end integration tests
├── docs/                       # Documentation
│   ├── architecture/           # System design docs
│   ├── development/            # Development guides
│   ├── deployment/             # Deployment procedures
│   └── updates/                # Project updates
├── scripts/                    # SQL scripts and utilities
├── deploy/                     # Deployment configurations
├── pyproject.toml              # Project configuration
└── mkdocs.yml                  # Documentation config

## Comments & Documentation

- Comments explain **why**, not what
- Keep comments close to code (inline > separate docs)
- Update comments when code changes
- Document key decisions and trade-offs

## Python Imports and Path Guidelines

- Use absolute imports throughout the codebase, e.g. `from src.api import HTTPServerApp`.
- Never use relative imports (`.module`) or sys.path manipulation
- Run all commands with UV: e.g. `uv run python script.py`
```

### Custom Commands for Common Operations

Custom slash commands reduce repetition and standardize common workflows. These commands, stored in `~/.claude/commands/`, become available across all sessions. I frequently use the `/test`, `/lint`, `/pr-describe` custom commands throughout my dev process. E.g.,

```bash
# ~/.claude/commands/test.md
---
description: fix unit tests
model: claude-sonnet-4-20250514
---

Run all tests and fix failures incrementally:
1. Execute the test suite
2. Identify failing tests
3. Fix issues sequentially, re-running after each fix
4. Provide a summary of changes made
```

### Subagents for Specialized Tasks

Subagents enable parallel task execution within a shared context. This new-ish feature addresses the common pattern of running multiple Claude Code sessions for different tasks in the same project. You can easily define an agent using natural language in a Markdown file in `~/.claude/agents/`.

Check out the [example subagents](https://docs.claude.com/en/docs/claude-code/sub-agents#example-subagents) "code-reviewer", "unit-test-writer" and "debugger" templates from Anthropic. I also defined my own subagent to improve my prompt.

For example, after I have agreed on the implementation plan written by one Claude agent, I would often invoke the code-reviwer subagent in another Claude Code session (`Use the code-reviwer subagent to review the implementation plan in docs/...`).

## Production Development Workflows

### Iterative Development Phases

Analysis of multiple projects has led to a five-phase workflow that balances automation with manual oversight:

1. **Exploration**: Opus model analyzes codebase structure and identifies integration points
2. **Planning**: Utilize Opus for architectural decisions and design
3. **Implementation**: Deploy Sonnet 4 for detailed coding tasks
4. **Testing**: Engage specialized subagents for test coverage
5. **Commit**: Review and document changes

### The Plan mode

Different Claude models demonstrate varying strengths. Opus performs well in strategic planning and architectural design but shows limitations in detailed implementation. Sonnet 4 excels at code generation, unit test creation, and concrete implementation tasks. This observation has informed a practical approach: using Opus for architectural decisions and Sonnet for implementation details. The introduction of Plan mode has made the switch between models even more intuitive.

### Documentation as Context Persistence

Documentation serves a dual purpose: team knowledge sharing and context maintenance across Claude Code sessions. Complex features benefit from pre-implementation documentation:

```markdown
# docs/development/2025-08-08-authentication-refactoring-plan.md

# [Feature Name] Implementation Plan

## Overview

[Brief description of what you're building and why it's needed. 1-2 sentences maximum.]

## Motivation

[List the key drivers for this implementation. Use bullet points with bold labels:]

- **Performance**: [Performance improvements expected]
- **Extensibility**: [How this enables future features]
- **Clean Architecture**: [Architectural benefits]
- **User Experience**: [User-facing improvements]

## Architecture Design

...

## Implementation Checklist

### Stage 1: Foundation
- [ ] [Analysis task]
- [ ] [Design task]
- [ ] [Setup task]

### Stage 2: [Data Layer Name]
- [ ] [Implementation task]
- [ ] [Testing task]
- [ ] [Validation task]

### Stage 3: [Business Logic Name]
- [ ] [Implementation task]
- [ ] [Integration task]
- [ ] [Testing task]

### Stage 4: Documentation & Testing
- [ ] [Documentation task]
- [ ] [Performance verification task]
- [ ] [Final validation task]
---

**Status**: [Planning|In Progress|Complete]
**Next**: [Next immediate action]
**Estimated Completion**: [Time estimate]
```

This approach addresses context window limitations by allowing Claude to resume work with full understanding of prior decisions and progress.

### Multi-Clauding

Operating multiple Claude Code sessions has proven effective for complex development tasks. A typical setup includes:
- Primary session for planning and core implementation
- Secondary session for code review and test generation
- Optional third session for documentation or exploratory work

When combined with git worktrees, this configuration enables safe experimentation with alternative implementations without affecting the main development branch.

## Feedback Mechanisms

The quality of Claude's output correlates with the feedback quality provided, as LLMs are trained by feedback mechanisms, like rewards or penalties, during the reinforment training process.
Three feedback categories have proven particularly effective:

**Syntactic Feedback**: Compilation errors and linting issues provide clear signals that Claude processes efficiently.

**Behavioral Feedback**: Test results offer detailed information about functionality. Comprehensive test suites improve Claude's ability to identify and correct issues.

**Visual Feedback**: For frontend development, screenshots often communicate UI issues much more effectively than text descriptions. Claude's image processing capabilities make this approach particularly useful.

## Iterative Development and Course Correction

Experience suggests that early intervention and guidance produce better results than allowing Claude to proceed far into a suboptimal solution. Key practices:

- Allocating substantial time (often exceeding 50% of total task time for me) to initial requirement definition and context setup
- Providing early guidance when implementation approaches appear suboptimal
- Rolling back all changes and restarting when Claude is stuck rather than attempting incremental fixes
- Treating Claude as a capable but guidance-requiring development partner

## Practical Observations

Extended work with Claude Code has revealed several patterns worth noting. The tool functions most effectively not as an autonomous system but as a collaborative partner requiring architectural guidance and strategic direction. Success depends less on the tool's inherent capabilities and more on the user's ability to structure context, provide clear requirements, and establish effective feedback loops.

The distinction between Claude Code and traditional development tools lies in its collaborative nature. Rather than simple code completion or generation, it offers a development partnership where human developers focus on architecture and strategy while Claude handles implementation details under guidance.

The evolution toward AI-assisted development represents a shift in how software is created, not merely in the tools used. Understanding how to effectively communicate intent, maintain context, and guide AI systems through complex implementation tasks has become a valuable addition to the developer's skill set.
