---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Maintainer Track"
themes: ["AI ML", "Security", "Kubernetes Core", "Community Governance"]
speakers: ["Mo Khan", "Microsoft", "Jordan Liggitt", "Google"]
sched_url: https://kccncna2023.sched.com/event/1R2tg/the-future-of-kubernetes-auth-and-policy-config-common-expression-language-mo-khan-microsoft-jordan-liggitt-google
youtube_search_url: https://www.youtube.com/results?search_query=The+Future+of+Kubernetes+Auth+and+Policy+Config%3A+Common+Expression+Language+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Future of Kubernetes Auth and Policy Config: Common Expression Language - Mo Khan, Microsoft & Jordan Liggitt, Google

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Kubernetes Core]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Mo Khan, Microsoft, Jordan Liggitt, Google
- Schedule: https://kccncna2023.sched.com/event/1R2tg/the-future-of-kubernetes-auth-and-policy-config-common-expression-language-mo-khan-microsoft-jordan-liggitt-google
- Busca YouTube: https://www.youtube.com/results?search_query=The+Future+of+Kubernetes+Auth+and+Policy+Config%3A+Common+Expression+Language+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Future of Kubernetes Auth and Policy Config: Common Expression Language.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2tg/the-future-of-kubernetes-auth-and-policy-config-common-expression-language-mo-khan-microsoft-jordan-liggitt-google
- YouTube search: https://www.youtube.com/results?search_query=The+Future+of+Kubernetes+Auth+and+Policy+Config%3A+Common+Expression+Language+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yOF9S_0TO3A
- YouTube title: The Future of Kubernetes Auth and Policy Config: Common Expression Langu... Mo Khan & Jordan Liggitt
- Match score: 0.949
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-future-of-kubernetes-auth-and-policy-config-common-expression-lang/yOF9S_0TO3A.txt
- Transcript chars: 27252
- Keywords: actually, cost, config, authorization, expressions, admission, object, access, server, authorizer, client, expression, requests, basically, schema, wanted, claims, policy

### Resumo baseado na transcript

all right can everybody hear me thank you all right let's get started so hey everyone this is the sigo Deep dive for cucon na 2023 uh so this year we're going to focus pretty heavily on cell and our usage of it in seot so I'm Mo from Microsoft I'm one of the leads for sigo I'm Jordan liot also lead for sigo from Google all right so we're going to mix it up this year so normally we wait till the end to do this but this year

### Excerpt da transcript

all right can everybody hear me thank you all right let's get started so hey everyone this is the sigo Deep dive for cucon na 2023 uh so this year we're going to focus pretty heavily on cell and our usage of it in seot so I'm Mo from Microsoft I'm one of the leads for sigo I'm Jordan liot also lead for sigo from Google all right so we're going to mix it up this year so normally we wait till the end to do this but this year we're going to do it at the beginning uh so I see Anish I see you in the audience there uh thank you very much for all your contributions this year uh to here I know you're not here hopefully you're watching this uh thank you also I don't think I saw James maybe if he's here uh but also thank you for your contributions NE I know you're not here but hopefully you'll watch this uh and say yeah so NE Brun I hope you were here I know you're here at the conference but uh thank you also for all the work you did uh Rita I know you're hopefully going to watch this afterwards and thank you for all your hard work and tting I know you're not here but we very much appreciate your contributions I'm gonna go over some of the stuff we did generically in um we won 129 before we sort of Deep dive more into the self stuff so there was like six High Lev things we worked on uh csv2 went GA and 129 so yay it's over um uh cluster trust bundle just landed in Alpha so like I know I see certain manager folks here I hope that they will adopt it at some point um we made some great improvements to bound service account tokens they contain node references as Alpha in v229 James helped with that uh uh We've made a bunch of improvements to aen and ID that we'll talk about in detail and we are continuing possibly the longest journey of any single thing which is the reduction of Secrets spased service account tokens all right so you've heard probably people in various sessions talking about cell uh what is it if you're unfamiliar with it it stands for common expression language um it's a non-touring complete language and it's designed to be pretty intuitive to read and write uh with a heavy focus on being able to bound execution time run quickly run in performance critical paths uh and be able to limit the amount of memory and CPU that's used um here's a just an example of what it might look like uh it's pretty natural syntax you sort of have dot accessors to to Fields um there's the ability to have macros or functions that the integrator provides to the expression so t
