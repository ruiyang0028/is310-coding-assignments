# Assignment for Sep 17: Inspecting the Cultural Web

**Name:** Rui Yang  
**Topic:** Ancient Greek Mythology Retellings

## Website

For this assignment, I inspected the Encyclopaedia Britannica article:

**Types of Myths in Greek Culture**  
https://www.britannica.com/topic/Greek-mythology/Types-of-myths-in-Greek-culture

I chose this website because it is directly related to my project topic, Ancient Greek Mythology. In my project, I am interested in how Greek myths were preserved and how they communicated religious beliefs, social values, cultural ideas, and explanations of the world. Britannica provides an organized digital presentation of information about Greek mythology, making it useful for examining how cultural information is presented on the web.

---

## Web Technologies

### HTML

I used Chrome Developer Tools to inspect the HTML structure of the Britannica webpage. The Elements panel shows that the page uses standard HTML elements such as `<html>`, `<head>`, `<body>`, `<div>`, and `<article>`.

The page contains many nested `<div>` elements that organize different parts of the website, including the navigation bar, article content, advertisements, and other page components. The article itself is also organized within HTML elements such as `<article>` and other containers.

**Evidence:** The Chrome Developer Tools Elements panel shows the HTML structure of the webpage.

![HTML structure](images/html-inspection.png)

---

### CSS

The Britannica webpage uses CSS to control its layout and appearance. In the Developer Tools panel, I found CSS classes such as `flex-column`, `h-100`, and `position-relative`.

The Developer Tools also showed references to external stylesheet files, including `britannica-ui.css`. This indicates that Britannica uses external CSS files and CSS classes to control the visual design and layout of the webpage.

**Evidence:** The Styles panel in Chrome Developer Tools displays CSS rules and references to Britannica stylesheet files.

![CSS inspection](images/css-inspection.png)

---

### JavaScript

The webpage also uses JavaScript to provide dynamic and interactive functionality. In the HTML inspected through Developer Tools, I found multiple `<script>` elements. Some of these scripts load external JavaScript files, while others contain JavaScript directly within the page.

This shows that the Britannica page is not simply a static HTML document. JavaScript is used to support interactive and dynamic parts of the website.

**Evidence:** The Elements panel shows multiple `<script>` elements and external JavaScript resources.

![JavaScript inspection](images/javascript-inspection.png)

---

### Other Technologies

The page also contains external resources and embedded content. For example, the HTML includes `<iframe>` elements that are used to embed external content such as advertisements and third-party services.

This shows that the webpage is connected to other external services in addition to its main Britannica content.

---

## Who Built the Website?

The Britannica article was created and maintained by multiple contributors rather than by a single person.

The article identifies the following primary contributors:

- A.W.H. Adkins
- John Richard Thornhill Pollard
- The Editors of Encyclopaedia Britannica

The article also lists many other Encyclopaedia Britannica contributors. The article history shows contributions including revisions, media additions, links, cross-references, and other changes.

The article history provides evidence that the page has been maintained and updated by different people over a long period of time. The history shown on the website includes contributions dating back to 1998 and continuing through 2026.

For example, the article history shows contributions from people such as Grace Young, Amy Tikkanen, Gloria Lotha, Gitanjali Roy, Kara Rogers, Alicia Zelazko, and other Britannica contributors.

This suggests that the webpage is the result of an ongoing editorial process involving many contributors rather than a single author.

![Article contributors](images/contributors.png)

![Article history](images/article-history.png)

---

## GitHub Repository

I looked for a public GitHub repository for the Britannica website/article. I could not identify a public GitHub repository containing the source code for this specific Britannica webpage.

Because Britannica is a large commercial website, much of its website code is not publicly available as a single GitHub repository.

---

## Assessment

Overall, the Britannica webpage demonstrates how a traditional cultural reference source can be presented through a modern website. The page combines HTML for its structure, CSS for its visual layout, and JavaScript for dynamic and interactive functionality.

I also found that the article is maintained by many contributors over time. The contributor information and article history show that cultural information on the website is not necessarily produced by one person. Instead, it is continuously edited, updated, and expanded by an editorial team and other contributors.

This is especially relevant to my Ancient Greek Mythology project because the website is not only presenting information about Greek myths; it is also showing how modern digital platforms organize, preserve, and interpret cultural knowledge.

## Conclusion

Inspecting the Britannica webpage helped me understand that a cultural website is more than the information that appears on the screen. The page is supported by multiple layers of HTML, CSS, JavaScript, external resources, and contributions from many people. Looking at the underlying structure helped me see how cultural knowledge is organized and presented digitally.