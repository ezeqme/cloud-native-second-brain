---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Connectivity"
themes: ["Connectivity"]
speakers: ["Dave Protasowski"]
sched_url: https://kccncna2024.sched.com/event/1i7kV/all-your-routes-are-ready-more-or-less-dave-protasowski
youtube_search_url: https://www.youtube.com/results?search_query=All+Your+Routes+Are+Ready%2C+More+or+Less+CNCF+KubeCon+2024
slides: []
status: parsed
---

# All Your Routes Are Ready, More or Less - Dave Protasowski

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[Connectivity]]
- País/cidade: United States / Salt Lake City
- Speakers: Dave Protasowski
- Schedule: https://kccncna2024.sched.com/event/1i7kV/all-your-routes-are-ready-more-or-less-dave-protasowski
- Busca YouTube: https://www.youtube.com/results?search_query=All+Your+Routes+Are+Ready%2C+More+or+Less+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre All Your Routes Are Ready, More or Less.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7kV/all-your-routes-are-ready-more-or-less-dave-protasowski
- YouTube search: https://www.youtube.com/results?search_query=All+Your+Routes+Are+Ready%2C+More+or+Less+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6eMplLH3NIw
- YouTube title: All Your Routes Are Ready, More or Less - Dave Protasowski
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/all-your-routes-are-ready-more-or-less/6eMplLH3NIw.txt
- Transcript chars: 30572
- Keywords: gateway, traffic, essentially, actually, create, updates, native, provide, ingress, ideally, probing, interesting, envoy, update, little, status, contour, condition

### Resumo baseado na transcript

for some background I'm an engineer I work on the open source project K native this project has a bunch of subgroups uh which I'll kind of get into but I'm the lead for the serving I'm also on the steering committee um we had a Toc but we merged it we simplified our governance a little bit you can see my different handles I signed up for blue sky yesterday you can be my first follower so uh quick overview of ke native um there's a bunch of subgroups

### Excerpt da transcript

for some background I'm an engineer I work on the open source project K native this project has a bunch of subgroups uh which I'll kind of get into but I'm the lead for the serving I'm also on the steering committee um we had a Toc but we merged it we simplified our governance a little bit you can see my different handles I signed up for blue sky yesterday you can be my first follower so uh quick overview of ke native um there's a bunch of subgroups with it but um serving is sort of the one I'm involved in and it kind of does autoscaling your workloads uh to zero I'll cover a little bit more then you have a venting that lets you um kind of wire sources to these workloads and you don't need to use K native serving you can wire them up to uh deployments and things like that and we have a bunch of sources think of like some Pub sub Stuff Etc um that can you react on we have a CLI group um so you can interact everything using a CLI and then we also have this uh functions subgroup and what they try to do is just provide like a functional uh programming model that then runs on top of serving but you can use all these things together and build like a fast but you can use things separately so if I want to build functions and then run them on just anything I want I can do that because it just builds containers um if you just want to have a serving and not a venting you can so we kind of call it like a Voltron project project where you can use all these things independently but if you use it together you get some cool capabilities kind of like a platform uh so surveying in a little bit more detail you kind of offer a higher level abstraction of kubernetes entally we do all this network programming um you do revision management and things like that but essentially what you're doing is you're taking a container an image and then you'll get like a URL back that has uh certificates provisioned things like that and we can do traffic spinning and we do things like these automatic health checks so here's kind of like an example um this is we named it it's called service but it's actually a k native service so I'll just call it K service just to not confuse people this is kind of like all you need to Define so in my service I have a template spec you can see my image has like some function I can specify container Port I'm kind of highlighting like you can do traffic spitting but if you don't specify anything that traffic block it will just always route to the latest revisio
