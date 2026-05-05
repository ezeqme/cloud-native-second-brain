---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Observability", "Storage Data", "Community Governance"]
speakers: ["Alolita Sharma", "Apple", "Pereira Braga", "Google", "Chris Larsen", "Netflix"]
sched_url: https://kccnceu2025.sched.com/event/1tcyx/from-the-observability-tag-designing-a-common-query-language-for-observability-data-alolita-sharma-apple-pereira-braga-google-chris-larsen-netflix
youtube_search_url: https://www.youtube.com/results?search_query=From+the+Observability+TAG%3A+Designing+a+Common+Query+Language+for+Observability+Data+CNCF+KubeCon+2025
slides: []
status: parsed
---

# From the Observability TAG: Designing a Common Query Language for Observability Data - Alolita Sharma, Apple; Pereira Braga, Google; Chris Larsen, Netflix

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Observability]], [[Storage Data]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Alolita Sharma, Apple, Pereira Braga, Google, Chris Larsen, Netflix
- Schedule: https://kccnceu2025.sched.com/event/1tcyx/from-the-observability-tag-designing-a-common-query-language-for-observability-data-alolita-sharma-apple-pereira-braga-google-chris-larsen-netflix
- Busca YouTube: https://www.youtube.com/results?search_query=From+the+Observability+TAG%3A+Designing+a+Common+Query+Language+for+Observability+Data+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre From the Observability TAG: Designing a Common Query Language for Observability Data.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyx/from-the-observability-tag-designing-a-common-query-language-for-observability-data-alolita-sharma-apple-pereira-braga-google-chris-larsen-netflix
- YouTube search: https://www.youtube.com/results?search_query=From+the+Observability+TAG%3A+Designing+a+Common+Query+Language+for+Observability+Data+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=1iWD14xvBQA
- YouTube title: From the Observability TAG: Designing a Common Query... lolita Sharma, Pereira Braga & Chris Larsen
- Match score: 0.766
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/from-the-observability-tag-designing-a-common-query-language-for-obser/1iWD14xvBQA.txt
- Transcript chars: 29255
- Keywords: observability, language, google, across, syntax, metrics, support, actually, understand, developers, common, logs, course, specific, context, company, traces, events

### Resumo baseado na transcript

Uh very nice to see you all and uh hope you're enjoying the sunny weather in London as we are all you know sitting inside in the rooms but this should be an interesting session today. Um again you know we are um from the observability uh tag and we've been um we'll kind of go through you know our work and uh some a case study from Google uh on uh designing an observability language. we have traces we have logs we have profiles events you know client events um as well as errors failures all kinds of exceptions that are uh considered to measurable you know observable and really tell us a lot about the system uh that we The other the so the other part that I wanted to call out here as focus of the session is that again we want to present on the research that you know the observability tag has been doing as part of the query language specification workg group uh on building an specification for open observability query semantic definitions right common definitions that are used across the industry uh and Chris will be talking a bit about that and Then of course Google who you know as a uh diving in So just to be clear again making sure that you know people don't get confused and us especially uh it's uh metrics and telemetry will be used interchangeably especially by Pereira because you know uh uh in the larger observability open source observability world we

### Excerpt da transcript

So good morning everybody. Uh very nice to see you all and uh hope you're enjoying the sunny weather in London as we are all you know sitting inside in the rooms but this should be an interesting session today. Um again you know we are um from the observability uh tag and we've been um we'll kind of go through you know our work and uh some a case study from Google uh on uh designing an observability language. So with that said let's get started. Um I'm Alolita Sharma from Apple. I lead observability engineering and I'm also uh co-chair on the uh tag for observability. Um I have Chris Larson who is also an observability engineer uh and my fellow um colleague in the work group that we have in the tag for um query standardization specification. Um and we also have Pereira from Google uh who is um a uh observability steward at Google and has been working with uh internal teams at Google to be able to uh look at you know how observability is being used by different user groups uh developers and others across the company.

and we'll be talking a bit more about you know some of the research that they have done within their org. So with that said um let's get started. Uh so the focus of this session today is really to um not you know really be prescriptive about a query language. Right? That's not the objective of this discussion. It really is that hey you know how do we propose a recommended recommended way of commonly you know using a common query method to be able to query all kinds of data right because again as you know in observability data we have metrics we have traces we have logs we have profiles events you know client events um as well as errors failures all kinds of exceptions that are uh considered to measurable you know observable and really tell us a lot about the system uh that we are trying to manage. So with that said, you know, I mean again as an enduser or any kind of user, how do you actually um look at that data end to end? The other the so the other part that I wanted to call out here as focus of the session is that again we want to present on the research that you know the observability tag has been doing as part of the query language specification workg group uh on building an specification for open observability query semantic definitions right common definitions that are used across the industry uh and Chris will be talking a bit about that and Then of course Google who you know as a uh diving in into the open- source uh SQL extensions t
