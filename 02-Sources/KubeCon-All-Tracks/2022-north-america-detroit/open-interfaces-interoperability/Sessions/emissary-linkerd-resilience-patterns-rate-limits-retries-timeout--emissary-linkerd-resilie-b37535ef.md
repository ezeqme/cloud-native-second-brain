---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Open Interfaces + Interoperability"
themes: ["SRE Reliability"]
speakers: ["Flynn", "Buoyant", "Daniel Bryant", "Ambassador Labs"]
sched_url: https://kccncna2022.sched.com/event/182Ie/emissary-+-linkerd-resilience-patterns-rate-limits-retries-timeouts-flynn-buoyant-daniel-bryant-ambassador-labs
youtube_search_url: https://www.youtube.com/results?search_query=Emissary+%2B+Linkerd+Resilience+Patterns%3A+Rate+Limits%2C+Retries+%26+Timeouts+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Emissary + Linkerd Resilience Patterns: Rate Limits, Retries & Timeouts - Flynn, Buoyant & Daniel Bryant, Ambassador Labs

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Open Interfaces + Interoperability]]
- Temas: [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Flynn, Buoyant, Daniel Bryant, Ambassador Labs
- Schedule: https://kccncna2022.sched.com/event/182Ie/emissary-+-linkerd-resilience-patterns-rate-limits-retries-timeouts-flynn-buoyant-daniel-bryant-ambassador-labs
- Busca YouTube: https://www.youtube.com/results?search_query=Emissary+%2B+Linkerd+Resilience+Patterns%3A+Rate+Limits%2C+Retries+%26+Timeouts+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Emissary + Linkerd Resilience Patterns: Rate Limits, Retries & Timeouts.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182Ie/emissary-+-linkerd-resilience-patterns-rate-limits-retries-timeouts-flynn-buoyant-daniel-bryant-ambassador-labs
- YouTube search: https://www.youtube.com/results?search_query=Emissary+%2B+Linkerd+Resilience+Patterns%3A+Rate+Limits%2C+Retries+%26+Timeouts+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=hOGPz1DJqb8
- YouTube title: Emissary + Linkerd Resilience Patterns: Rate Limits, Retries & Timeouts - Flynn & Daniel Bryant
- Match score: 0.947
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/emissary-linkerd-resilience-patterns-rate-limits-retries-timeouts/hOGPz1DJqb8.txt
- Transcript chars: 35662
- Keywords: emissary, timeouts, actually, always, retries, mesh, application, probably, ingress, linker, traffic, little, smiley, resilience, limits, limiting, gateway, question

### Resumo baseado na transcript

just as expectations is a sort of 101 level talk okay we're not going to go super deep into some of the patterns we're not going to go super deep into some of the config but hopefully you walk away with a good understanding of resilience good understanding of reliability and then you've got some tips and tricks that you can use with Linker D and with Emissary Ingress as well and also a good understanding of what each of these things actually brings to the table what rate limits yeah so it's battle tested right that's one of the things like you know there's many Serene dresses out there but this is Battle tested it's used massive scale at various different companies and it's Envoy powered under the hood so we all know in service right we've also got Mark here going through to backend service from a security perspective we might want to stop that we might have some auth in place right that has to stop that happening or the X might actually represent something breaking within

### Excerpt da transcript

just as expectations is a sort of 101 level talk okay we're not going to go super deep into some of the patterns we're not going to go super deep into some of the config but hopefully you walk away with a good understanding of resilience good understanding of reliability and then you've got some tips and tricks that you can use with Linker D and with Emissary Ingress as well and also a good understanding of what each of these things actually brings to the table what rate limits can accomplish what Retros accomplish Etc et cetera perfect I'm Daniel this is Flynn we have worked together for five plus years there were different companies and communities and so forth they're very active in the open source Community love to get involved in the twitters you can jump on our respective slacks engage with us as well you know don't you feel free to come up just the end of the talk but don't worry you can always engage this online as well I'm always happy to chat afterwards it's also worth pointing out for those of you who might know me from the past the uh that at buoyant that is not a typo I am at brilliant now not an ambassador fantastic so resilience when I always like to think about the you know why are we doing this stuff right I'm a technologist you know Java programmed by heart and by background um but I always like to think why are we thinking about a thing why should we care about reliability why should we care about resilience right the user wants that reliable end-to-end experience but they don't really want to know about the the details right they just want the web app to work they want to get a good you know good user experience right you've got to handle north south and East-West traffic when you're dealing with microservices back in my Java monolith days North South traffic coming from the user to the monolith Happy Days right as we've split up to microservices I started to get Ruby but it'd go all these other things suddenly I was implementing libraries to manage all the comms between the services we've pulled that out things like observability security and resilience within the application now can be done via a service mesh East-West so gotta think now north south east west as we'll demonstrate as Lynn will demonstrate the patterns do differ whether you're at the edge or within the mesh so some little gotchas little takeaways will go through there and despite what you're hearing at the conference devops is not dead right um and self-service is requi
