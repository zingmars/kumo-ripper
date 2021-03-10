I'm a spider, so what WN fan translation pdf creator
===

A couple of scripts I wrote to scrape the web novel translations and create pdfs of the said translations. No changes are done to the content, it just downloads them and creates a html file and generates a pdf file from it. Requires python 3 with pdfKit and bs4 libraries. pdfKit requires wkhtmltopdf available [here](https://wkhtmltopdf.org/downloads.html).

(Github) I've also added the rips to the releases section, but I'm not going to be updating them.

### Some links:

Original WN can be found [here](http://ncode.syosetu.com/n7975cr/) (in Japanese).

MAL link for the VN: [here](https://myanimelist.net/manga/95012/Kumo_desu_ga_Nani_ka).

Yen press (official English distributor) link for the VN: [here](https://yenpress.com/series-search/?series=yen310-so-im-a-spider-so-what-light-novel&supapress_order=publishdate-asc).

Where to start reading: [click here](https://it-came-from-the-labyrinth.blogspot.com/p/so-where-do-i-start.html).

KumoDesu subreddit FAQ: [click here](https://old.reddit.com/r/KumoDesu/wiki/faq)

## Scripts

* blastron.py - downloads the fan translation from [blastron](https://blastron01.tumblr.com/kumoko-contents). Chapters 1 - 154.
* turb0.py - downloads the fan translation from [turb0 translations](https://turb0translation.blogspot.com/p/blog-page.html). Contains chapters 1-336. Note that these are lower quality than the blastron ones, and it's recommended to read the blastron ones and then switch to turb0.
* rtd.py - downloads translations from [Raising the dead](https://rtd.moe/novels/kumo-desu-ga-nani-ka/). Chapters 336+.
* rtd-single.py - use it to download a single chapter (pass the full url as a parameter) from Raising the dead.
