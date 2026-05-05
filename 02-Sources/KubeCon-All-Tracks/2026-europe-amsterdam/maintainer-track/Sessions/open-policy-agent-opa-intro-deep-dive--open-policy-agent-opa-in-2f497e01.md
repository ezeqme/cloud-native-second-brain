---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Charlie Egan", "Anders Eknert", "Apple"]
sched_url: https://kccnceu2026.sched.com/event/2EF4m/open-policy-agent-opa-intro-deep-dive-charlie-egan-anders-eknert-apple
youtube_search_url: https://www.youtube.com/results?search_query=Open+Policy+Agent.+%28OPA%29+Intro+%26+Deep+Dive+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Open Policy Agent. (OPA) Intro & Deep Dive - Charlie Egan & Anders Eknert, Apple

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Charlie Egan, Anders Eknert, Apple
- Schedule: https://kccnceu2026.sched.com/event/2EF4m/open-policy-agent-opa-intro-deep-dive-charlie-egan-anders-eknert-apple
- Busca YouTube: https://www.youtube.com/results?search_query=Open+Policy+Agent.+%28OPA%29+Intro+%26+Deep+Dive+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Open Policy Agent. (OPA) Intro & Deep Dive.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EF4m/open-policy-agent-opa-intro-deep-dive-charlie-egan-anders-eknert-apple
- YouTube search: https://www.youtube.com/results?search_query=Open+Policy+Agent.+%28OPA%29+Intro+%26+Deep+Dive+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TENlj4r6IXk
- YouTube title: Open Policy Agent. (OPA) Intro & Deep Dive - Charlie Egan & Anders Eknert, Apple
- Match score: 0.772
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/open-policy-agent-opa-intro-deep-dive/TENlj4r6IXk.txt
- Transcript chars: 23681
- Keywords: policy, language, updates, policies, little, basically, languages, easier, examples, projects, express, advanced, please, feature, sprint, gatekeeper, source, recent

### Resumo baseado na transcript

So uh and I have been involved in the OPA project for for just as many years. And uh so I started out as an end user uh and eventually started contributing and uh for the past five six years I've been a maintainer of of Opa and a few adjacent projects. Uh, not just authorization, not just Kubernetes admission, not just controls around uh source uh source control and file updates, but uh one one policy language for all these different use cases. uh as well as producing audit logs about all of the decisions that have been made whether a user was allowed access or not or whether a resource was um you know denied from being created or not. So just a a quick little overview now about um some some data that we've we've learned about how people use the project and things that people are doing with it. Um this is uh noteworthy or it's noteworthy because uh often policy is a security uh some security code is not typically something that people do publish but of the policies that are being published uh a lot of people are sharing their oper code

### Excerpt da transcript

Awesome. We have a full house and some people were couldn't even make it in. The gatekeeper is effective. They'll have to watch online later. Yeah, thanks for coming everybody. It's um yeah, a privilege to have a full room. Um yeah, thanks for coming. Um so yeah, this is the open maintainer track. Uh this is uh going to be our update for for this event. Um uh first a few uh short little introductions about ourselves. I'll let you go first Anders. >> Yeah. Uh I'm sure many of you have seen me here before. This is my sixth or seventh CubeCon. So uh and I have been involved in the OPA project for for just as many years. Uh I started out with identity and access control. That kind of brought me into OPA. And uh so I started out as an end user uh and eventually started contributing and uh for the past five six years I've been a maintainer of of Opa and a few adjacent projects. >> Yeah. And so hello everybody. I'm Charlie. I first used Oper as a user in 2019 for a Kubernetes admission use case and have used it both in a a product uh since then as well.

I was working on a a product which did policy around X509 configuration in Kubernetes environments and um was enjoying using open and contributing to the project working with Anders and team. So I I joined uh joined Starra at the time at the end of 2022 and I've been a maintainer of the project since then as well. Uh so yeah I was also a user a user first. Um so hopefully it's a little bit of inspiration for some of you users if you're interested in getting involved in open source like being a user is a is a great place to get started with our project and all the projects here really. So yeah, um today we're going to talk about uh for those of you who are very new to OPER, a quick introduction about what our project is, what it does. Uh we're going to cover some updates from the community survey. Just quick show of hands. Did anybody complete the community survey we ran at the end of last year? One or two. Yeah, thank you. It's appreciated. Um and uh yeah, then we're going to go over some recent updates to the to the Rego language and some some changes that are upcoming as well as um yeah, other things that are next for our project.

So um so yeah, uh Opra's a general purpose policy engine. Uh you uh you might not know what that means. You may not be familiar with the idea of a general purpose policy engine. What can you do with a general purpose policy engine to begin with? uh you you haven't used one of them pe
