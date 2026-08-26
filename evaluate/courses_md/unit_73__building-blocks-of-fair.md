---
title: "Building Blocks of FAIR"
unit_id: 73
course_id: 3
level: "Foundation"
slug: building-blocks-of-fair
is_course: 0
---

# Building Blocks of FAIR

## Text content

### What Is FAIR?
What Is FAIR?
FAIR stands for:
F
indability: How accessible is the data you are collecting and putting out to the world. This should be easy to find in for humans and computers.
A
ccessible: Once found, the user needs to be able to access it in some way, shape, or form.
I
nteroperable: The data usually needs to have other data integrated into it. Also, the data should have an interoperate with applications or workflows for analysis, storage, etc.
R
eusable: Can the data provided be reproduced? Can the data provided be used in other ways and places? Can it be replicated?
Is FAIR and Open Data the Same?
Scientist are encouraged to share their data and findings openly. Open can be described as “data that can be downloaded freely from the internet.” (
https://www.natureindex.com/news-blog/what-scientists-need-to-know-about-fair-data
) FAIR refers to the thought of the people that can benefit from it. That’s where the use of DOIs (digital object identifiers) come in to play. DOIs are a way for researchers to, in a way, stamp their work and license it to which the data can be reused.
Not all FAIR data is open. They like the phrase, “as open as possible, as closed as necessary”. This means that not all data should be shared. An example of this is data that includes people’s medical information. That is what remains closed. That is personal information that should not be put out for the world to see.

### FAIR in Climate and Geoscience Setting
FAIR data is being used in many careers. One being Climate and Geoscience. They want to make their data available to all. It is publishing to repositories and journals. They want everyone to be educated in order for everyone to know the truth of what is going to our earth. They don’t want people making assumptions or false facts and it is harder to do so with all of the climate and geoscience data out there for everyone and anyone to see.

### Coming Up in the Modules
Coming up in the next modules and lessons, you will be able to learn about some of the different forms of programming tools like R studio, Python, and Jupyter Notebook. You will see the use, complexity, and how wide-spread Unix/Linux is. How it is the base for many other programs, and how these two are different.
You will learn about how you, yourself, is able to make your data FAIR through some of these tools that was mentioned and also through Repositories, where you can store your data and it still be FAIR. Here at Purdue, we have our own repository that you can publish to. It is called PURR. PURR stands for Purdue University Research Repository. Students can publish their own data to this repository as they desire. Everything in this course will tie back to how data is FAIR and how to make it FAIR.
Another thing that you will be learning is Metadata. In short, Metadata is data that provides data about other data (see lesson for more). Later, you will be able to see examples of these different things along with a more in-depth explanation of what they are and how to use them, along with some videos and PowerPoints.

## Fetched resources (external URLs)

### FAIR Principles (link)
*URL:* https://www.go-fair.org/fair-principles/

# FAIR Principles - GO FAIR

FAIR Principles - GO FAIR
×
×
Search
FAIR Principles
Home
›
FAIR Principles
Toggle menu
In 2016, the ‘
FAIR Guiding Principles for scientific data management and stewardship’
were published in
Scientific Data
. The authors intended to provide guidelines to improve the
F
indability,
A
ccessibility,
I
nteroperability, and
R
euse of digital assets. The principles emphasise machine-actionability (i.e., the capacity of computational systems to find, access, interoperate, and reuse data with none or minimal human intervention) because humans increasingly rely on computational support to deal with data as a result of the increase in volume, complexity, and creation speed of data.
A practical “how to” guidance to go FAIR can be found in the
Three-point FAIRification Framework
.
F
indable
The first step in (re)using data is to find them. Metadata and data should be easy to find for both humans and computers. Machine-readable metadata are essential for automatic discovery of datasets and services, so this is an essential component of the
FAIRification process
.
F1
. (Meta)data are assigned a globally unique and persistent identifier
F2
. Data are described with rich metadata (defined by R1 below)
F3
. Metadata clearly and explicitly include the identifier of the data they describe
F4
. (Meta)data are registered or indexed in a searchable resource
A
ccessible
Once the user finds the required data, she/he/they need to know how they can be accessed, possibly including authentication and authorisation.
A1
. (Meta)data are retrievable by their identifier using a standardised communications protocol
A1.1
The protocol is open, free, and universally implementable
A1.2
The protocol allows for an authentication and authorisation procedure, where necessary
A2
. Metadata are accessible, even when the data are no longer available
I
nteroperable
The data usually need to be integrated with other data. In addition, the data need to interoperate with applications or workflows for analysis, storage, and processing.
I1
. (Meta)data use a formal, accessible, shared, and broadly applicable language for knowledge representation.
I2
. (Meta)data use vocabularies that follow FAIR principles
I3
. (Meta)data include qualified references to other (meta)data
R
eusable
The ultimate goal of FAIR is to optimise the reuse of data. To achieve this, metadata and data should be well-described so that they can be replicated and/or combined in different settings.
R1
. (Meta)data are richly described with a plurality of accurate and relevant attributes
R1.1
. (Meta)data are released with a clear and accessible data usage license
R1.2
. (Meta)data are associated with detailed provenance
R1.3
. (Meta)data meet domain-relevant community standards
The principles refer to three types of entities: data (or any digital object), metadata (information about that digital object), and infrastructure. For instance, principle F4 defines that both metadata and data are registered or indexed in a searchable resource (the infrastructure component).
Download this overview of FAIR Principles as a
pdf-file
.
For a downloadable format of the FAIR Principles, visit the
FAIR-nanopubs page on GitHub
.

### FAIR data principles (link)
*URL:* https://www.youtube.com/watch?v=F13nkArkp_A

[YouTube transcript F13nkArkp_A]
[Music] [Music] first of all who's heard of the fair data principles okay so this is back 2014 Lauren's workshop in Leiden in the Netherlands a group of leading the thought leaders in this space including publishers including researchers including scholarly societies came together and said well what is a good way of thinking about data and making data available and they came up with these the four principles making data findable accessible interoperable and reusable and they actually broke those down quite thoroughly and it's proven to be really useful as a way of thinking about data and I think one of the big extra bits of value there is that they're thinking about how data can be made available in a form that it can be also be picked up by machines and be brought together found and reused so first of all data should be findable and when they say findable means it should have a DOI over the data it should be in a repository so that it can be found through different finding mechanisms around the world globally so through machines so preferably in a discipline repository or an institutional repository that feeds up into into international collection mechanisms the data should be accessible now this doesn't mean that it has to be open so there are good reasons why some datasets can't be made open and that's especially around sensitive data so date about humans but also data about biological specimens for example the location of the wool of my pine well now the wool of my pine is no longer threatened but when it originally was found that's the sort of data you don't want to throw out in the public immediately you need to make it available through appropriate mechanisms so that the researchers that need want to use it and want to be able to untangle and use those data can get access to it but that it is available through appropriate routes the data should also be accessible in a format that's easily to be easy to pick up sort of standard protocols that machines can use to defined it and access it the data should be interoperable as in using as much as possible discipline standards so that other researchers can easily pick it up and don't need to find some proprietary software to read it or use it or be able to combine it with a different type of data and finally the data should be reusable and when they talk about reusable first of all I always say the FDA and the IEEE are part of it being reusable because if you can't find it you won't be able to reuse it but building on top of those points I mentioned earlier it's important that the data also has a clear license over it so that somebody knows what they can do with it if there's no license you don't know what you can do with the data and also it needs associated information about how it was created so just having a table there saying this these are all our observations you actually need to have a bit of context around that knowing under which conditions were those was the data collected or if you have a series of interviews under which conditions were those interviews conducted and why did you select those respondents for those interviews so having some provenance information how did you make that selection and how did you select that data and make changes to the data maybe is a very important aspect in being able to reuse that data and understand it one of the actions was we worked on the cop des so on the the a GU enabling fair data project we were one of the partners in that space and that resulted in a commitment statement for that was signed has now been signed by a range of repository managers researchers research institutions and publishers look into that sort of have committed themselves to making data available and what they argue for there and that's something we very strongly encourage not to have the data as an appendix in the article because that actually doesn't make it very reusable but to have it in a repository where it can be made findable accessible interoperable and reusable so that means that other people can easily find that data but having an appropriate do I over that day to win an appropriate citation so that from the article you can reference the data and it's and with the appropriate credit associated with that when we're talking about making data accessible you can talk about it on the short-term but having it in that repository also means that it can stay there for a longer term and that's where we've been working with a number of data repositories and custodians around Australia saying well what does it mean to make that data available for the longer term and accessible for the longer term and one mechanism for that is to have it in a certified trusted data repository and there is now a court Russell's an international standard certification organization and you can have your repository certified as a court Russell certified repository so we've been working with the Australian data archive great archives in in Canberra there for social science data and worked with them what does it mean to have that their repository certified as a core trust yield certified repository and they were successful we've also been trying to provide guidance to the secretary around Australia what is it what does it mean to make your data fair what sort of things can you do this is a self-assessment tool that researchers or research support staff can use to hold up a data set and see how well are we scoring on making this data fair and what could we do to make it more fair what steps could we take what actions could we do so it's just tangible trying to turn it into real actions also developing skills around the country especially amongst the research support staff and one of the Act one of the things we did there was did a global sprint to develop top ten fair data and software things in different disciplines and they've been developed in they're now publicly available so anybody can pick them up and use them to untangle what does it mean to make data my data fair in a specific area so to make data fair actually requires actions from a number of different players stakeholders in this space so what can research you do researcher can make sure that they have an orchid that they know their institutional repository or discipline repository make sure that when they publish their data it does have a DOI so they can reference it and think about that longer-term editors can promote the use of trusted repositories the the actions you're already doing around standardizing journal data policy just makes it much easier for all the different stakeholders to publish that data and it's just consistent way and if you look at the research supports staff that's where we can they can help researchers make it easy make it reasonably seamless not put too much effort into that to have to put too much effort into this space

### The FAIR Data Principles (link)
*URL:* https://force11.org/info/the-fair-data-principles/

# The FAIR Data Principles – FORCE11

The FAIR Data Principles – FORCE11
Skip to content
The FAIR Data Principles
On this page:
Translations
Japanese
–
https://doi.org/10.18908/a.2019112601
(added 31.01.2020).
Preamble
One of the grand challenges of data-intensive science is to facilitate knowledge discovery by assisting humans and machines in their discovery of, access to, integration and analysis of, task-appropriate scientific data and their associated algorithms and workflows. Here, we describe FAIR – a set of guiding principles to make data Findable, Accessible, Interoperable, and Reusable.  The term FAIR was launched at a
Lorentz workshop
in 2014, the resulting  FAIR principles were
published
in 2016.
To be Findable:
F1. (meta)data are assigned a
globally unique and eternally persistent identifier.
F2. data are described with
rich metadata.
F3. (meta)data are
registered or indexed in a searchable resource.
F4. metadata
specify
the data identifier.
To be Accessible:
A1  (meta)data are
retrievable by their identifier
using
a standardized communications protocol.
A1.1 the
protocol
is open, free, and universally implementable.
A1.2 the
protocol
allows for an authentication and authorization procedure, where necessary.
A2
metadata are accessible
, even when the data are no longer available.
To be Interoperable:
I1. (meta)data use a
formal, accessible, shared, and broadly applicable language
for knowledge representation.
I2. (meta)data use
vocabularies that follow FAIR principles.
I3. (meta)data include
qualified references
to other (meta)data.
To be Re-usable:
R1. (meta)data have a
plurality of accurate and relevant attributes.
R1.1. (meta)data are released with a
clear and accessible data usage license.
R1.2. (meta)data are associated with their
provenance.
R1.3. (meta)data
meet domain-relevant community standards.
FAIR Principles Working Detailed Document
Archive:
https://archive.force11.net/node/6048
Close
We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept”, you consent to the use of ALL the cookies.
Do not sell my personal information
.
Cookie Settings
Accept
Manage consent
Close
Privacy Overview
This website uses cookies to improve your experience while you navigate through the website. Out of these, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may affect your browsing experience.
Necessary
Necessary
Always Enabled
Necessary cookies are absolutely essential for the website to function properly. These cookies ensure basic functionalities and security features of the website, anonymously.
Cookie
Duration
Description
cookielawinfo-checkbox-advertisement
1 year
Set by the GDPR Cookie Consent plugin, this cookie is used to record the user consent for the cookies in the "Advertisement" category .
cookielawinfo-checkbox-analytics
11 months
This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Analytics".
cookielawinfo-checkbox-functional
11 months
The cookie is set by GDPR cookie consent to record the user consent for the cookies in the category "Functional".
cookielawinfo-checkbox-necessary
11 months
This cookie is set by GDPR Cookie Consent plugin. The cookies is used to store the user consent for the cookies in the category "Necessary".
cookielawinfo-checkbox-others
11 months
This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Other.
cookielawinfo-checkbox-performance
11 months
This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Performance".
CookieLawInfoConsent
1 year
Records the default button state of the corresponding category & the status of CCPA. It works only in coordination with the primary cookie.
elementor
never
This cookie is used by the website's WordPress theme. It allows the website owner to implement or change the website's content in real-time.
viewed_cookie_policy
11 months
The cookie is set by the GDPR Cookie Consent plugin and is used to store whether or not user has consented to the use of cookies. It does not store any personal data.
Functional
Functional
Functional cookies help to perform certain functionalities like sharing the content of the website on social media platforms, collect feedbacks, and other third-party features.
Performance
Performance
Performance cookies are used to understand and analyze the key performance indexes of the website which helps in delivering a better user experience for the visitors.
Cookie
Duration
Description
_gat
1 minute
This cookie is installed by Google Universal Analytics to restrain request rate and thus limit the collection of data on high traffic sites.
Analytics
Analytics
Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics the number of visitors, bounce rate, traffic source, etc.
Cookie
Duration
Description
_ga
2 years
The _ga cookie, installed by Google Analytics, calculates visitor, session and campaign data and also keeps track of site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognize unique visitors.
_gid
1 day
Installed by Google Analytics, _gid cookie stores information on how visitors use a website, while also creating an analytics report of the website's performance. Some of the data that are collected include the number of visitors, their source, and the pages they visit anonymously.
CONSENT
2 years
YouTube sets this cookie via embedded youtube-videos and registers anonymous statistical data.
Advertisement
Advertisement
Advertisement cookies are used to provide visitors with relevant ads and marketing campaigns. These cookies track visitors across websites and collect information to provide customized ads.
Cookie
Duration
Description
VISITOR_INFO1_LIVE
5 months 27 days
A cookie set by YouTube to measure bandwidth that determines whether the user gets the new or old player interface.
YSC
session
YSC cookie is set by Youtube and is used to track the views of embedded videos on Youtube pages.
yt-remote-connected-devices
never
YouTube sets this cookie to store the video preferences of the user using embedded YouTube video.
yt-remote-device-id
never
YouTube sets this cookie to store the video preferences of the user using embedded YouTube video.
Others
Others
Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.
Cookie
Duration
Description
wplegalpages-update-notice-147470
8 hours
No description
wplegalpages-update-notice-147471
8 hours
No description
wplegalpages-update-notice-147472
8 hours 1 minute
No description
SAVE & ACCEPT
Powered by

### What scientists need to know about FAIR data (link)
*URL:* https://www.nature.com/nature-index/news-blog/what-scientists-need-to-know-about-fair-data

# "A love letter to your future self": What scientists need to know about FAIR data | News | Nature Index

"A love letter to your future self": What scientists need to know about FAIR data | News | Nature Index
Skip to main content
Advertisement
×
Institutions
Institutions
Countries/territories
Topics
Article
Search
Search
Search
Search
Time frame: 1 March 2025 - 28 February 2026
Institution search supports local language names.
(Examples: Universidad Autónoma de Madrid
,
筑波大学)
View the latest institution rankings
View the latest Country/territory rankings
View topics
Jon Brock
Email
Bluesky
Facebook
LinkedIn
Reddit
Whatsapp
X
Credit: Caiaimage/Rafal Rodzoch
Nature Index 360°
The idea that scientific data should be
FAIR
— Findable, Accessible, Interoperable, and Reusable — is one increasingly endorsed by scientific institutions including the
United States
National Academies of Science Engineering and Medicine
, the
European Commission
, and the Wellcome Trust. But it is yet to gain much traction among the people that ultimately matter, the scientists generating the data. The 2018 State of Open Data report, published by Digital Science, found that just 15% of researchers were “familiar with FAIR principles”. (Digital Science is operated by the Holtzbrinck Publishing Group, which also has a majority share in the publisher of the Nature Index.)
So what do scientists need to know about FAIR?
Nature Index
spoke to Kate LeMay, senior research data specialist at the Australian Research Data Commons, and Lambert Heller, leader of the Open Science Lab at TIB, the German National Library of Science and Technology.
Is FAIR the same as open data?
Increasingly, researchers are encouraged to share their data openly. But open data and FAIR data are distinct concepts. “When we’re talking about open data,” LeMay says, “we’re generally referring to data that can be downloaded freely from the internet.” But researchers need to do more than simply post their data on the web for it to be useful.
Lambert Heller
“FAIR means thinking about the people who could benefit from your data,” explains Heller. “It means adding persistent identifiers like DOIs [digital object identifiers] to the data, having a stable URL so the data doesn’t ‘disappear’, adding metadata that describes the data and a license stating the conditions under which it can be reused. It also means presenting the data in a standardized way so it’s machine readable.”
Data can also be FAIR but not open. The guiding principle, Heller says, is for data to be “as open as possible, as closed as necessary”. A classic example is medical data, where access has to be controlled to ensure patient privacy and confidentiality. In such cases, LeMay explains, the FAIR approach would be to make the metadata publicly available and provide information about the conditions for accessing the data itself.
What exactly is metadata?
Kate LeMay
Metadata describe the data and are critical to helping users discover relevant datasets. “We love rich metadata,” says LeMay. “We want to know who made the data, where it was made, what it contains, who to credit, how to reference the dataset.”
Metadata can also include keywords, field of science classification codes, the DOIs of related papers, the researchers’ ORCID identifiers, and the codes for the grants that supported the research. For help with metadata, LeMay recommends talking to university librarians, whose experience with cataloguing books and journals has put them at the forefront of data archiving and curation.
Why does FAIR data need a license?
True interoperability (the I in FAIR) requires that the data and metadata follows predetermined standards with a consistent structure and agreed vocabularies and ontologies (keywords for describing the data). This allows the data to be interrogated automatically and datasets to be merged. The challenge, LeMay notes, is that different research fields have different cultures and requirements for data and metadata. “There needs to be community ownership of these data standards,” she says. “We can’t just impose them on researchers.”
Where should FAIR data be stored?
Most researchers currently share their data either as supplementary material to a journal article or in an independent data repository. Although the FAIR guidelines don’t state a preference, Heller notes that repositories such as Zenodo, Figshare and the Open Science Framework offer useful tools that help researchers make their uploaded data FAIR; for example, generating a DOI and populating the metadata. Repositories also allow researchers to make data curation part of their ongoing workflow, rather than an additional task at the end of the publication process. “It’s never too early to make your data reusable,” he says. “If I could add one more letter to FAIR it would be T for timely.”
What’s in it for researchers?
Many scientific journals and research funders now require scientists to share their data openly.
Nature
, for example, recently
endorsed
the Enabling FAIR Data initiative, which requires authors in the Earth, space and environmental science to share their supporting data on community repositories, where available. The American Chemical Society's author guidelines state that supplementary information submitted with a manuscript will be automatically hosted on Figshare "to promote open data discoverability and use of your research outputs." (See more details in the 'Useful resources' section below, particularly 'Fairsharing.org' and 'Publisher commitment'.)
But as LeMay argues, there are both altruistic and selfish reasons for researchers to take the next step and make their data FAIR. “Most people get into research because they want to make a difference,” she says. “That includes making your data as useful as possible.” FAIR can also be good for career advancement, particularly for early-career researchers. “FAIR helps you demonstrate the impact of your research when people re-use and cite your dataset,” LeMay says. “It gets your name out there and can lead to new collaborations.”
Heller agrees. However, the true benefit of FAIR, he argues, is in providing a framework for researchers to manage their own data so they can themselves find it, understand it, and reuse it. “As a scientist, you should treat your data like a love letter to your future self,” he says.
USEFUL RESOURCES
Introducing FAIR
Cochrane Living Systematic Review website
Publisher commitment
List of
signatories
to the Coalition for Publishing Data in the Earth and Space Sciences Statement of Commitment. The list includes Springer, Elsevier, and several other publishers of journals in the Nature Index. The site includes a helpful
FAQ
.
FAIRsharing.org
A resource on existing data and metadata
standards and policies
, including those linked to specific funders and journals.
re3data.org
A detailed
registry
of more than 2,000 research data repositories to assist in finding the right repository for your data.
License finder
A simple tool for choosing the right
Creative Commons license
.
Further learning
Webinar series
provided by the Australian National Data Service for those in the business of creating and curating research data.
See also:
Big data goes green
Correction 19/03/2019: Springer has signed onto the Coalition for Publishing Data in the Earth and Space Sciences. An earlier version suggested it was Springer Nature.
This is the first article in the
Nature Index 360°
series, which takes an all-round look at key topics in scientific research performance and publishing
.
Subjects
Open access
National Academies of Science Engineering and Medicine
European Commission
United States
Advertisement
Sign up to the Nature Index newsletter
Get regular news, analysis and data insights from the editorial team delivered to your inbox.
Email Address
Sign up to receive the Nature Index newsletter. I agree my information will be processed in accordance with the
Nature
and Springer Nature Limited
Privacy Policy
.
