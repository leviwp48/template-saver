
<h1 align="center">Template Saver</h1>


# Overview 
Template Saver is a simple bot that makes it easier to send repeated messages such as announcements and reminders. 

# Usage

### Commands

#### .how
'''
How to use this bot: 

=================================
Make a new Template: 

Use the .new command with the following arguments (each between quotes) 
- Template name
- Keywords to use in a comma separated list 
- Text for the Template with your keywords embedded between quotes -> Like so: '[keyword]' 

     Example: .new "Event Members", "member, event", "
        List of members for [event]: 
         * [member] 
         * [member]" 

Remember to put arguments between quotes 
=================================

=================================
View any saved Templates: 

Use the .view command and you'll see your saved Templates
=================================

=================================
Use any saved Templates: 
 
NOTE: You will need to enter your values in the same order as they appear in the text. In this case, "[event]" comes first, so you would enter the value for the event first 

Use the .use command with the following arguments (each between quotes) 
- Template name
- Words to insert into template (in a comma separated list)

    Example: .use "Event Members", "Game Night, Joe, Lucas"
    This will result in: 
    List of members for Game Night: 
    * Joe
    * Lucas 

 Remember to put arguments between quotes 
=================================
'''
