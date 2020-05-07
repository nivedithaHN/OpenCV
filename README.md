

# ROLE BASED USER ACCESS CONTROL     

##### Role-based user access control assigns roles to users and through these roles, users will be authorised to access resources and perform particular functions.   



---
---
## **Slack Integration**
---
---
# Steps to create a Slack bot in your workspace and integrate with YM platform -
---

1. Visit the link [link text](https://api.slack.com/apps), sign in to your workspace and click on **Create New App**
    ![image](https://octodex.github.com/images/yaktocat.png "This is a tooltip"){: width=200px}
    ![slack.png](img)
    ![[very good|512x397,20%]](https://cdn.yellowmessenger.com/UN5tGKpH9nbw1574251954153.png)
    ![b|small](https://cdn.yellowmessenger.com/QOgIktbx0Nop1574252039402.png)
    ![](https://cdn.yellowmessenger.com/QOgIktbx0Nop1574252039402.png){ width=50% }
    ![image](https://octodex.github.com/images/yaktocat.png){:width=200px}
    ![Benjamin Bannekat](https://octodex.github.com/images/bannekat.png)
2. Next, go back to your Slack config page by clicking on your app and go to **Bot Users** from the left-hand menu, and click the **Add a Bot User** button
   On the same screen, just go ahead and click **Add Bot User** green button at the end. You can change the display name and default username anytime later if you want

3. Next, install the app to your workspace once to obtain your OAuth token. Go to **Install App** from the left-hand menu and click the green **Install App to Workspace** button 
   Follow the screen and install it.

4. Once you finish installing, you should see this screen showing two tokens
   Copy **Bot User OAuth Access Token** that begins with **xoxb-**

5. Go to **Configuration > Channels > Slack**. Paste the copied bot token in YM platform
   And then click **Save Slack Token**

6. Go to **Event Subscriptions** from the left-hand menu, and turn the toggle switch on to enable events
   Paste “https://app.yellowmessenger.com/integrations/slack/receive/**botId**” in **Request URL** field
   Example : https://app.yellowmessenger.com/integrations/slack/receive/x157148753865834
   
   Note: When your request URL is correct, you should see a green checkmark

7. Scroll down to **Subscribe to Bot Events** on the same page
   Click the **Add Bot User Event** button to add *message_im, message_groups, message_channels, message_mpim* events
   
8. Go to **Interactive Components** from the left-hand menu, and turn the toggle switch on to enable events
   
   Paste “https://app.yellowmessenger.com/integration/slack/interaction/**botId**” in **Request URL** field
   Example: https://app.yellowmessenger.com/integration/slack/interaction/x157148753865834

And click **Save Changes**
---
__Advertisement :)__

- __[pica](https://nodeca.github.io/pica/demo/)__ - high quality and fast image
  resize in browser.
- __[babelfish](https://github.com/nodeca/babelfish/)__ - developer friendly
  i18n with plurals support and easy syntax.

You will like those projects!

---

# h1 Heading 8-)
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading


## Horizontal Rules

___

---

***


## Typographic replacements

Enable typographer option to see result.

(c) (C) (r) (R) (tm) (TM) (p) (P) +-

test.. test... test..... test?..... test!....

!!!!!! ???? ,,  -- ---

"Smartypants, double quotes" and 'single quotes'


## Emphasis

**This is bold text**

__This is bold text__

*This is italic text*

_This is italic text_

~~Strikethrough~~


## Blockquotes


> Blockquotes can also be nested...
>> ...by using additional greater-than signs right next to each other...
> > > ...or with spaces between arrows.


## Lists

Unordered

+ Create a list by starting a line with \`+\`, \`-\`, or \`*\`
+ Sub-lists are made by indenting 2 spaces:
  - Marker character change forces new list start:
    * Ac tristique libero volutpat at
    + Facilisis in pretium nisl aliquet
    - Nulla volutpat aliquam velit
+ Very easy!

Ordered

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa


1. You can use sequential numbers...
1. ...or keep all the numbers as \`1.\`

Start numbering with offset:

57. foo
1. bar


## Code

Inline \`code\`

Indented code

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


Block code "fences"

\`\`\`
Sample text here...
\`\`\`

Syntax highlighting

\`\`\` js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
\`\`\`

## Tables

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

Right aligned columns

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


## Links

[link text](http://dev.nodeca.com)

[link with title](http://nodeca.github.io/pica/demo/ "title text!")

Autoconverted link https://github.com/nodeca/pica (enable linkify to see)


## Images

![Minion](https://octodex.github.com/images/minion.png)
![Stormtroopocat](https://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

![Alt text][id]

With a reference later in the document defining the URL location:

[id]: https://octodex.github.com/images/dojocat.jpg  "The Dojocat"


## Plugins

The killer feature of \`markdown-it\` is very effective support of
[syntax plugins](https://www.npmjs.org/browse/keyword/markdown-it-plugin).


### [Emojies](https://github.com/markdown-it/markdown-it-emoji)

> Classic markup: :wink: :crush: :cry: :tear: :laughing: :yum:
>
> Shortcuts (emoticons): :-) :-( 8-) ;)

see [how to change output](https://github.com/markdown-it/markdown-it-emoji#change-output) with twemoji.


### [Subscript](https://github.com/markdown-it/markdown-it-sub) / [Superscript](https://github.com/markdown-it/markdown-it-sup)

- 19^th^
- H~2~O


### [\\<ins>](https://github.com/markdown-it/markdown-it-ins)

++Inserted text++


### [\\<mark>](https://github.com/markdown-it/markdown-it-mark)

==Marked text==


### [Footnotes](https://github.com/markdown-it/markdown-it-footnote)

Footnote 1 link[^first].

Footnote 2 link[^second].

Inline footnote^[Text of inline footnote] definition.

Duplicated footnote reference[^second].

[^first]: Footnote **can have markup**

    and multiple paragraphs.

[^second]: Footnote text.


### [Definition lists](https://github.com/markdown-it/markdown-it-deflist)

Term 1

:   Definition 1
with lazy continuation.

Term 2 with *inline markup*

:   Definition 2

        { some code, part of Definition 2 }

    Third paragraph of definition 2.

_Compact style:_

Term 1
  ~ Definition 1

Term 2
  ~ Definition 2a
  ~ Definition 2b


### [Abbreviations](https://github.com/markdown-it/markdown-it-abbr)

This is HTML abbreviation example.

It converts "HTML", but keep intact partial entries like "xxxHTMLyyy" and so on.

*[HTML]: Hyper Text Markup Language

### [Custom containers](https://github.com/markdown-it/markdown-it-container)

::: warning
*here be dragons*
:::
