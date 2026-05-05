---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States"
event_id: kccncna2021
year: 2021
region: "North America"
city: "Los Angeles"
country: "United States"
event_date: "2021-10-11/2021-10-15"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Scott Nichols", "VMware"]
sched_url: https://kccncna2021.sched.com/event/lV9b/cloudevents-intro-status-and-the-future-scott-nichols-vmware
youtube_search_url: https://www.youtube.com/results?search_query=CloudEvents%3A+Intro%2C+Status+and+the+Future...+CNCF+KubeCon+2021
slides: []
status: parsed
---

# CloudEvents: Intro, Status and the Future... - Scott Nichols, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Scott Nichols, VMware
- Schedule: https://kccncna2021.sched.com/event/lV9b/cloudevents-intro-status-and-the-future-scott-nichols-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=CloudEvents%3A+Intro%2C+Status+and+the+Future...+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre CloudEvents: Intro, Status and the Future....

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV9b/cloudevents-intro-status-and-the-future-scott-nichols-vmware
- YouTube search: https://www.youtube.com/results?search_query=CloudEvents%3A+Intro%2C+Status+and+the+Future...+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=m1sT-BuA9WU
- YouTube title: CloudEvents: Intro, Status and the Future... - Scott Nichols, Chainguard
- Match score: 0.837
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloudevents-intro-status-and-the-future/m1sT-BuA9WU.txt
- Transcript chars: 18452
- Keywords: events, application, protocol, envelope, working, producer, interesting, consume, little, actually, consumer, mediator, github, write, payload, schema, serverless, update

### Resumo baseado na transcript

okay thank you for coming uh and delaying your lunch time by a little bit i'm sure uh the pesta will be better today um we're here to talk about cloud events i am part of the sig service sig serverless community and we are working on uh cloud events and this is the working group update so i'm i'm here on behalf of uh a bunch of people dedicating a lot of time to try to make cloud events and this these connecting bits better for cncf i am

### Excerpt da transcript

okay thank you for coming uh and delaying your lunch time by a little bit i'm sure uh the pesta will be better today um we're here to talk about cloud events i am part of the sig service sig serverless community and we are working on uh cloud events and this is the working group update so i'm i'm here on behalf of uh a bunch of people dedicating a lot of time to try to make cloud events and this these connecting bits better for cncf i am a co-founder of chainguard we are as of today at eight days old so there was some scheduled changes so yeah [Music] okay so we're gonna roll back the time a little bit to circa 2015 and if you think of a standard pub sub model application you have some sort of event producer and it was producing events maybe you have several of them that goes into some sort of event queue you might have a mediator that looks at the events and says well actually it's high priority or it's for production or it's for uh servicing uh the chain guard t-shirt sales and it goes to a specific channel and then you have some sort of event consumer which is your application that's hard-coded to consume those events in that particular shape and so the event mediator might have some complicated logic to inspect the packet and then route it to the correct spot and the serverless working group wrote a white paper thinking about well if we have this problem and we're thinking about the world in what's the future of serverless one of the issues is that we don't really have a way to talk about like there's no common language on the event itself is there all these interesting shapes and it'd be interesting if we could think about the world from higher order so well we'll break this problem down and we have some event producer which is likely third party you're probably going to you know check the boxes i want to get github action or github events or i want to get get lab events or i want to get other events from my application you have this custom necessary evil event mediator thing that is looking at those things and kind of shuffling it to the appropriate consumer of those events because you don't want the event producer to be tied directly to the event consumers right because then you're holding the event producer open and we what we really want to focus on as as a you know people writing code is the event per the event consumer code that wants to look at those events right so it'd be interesting if we could think if we could have enough data on the event
