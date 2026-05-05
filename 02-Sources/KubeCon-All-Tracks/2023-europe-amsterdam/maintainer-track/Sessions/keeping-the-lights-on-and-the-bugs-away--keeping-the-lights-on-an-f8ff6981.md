---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Patrick Ohly", "Intel"]
sched_url: https://kccnceu2023.sched.com/event/1Hzcr/keeping-the-lights-on-and-the-bugs-away-patrick-ohly-intel
youtube_search_url: https://www.youtube.com/results?search_query=Keeping+the+Lights+on+and+the+Bugs+Away+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Keeping the Lights on and the Bugs Away - Patrick Ohly, Intel

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Patrick Ohly, Intel
- Schedule: https://kccnceu2023.sched.com/event/1Hzcr/keeping-the-lights-on-and-the-bugs-away-patrick-ohly-intel
- Busca YouTube: https://www.youtube.com/results?search_query=Keeping+the+Lights+on+and+the+Bugs+Away+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Keeping the Lights on and the Bugs Away.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hzcr/keeping-the-lights-on-and-the-bugs-away-patrick-ohly-intel
- YouTube search: https://www.youtube.com/results?search_query=Keeping+the+Lights+on+and+the+Bugs+Away+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7rJUcEC7H0s
- YouTube title: Keeping the Lights on and the Bugs Away - Patrick Ohly, Intel
- Match score: 0.884
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/keeping-the-lights-on-and-the-bugs-away/7rJUcEC7H0s.txt
- Transcript chars: 30162
- Keywords: framework, testing, better, ginkgo, useful, failure, end-to-end, perhaps, basically, helper, context, cleanup, waiting, message, expect, another, function, probably

### Resumo baseado na transcript

I think it's 25 past I I believe it's the last session of this conference today so let's get started you're all probably eager to get to the booth crawl but first let's talk about the sick testing update of this year's kubecon my name is Patrick Uli I work on kubernetes for Intel on various topics including testing end-to-end testing in particular and I recently became a tech lead for that particular area in sick testing we do have other experts where suggesting is a fairly big seek but

### Excerpt da transcript

I think it's 25 past I I believe it's the last session of this conference today so let's get started you're all probably eager to get to the booth crawl but first let's talk about the sick testing update of this year's kubecon my name is Patrick Uli I work on kubernetes for Intel on various topics including testing end-to-end testing in particular and I recently became a tech lead for that particular area in sick testing we do have other experts where suggesting is a fairly big seek but owns a lot of code but I'm the one who has done most of the work on end-to-end testing and therefore I got the honor to talk about that today usually in these sick updates someone goes through all the things that the Sikh has done to inform the community but I figured that with a lot of things Landing very reasonably in end-to-end testing with I'll focus on just that aspect and make it hopefully interesting for you guys because that is also something that everyone who touches kubernetes sooner or later needs to deal with whether it's develop upping features or debugging perhaps something or writing your own code and trying to figure out how to test that with a new kubernetes cluster that is where we're end-to-end testing becomes useful and is needed but Zig testing as I said is a big Sig that is really crucial to kubernetes we officially own several tools that really keep the lights on in kubernetes these other tools brow for testing tied for merging code that has approvals all of that are crucial tools that keep the high velocity of changes of going into that are going into kubernetes is alive and keeping the project healthy is part of that too we own some tools that do analysis we also help other six to develop their tests but a common misconception is that sick testing is not itself responsible for those tests we just provide some infrastructure and then we expect and hope that the other six will use those responsibly do the right things and and write good tests because good tests are part of that thing that keeps kubernetes healthy we run those all mini tests run on all PRS they need to pass reliably so flaky tests are probably one of the biggest problems that we are dealing with in kubernetes when merging changes because the flaky test not only affects that thing but is not getting tested properly it also affects any other PR that doesn't go in immediately because some proud job failed temporarily that is a big problem that we still struggle with and some of the tints
