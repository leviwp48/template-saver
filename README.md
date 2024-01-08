<h1 align="center">Template Saver</h1>

# Overview 
Template Saver is a simple bot designed to streamline sending repeated messages such as announcements and reminders.

# Usage

## Commands

### .new

### .view

### .use

### .how
This will display a message that tells how to use this bot 

## How to Use

### Creating a New Template

Use the `.new` command with the following arguments (each between quotes):
- Template name
- Keywords (comma-separated)
- Template text with keywords embedded between quotes (e.g., '[keyword]')

Example:
```markdown
.new "Event Members", "member, event", "
   List of members for [event]: 
   * [member] 
   * [member]"
```

### Viewing Saved Templates
Use the .view command to see your saved templates.

### Using Saved Templates
To use a saved template:

1. Enter values in the same order as they appear in the text.
2. Use the .use command with the following arguments (each between quotes):
   - Template name
   - Words to insert into the template (comma-separated)

Example: `.use "Event Members", "Game Night, Joe, Lucas"`

This will result in:
```markdown
List of members for Game Night:
Joe
Lucas
```

Remember to put arguments between quotes.


