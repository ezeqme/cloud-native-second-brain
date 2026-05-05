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
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Evan Gilman", "VMware"]
sched_url: https://kccncna2022.sched.com/event/19QI3/dont-mind-the-gap-securely-accessing-cloud-resources-from-anywhere-with-spiffespire-evan-gilman-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Don%27t+Mind+the+Gap%3A+Securely+Accessing+Cloud+Resources+From+Anywhere+With+SPIFFE%2FSPIRE+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Don't Mind the Gap: Securely Accessing Cloud Resources From Anywhere With SPIFFE/SPIRE - Evan Gilman, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Detroit
- Speakers: Evan Gilman, VMware
- Schedule: https://kccncna2022.sched.com/event/19QI3/dont-mind-the-gap-securely-accessing-cloud-resources-from-anywhere-with-spiffespire-evan-gilman-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Don%27t+Mind+the+Gap%3A+Securely+Accessing+Cloud+Resources+From+Anywhere+With+SPIFFE%2FSPIRE+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Don't Mind the Gap: Securely Accessing Cloud Resources From Anywhere With SPIFFE/SPIRE.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/19QI3/dont-mind-the-gap-securely-accessing-cloud-resources-from-anywhere-with-spiffespire-evan-gilman-vmware
- YouTube search: https://www.youtube.com/results?search_query=Don%27t+Mind+the+Gap%3A+Securely+Accessing+Cloud+Resources+From+Anywhere+With+SPIFFE%2FSPIRE+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=PtYluGzPvGo
- YouTube title: Don't Mind the Gap: Securely Accessing Cloud Resources From Anywhere With SPIFFE/SPIRE - Evan Gilman
- Match score: 1.013
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/dont-mind-the-gap-securely-accessing-cloud-resources-from-anywhere-wit/PtYluGzPvGo.txt
- Transcript chars: 29832
- Keywords: spiffy, domain, workload, identity, server, provider, little, bundle, aspire, identities, similar, registration, running, utility, supports, domains, software, google

### Resumo baseado na transcript

hello hello everybody officially day number one I guess day plus one or two if you've been to some of the co-located events thank you for coming I'm Evan Gilman I'm a maintainer on uh spiffy inspired projects both I've been on those projects for uh since they were started I guess as for five and a half years maybe or so in 2017.

### Excerpt da transcript

hello hello everybody officially day number one I guess day plus one or two if you've been to some of the co-located events thank you for coming I'm Evan Gilman I'm a maintainer on uh spiffy inspired projects both I've been on those projects for uh since they were started I guess as for five and a half years maybe or so in 2017. and um title of the talk today is don't mind the gap we're going to be talking predominantly about how to use spit the identities to authenticate to third-party resources um specifically to the three major Cloud providers there's a few tricks up our sleeve we can talk about others have kind of clued into the trick over the last year or two um which some of you may have noticed I'm trying to keep this talk as casual as possible I've got 20 slides it's been around 20 minutes if folks have questions anything like that please feel free to raise your hand in the middle of the talk I'm happy to kind of stop and answer your questions make it personal I've got a mic up here there's a mic back there or we can shout or we'll figure it out um so we'll talk first about the spiffy Basics kind of we won't go over all of spiffy but we'll go over the things that are important to understand for the content in this in this presentation um similar thing for aspire cover kind of at a high level some of the important things that you'll you'll need to kind of make sense of the rest of the talk and then I'll step through kind of like three examples of how to do this AWS Azure and gcp they're all kind of um they all leverage kind of the same underlying technology but you know have their little quirks and differences here and there kind of thing and then finally we'll have hopefully plenty of time at the end for Q a uh if nobody raises their hand during my presentation which I hope they do so without further ado you can dive on oops wrong one spiffy basics the first thing to know about spiffy is a spiffy ID and I apologize I some people here tend to be newcomers some people tend to not be so bear with me the spiffy ideas kind of what it sounds like it's basically like a username for workloads and specifically deals with workload identity this is kind of like the core thing and as you can see here it's it's like a structured string is structured as a URI it is compatible with 3986 or whatever that your irfc is it does have some like additional limitations placed on top of that and to constrain so there's a lot of stuff in that RFC if you spend adequate amou
