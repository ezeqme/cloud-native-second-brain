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
themes: ["AI ML", "Community Governance"]
speakers: ["Manuel Ottlik", "HDI Global SE"]
sched_url: https://kccnceu2025.sched.com/event/1tcyi/beyond-cloudevents-endpoints-messages-schemas-cncf-xregistry-manuel-ottlik-hdi-global-se
youtube_search_url: https://www.youtube.com/results?search_query=Beyond+CloudEvents%3A+Endpoints%2C+Messages%2C+Schemas+%E2%80%93+CNCF+XRegistry+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Beyond CloudEvents: Endpoints, Messages, Schemas – CNCF XRegistry - Manuel Ottlik, HDI Global SE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Manuel Ottlik, HDI Global SE
- Schedule: https://kccnceu2025.sched.com/event/1tcyi/beyond-cloudevents-endpoints-messages-schemas-cncf-xregistry-manuel-ottlik-hdi-global-se
- Busca YouTube: https://www.youtube.com/results?search_query=Beyond+CloudEvents%3A+Endpoints%2C+Messages%2C+Schemas+%E2%80%93+CNCF+XRegistry+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Beyond CloudEvents: Endpoints, Messages, Schemas – CNCF XRegistry.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyi/beyond-cloudevents-endpoints-messages-schemas-cncf-xregistry-manuel-ottlik-hdi-global-se
- YouTube search: https://www.youtube.com/results?search_query=Beyond+CloudEvents%3A+Endpoints%2C+Messages%2C+Schemas+%E2%80%93+CNCF+XRegistry+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=M56SHzETAmM
- YouTube title: Beyond CloudEvents: Endpoints, Messages, Schemas – CNCF XRegistry - Manuel Ottlik, HDI Global SE
- Match score: 0.891
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/beyond-cloudevents-endpoints-messages-schemas-cncf-xregistry/M56SHzETAmM.txt
- Transcript chars: 25881
- Keywords: registry, events, schema, schemas, metadata, groups, business, actually, message, version, endpoints, server, basically, already, envelope, messages, letter, protocol

### Resumo baseado na transcript

So maintainer track always a little tricky one because you have a few people that have not heard of these projects ever before and want to get to know them as well as some veterans that know exactly what's going on and basically need the like nitty-gritty details of what changed. Um we will have an intro and explanation on cloud events as well as XX registry X registry a more deeper explanation since this is the newer project fairly unknown probably and I will try to make this more understandable with a demo. And what is still changing and where is there still a lot of evolvement is the extensions for this project and one would be CESQL cloud events structured query language and that is 1.0 zero know. So what you can now do is you can query for the event metadata and basically filter down on your events and K native is already using that. Um XR registry itself and its core specification does not have anything to do with event- driven architecture eventing or anything. And I will show you later in the demo what that could be because this is kind of abstract.

### Excerpt da transcript

cloud events and X registry. This is what we're going to talk about today. Uh so my name is Man Lotle. I'm a product owner for cloud native platforms at HDI Global. That's an insurance company in northern Germany. And I want to talk about cloud events registry. So maintainer track always a little tricky one because you have a few people that have not heard of these projects ever before and want to get to know them as well as some veterans that know exactly what's going on and basically need the like nitty-gritty details of what changed. So I will try to make both of you happy. Um we will have an intro and explanation on cloud events as well as XX registry X registry a more deeper explanation since this is the newer project fairly unknown probably and I will try to make this more understandable with a demo. So we're going to use a to-do list example and then I'm going to use the last five minutes to explain why an end user company might be interested. And finally I will share the project road map with you which a few people have been asking last year already and we have one to give in this talk.

Starting with cloud events. I will assume most of you have heard of cloud events already. It started in 2018 is graduated since last year shortly before CubeCon I think and it defines common metadata for events. So there are many diff different messaging and eventing protocols out there and even more event brokers and they have quite a few things in common but often differ in detail and it's a little bit like if you were to send a letter to a friend but depending on which postal service you use you have to write different things on the envelope. So this is where cloud events comes in. It is defining these common metadata and it defines protocol and broker independent headers. So what we are not do is we are not telling you how to write your letter. This is about what you write on the envelope. So it's not about a common event format but about common event data. And we have nine SDKs to do that. Six protocol bindings and this is what it actually looks like. So I just told you we're not telling you how to write your letter.

This is the envelope. This is an AMQP protocol binding. We have a few more uh six in total. We have Kafka as well. We have HTTP, MQTT. And you can see all the common meta data up there. And this is your letter. This is the one that you would be writing. Now, the nice thing when using this binary mode is that you do not have to do a breaking chang
