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
speakers: ["Walter Fender", "Google", "Steven Wong", "VMware", "Nick Turner", "Amazon"]
sched_url: https://kccncna2021.sched.com/event/lV7E/cloud-provider-extraction-what-weve-done-where-we-are-and-whats-left-walter-fender-google-steven-wong-vmware-nick-turner-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Provider+Extraction%3A+What+We%E2%80%99ve+Done%2C+Where+We+Are+and+What%27s+Left%21+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Cloud Provider Extraction: What We’ve Done, Where We Are and What's Left! - Walter Fender, Google; Steven Wong, VMware; Nick Turner, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2021 - Los Angeles, United States
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United States / Los Angeles
- Speakers: Walter Fender, Google, Steven Wong, VMware, Nick Turner, Amazon
- Schedule: https://kccncna2021.sched.com/event/lV7E/cloud-provider-extraction-what-weve-done-where-we-are-and-whats-left-walter-fender-google-steven-wong-vmware-nick-turner-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Provider+Extraction%3A+What+We%E2%80%99ve+Done%2C+Where+We+Are+and+What%27s+Left%21+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Cloud Provider Extraction: What We’ve Done, Where We Are and What's Left!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2021.sched.com/event/lV7E/cloud-provider-extraction-what-weve-done-where-we-are-and-whats-left-walter-fender-google-steven-wong-vmware-nick-turner-amazon
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Provider+Extraction%3A+What+We%E2%80%99ve+Done%2C+Where+We+Are+and+What%27s+Left%21+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ogLedHIERaA
- YouTube title: Cloud Provider Extraction: What We’ve Done, Where We Are and What's Left- W Fender, S Wong, N Turner
- Match score: 0.925
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/cloud-provider-extraction-what-weve-done-where-we-are-and-whats-left/ogLedHIERaA.txt
- Transcript chars: 27213
- Keywords: provider, controller, actually, manager, release, providers, connectivity, cubelet, credential, vsphere, google, feature, migration, server, cluster, working, effort, little

### Resumo baseado na transcript

hi uh welcome to kubecon 2021 in los angeles you're about to get updates from a bunch of people who work on the kubernetes cloud provider i'm steve wong with vmware and i'm joined by walter fender of google and nick turner of amazon we also have people representing many other popular cloud providers who couldn't be with us here physically but who graciously prepared lightning talk recordings or slides which we'll be sharing in the middle of this uh talk if you're wondering about the cloud suit of course getting the cloud provider abstraction the reference implementation for microsoft so that any of you can go and look how to bring up a kubernetes cluster on microsoft and get it all working um they've had multiple plot uh patch releases and they actually have

### Excerpt da transcript

hi uh welcome to kubecon 2021 in los angeles you're about to get updates from a bunch of people who work on the kubernetes cloud provider i'm steve wong with vmware and i'm joined by walter fender of google and nick turner of amazon we also have people representing many other popular cloud providers who couldn't be with us here physically but who graciously prepared lightning talk recordings or slides which we'll be sharing in the middle of this uh talk if you're wondering about the cloud suit of course it's sig cloud provider but it's just a demonstration that in spite of uh walter's rule with an iron fist as a co-chair we do have some fun and levity in the group so come to meetings and enjoy yourself the way we'll start out is i'll i'll quickly explain what a cloud provider is about just in case anybody here wandered in and isn't familiar with the kubernetes architecture and then we'll move on to a background on our strategic mission to move the cloud provider specific code out of the main kubernetes source tree then nick's going to give a general status followed by cloud the cloud provider specific lightning talks and then finally walter will close covering roadmap interesting topics and how you can get involved with the group so the cloud provider what is it well this is the uh part of the architecture that allows kubernetes apps to be portable across various public and on-prem clouds the goal is to allow a well-written app to run anywhere and for the most part not even able to tell where it's running sig cloud provider works closely with a few other sigs to make this happen for example most of the related abstraction is actually done by sig storage but there are cross-sig integration efforts and design reviews that go into this uh the effort in play now is moving out a tree when in the early days kubernetes was a monolith when it came to cloud providers the kubernetes binary included a bunch of cloud providers and it was bigger than it needed to be this had a number of sub-optimal aspects listed here for example a user investigating the startup logs running on google cloud might see a startup log entry saying could not find aws hyphen ecb the old model also slowed time to feature in patch delivery and we've been moving to out of tree cloud providers for a while new deployments are probably already using the out of tree now if they're picking up distros but anybody still on legacy deployments needs to be planning for migration and nick is going to tell
