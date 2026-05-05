---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Doug Davis", "Microsoft"]
sched_url: https://kccncna2022.sched.com/event/182Ng/cloudevents-and-beyond-doug-davis-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=CloudEvents+And+Beyond%21+CNCF+KubeCon+2022
slides: []
status: parsed
---

# CloudEvents And Beyond! - Doug Davis, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Doug Davis, Microsoft
- Schedule: https://kccncna2022.sched.com/event/182Ng/cloudevents-and-beyond-doug-davis-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=CloudEvents+And+Beyond%21+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre CloudEvents And Beyond!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ng/cloudevents-and-beyond-doug-davis-microsoft
- YouTube search: https://www.youtube.com/results?search_query=CloudEvents+And+Beyond%21+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bJTUttZr-Ck
- YouTube title: CloudEvents And Beyond! - Doug Davis, Microsoft
- Match score: 0.757
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/cloudevents-and-beyond/bJTUttZr-Ck.txt
- Transcript chars: 36167
- Keywords: events, actually, schema, messages, message, little, endpoint, metadata, obviously, itself, format, particular, discovery, endpoints, probably, simple, producer, anything

### Resumo baseado na transcript

so okay Cloud events are everywhere now in a world where life is really easy where you have like one event producer like a tractor sending events to an event consumer and you know what the events look like life is actually really easy right because you know the producer is you know the transports the schema the format you know everything about it you really don't need anything special just send the message and you can process it life is easy however in a little bit more real world

### Excerpt da transcript

so okay Cloud events are everywhere now in a world where life is really easy where you have like one event producer like a tractor sending events to an event consumer and you know what the events look like life is actually really easy right because you know the producer is you know the transports the schema the format you know everything about it you really don't need anything special just send the message and you can process it life is easy however in a little bit more real world scenario you're probably going to have lots of different event producers all going through potentially some middleware either destined for one then consumer or potentially multiple event consumers or does additional middleware like Kafka kinda is with other things right in this world where you have varying formats schemas business logic events that look all different from each Source all going through the same middleware when you need to do basic processing of these events whether it's routing purposes or just some quick introspection about what the heck the event actually is it actually becomes really really difficult to do that in middleware because of the right of the wide range of all the different data in particular you in terms of extracting the data that really matters to you from the business logic you have to understand the schema the format of the message a whole bunch of information and that's really really complex and quite expensive especially if you have new types of events coming online quite frequently okay so what cloud events tries to do is something very very simple it just defines common metadata and where it appears in the message independent of the business logic okay so it's really there to help in the delivery of events from the producer to the consumer whether the consumer is your middleware the consumer is the ultimate recipient of the message it doesn't matter okay it's just there to help augment your messages so that you can do some basic processing without having to understand the business logic itself okay now it's very important to understand that cloud events is not defining a new common event format every now and then the industry says we're going to Define one event form after the rule them all and we don't need to worry about all this stuff anymore not realistic and that's not what we're trying to do okay we're trying to I'll show you in a second but we're there to help you with your current flows not try to rock your world okay so let's actuall
