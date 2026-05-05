---
type: promcon-talk
conference: PromCon
edition: "PromCon 2017"
edition_id: 2017-munich
year: 2017
city: "Munich"
country: "Germany"
topics: ["Prometheus Core", "Alerting"]
speakers: []
source_url: https://promcon.io/2017-munich/talks/improving-user-and-developer-experience-of-the-alertmanager-ui/
youtube_url: https://www.youtube.com/watch?v=TpifnbUGXD8
youtube_search_url: https://www.youtube.com/results?search_query=Improving+User+and+Developer+Experience+of+the+Alertmanager+UI+PromCon+2017
video_match_score: 0.974
status: video-found
---

# Improving User and Developer Experience of the Alertmanager UI

## Identificação

- Edição: PromCon 2017
- País/cidade: Germany / Munich
- Temas: [[Prometheus Core]], [[Alerting]]
- Speakers: N/A
- Página oficial: https://promcon.io/2017-munich/talks/improving-user-and-developer-experience-of-the-alertmanager-ui/
- YouTube: https://www.youtube.com/watch?v=TpifnbUGXD8

## Resumo

Speaker: Max Inden Alertmanager deduplicates, groups, and routes alerts from Prometheus to all kinds of paging services. With it comes a dated UI which does not live up to the expectations of the users, nor does it attract new contributors. From this talk, you will learn how we addressed these issues when building the new UI from scratch.

## Abstract oficial

Speaker: Max Inden

Alertmanager deduplicates, groups, and routes alerts from Prometheus to all
kinds of paging services. With it comes a dated UI which does not live up to
the expectations of the users, nor does it attract new contributors.

From this talk, you will learn how we addressed these issues when building the
new UI from scratch. We made it friendlier to users by removing unnecessary
domain language noise. In addition we added new power features such as
filtering and grouping. As a result, it is now much easier to navigate through
thousands of alerts.

We chose to build the new UI with Elm — a functional programming language for
web interfaces. Elm enabled us to develop fast and with confidence by keeping a
promise of zero runtime errors. It lowered the entry barrier for non-frontend
developers and made the project appealing to newcomers.



Video link -
Slides

## Links

- Página oficial: https://promcon.io/2017-munich/talks/improving-user-and-developer-experience-of-the-alertmanager-ui/
- YouTube: https://www.youtube.com/watch?v=TpifnbUGXD8
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TpifnbUGXD8
- YouTube title: PromCon 2017: Improving User and Developer Experience of the Alertmanager UI - Max Inden
- Match score: 0.974
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2017/improving-user-and-developer-experience-of-the-alertmanager-ui/TpifnbUGXD8.txt
- Transcript chars: 17303
- Keywords: javascript, pretty, actually, little, manager, function, alerts, probably, framework, exactly, usability, experience, course, entire, language, maintainability, started, experts

### Resumo baseado na transcript

[Music] hi I'm Joyce I'm gonna guide you through the afternoon sessions and as the first talk in the afternoon we have max in from core OS and he's going to tell us about his work of making the alert managers UI better for user experience and also developer experience thank you very much okay can everybody understand me just fine oh okay all right I'm gonna do a little bit crazy things today may be a little bit dangerous stuff today I'm gonna talk about the new hip javascript

### Excerpt da transcript

[Music] hi I'm Joyce I'm gonna guide you through the afternoon sessions and as the first talk in the afternoon we have max in from core OS and he's going to tell us about his work of making the alert managers UI better for user experience and also developer experience thank you very much okay can everybody understand me just fine oh okay all right I'm gonna do a little bit crazy things today may be a little bit dangerous stuff today I'm gonna talk about the new hip javascript framework at an OPS conference so let's let's see how this turns out please don't kill me or anything but let's just go through it and I think a lot of stuff is quite interesting for you and in the end you gotta pretty UI okay alright the more former title is improve user and developer experience of the alert mange UI so let's look at it um a maximum test engineer at Korres I've been working a lot with the Prometheus team and that's how I got involved in today to the project itself feel free to ask questions during the talk or afterwards or feel free to reach out to me as well okay so alert manager we want to talk about alert manager we heard a lot about alert ninja I'll go over it really quickly so what is the alert mentor the idea is that for meatiest scrapes of targets calexis data goes over that data something goes wrong it sends out alerts but it doesn't send that out wide rate but there's alert manager in between right here but we've seen this graphic I think four times now it's very very helpful okay so what does the lurk manage to do well first of all it deduplicate alerts it groups alerts it routes your alerts in the end and the one feature is you can silence alerts as well so these are the the main functionalities of alert mender but most of it and the primitives echo system is configured via config files so there's not a lot to do for the UI so what what do we actually want from the I well first of all I wanted display alerts it's the alert manager why not we want to do crud operations on silences and we want to see the status of the alert manager how is it configured and how's it doing at the moment so these are the basic things and that's that's all the UI it pretty much has to serve and here you see the old guy and that's exactly what the old UI have solved exactly these operations but we had a couple of problems with it well first of all we're missing some features like cool filtering and searching and grouping and in addition maybe a little bit better user experience s
