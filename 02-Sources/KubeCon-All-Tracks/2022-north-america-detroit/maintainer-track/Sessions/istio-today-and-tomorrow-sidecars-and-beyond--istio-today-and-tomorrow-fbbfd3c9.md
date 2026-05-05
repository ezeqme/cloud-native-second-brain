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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Mitch Conners", "Google", "Lin Sun", "Solo.io"]
sched_url: https://kccncna2022.sched.com/event/1BvZ8/istio-today-and-tomorrow-sidecars-and-beyond-mitch-conners-google-lin-sun-soloio
youtube_search_url: https://www.youtube.com/results?search_query=Istio+Today+and+Tomorrow%3A+Sidecars+and+Beyond+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Istio Today and Tomorrow: Sidecars and Beyond - Mitch Conners, Google & Lin Sun, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Mitch Conners, Google, Lin Sun, Solo.io
- Schedule: https://kccncna2022.sched.com/event/1BvZ8/istio-today-and-tomorrow-sidecars-and-beyond-mitch-conners-google-lin-sun-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=Istio+Today+and+Tomorrow%3A+Sidecars+and+Beyond+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Istio Today and Tomorrow: Sidecars and Beyond.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/1BvZ8/istio-today-and-tomorrow-sidecars-and-beyond-mitch-conners-google-lin-sun-soloio
- YouTube search: https://www.youtube.com/results?search_query=Istio+Today+and+Tomorrow%3A+Sidecars+and+Beyond+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=bKNngrE4cc8
- YouTube title: Istio Today and Tomorrow: Sidecars and Beyond - Mitch Conners, Google & Lin Sun, Solo.io
- Match score: 0.784
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/istio-today-and-tomorrow-sidecars-and-beyond/bKNngrE4cc8.txt
- Transcript chars: 33540
- Keywords: ambient, application, waypoint, mesh, tunnel, traffic, actually, single, production, believe, container, control, running, processing, tendency, working, question, little

### Resumo baseado na transcript

here we're going to talk about ISO where ISO is today and where ISO is headed tomorrow super super excited to be here with Mitch Connor so if you allow me to quickly introduce myself I got you thank you Mitch uh yeah my name is lensa I'm working on open source at solo prior to join solo I was a senior technical staff member at IBM I wrote two books about Isel one is is still explained how many of you uh actually read that book before all right and what are the security tradeoff between EO ambient service mesh to cyos um so that's super exciting so we launched that I believe on September 7th so we tweeted out that I actually tweeted for the iso project and what's also really reassuring to us Matt Klein who is a founder of arvoy and uh really Endor the architecture we put out for Isel regarding this new site this architecture for ambient so that's really really cool so today I want to take you through a quick overview of

### Excerpt da transcript

here we're going to talk about ISO where ISO is today and where ISO is headed tomorrow super super excited to be here with Mitch Connor so if you allow me to quickly introduce myself I got you thank you Mitch uh yeah my name is lensa I'm working on open source at solo prior to join solo I was a senior technical staff member at IBM I wrote two books about Isel one is is still explained how many of you uh actually read that book before all right a few of you and I just published a new book ISO ambient explained uh so very excited about that I work in the iso steering committee and Technical oversight committee yeah now I'm going to pass on to Mitch hey everybody I think I've met a lot of you my name is I'm a software engineer at Google I joined the sto project way back in 201 18 and I'm very fortunate to serve on the TOC today uh I hold the dubious distinction of having the largest handcrafted commit in the IST or in any ISO repository not sure that's something I should be bragging about in my defense most of those lines are deletes rather than additions so it's not as bad as it looks uh I also had the privilege of being a guest on the kubernetes podcast check out episode 177 to hear about ISO just from a few months back uh especially with an ex the exciting announcement of the donation to cncf and a few other things so we said we were going to talk about ISO today and tomorrow and I'm going to cover mostly the today SE I'm going to use the keyboard uh how many of you guys are actively using a service mesh in production today all right wow okay and if you're not how about how many of you are evaluating service mes us usage cool and if you're not doing either of those you probably are in the wrong room but you're welcome to stick around we're happy you're here uh service Mass usage is a really really taking off worldwide and the cncf survey from 2021 showed that there's a shift into production that we're seeing you know for the last five years or so it was a very exciting topic everybody was talking about it but it wasn't really making its way into production so we've sort of crossed that Gap and are moving on towards maturity in the industry as a whole Ando is no different um we have a great Community behind Theo project that I'm very proud of we have 397 community members and that's growing every day it's actually I wrote that last week so we probably have a few more already we've got 50 maintainers seven working groups with 15 leads in the last 28 days the
