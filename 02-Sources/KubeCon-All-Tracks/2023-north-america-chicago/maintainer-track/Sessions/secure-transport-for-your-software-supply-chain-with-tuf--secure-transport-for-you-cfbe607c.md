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
themes: ["AI ML", "Security", "Storage Data", "Community Governance"]
speakers: ["Marina Moore", "New York University", "Trishank Kuppusamy", "Datadog"]
sched_url: https://kccncna2023.sched.com/event/1R2rM/secure-transport-for-your-software-supply-chain-with-tuf-marina-moore-new-york-university-trishank-kuppusamy-datadog
youtube_search_url: https://www.youtube.com/results?search_query=Secure+Transport+for+Your+Software+Supply+Chain+with+TUF+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Secure Transport for Your Software Supply Chain with TUF - Marina Moore, New York University & Trishank Kuppusamy, Datadog

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Storage Data]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Marina Moore, New York University, Trishank Kuppusamy, Datadog
- Schedule: https://kccncna2023.sched.com/event/1R2rM/secure-transport-for-your-software-supply-chain-with-tuf-marina-moore-new-york-university-trishank-kuppusamy-datadog
- Busca YouTube: https://www.youtube.com/results?search_query=Secure+Transport+for+Your+Software+Supply+Chain+with+TUF+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Secure Transport for Your Software Supply Chain with TUF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2rM/secure-transport-for-your-software-supply-chain-with-tuf-marina-moore-new-york-university-trishank-kuppusamy-datadog
- YouTube search: https://www.youtube.com/results?search_query=Secure+Transport+for+Your+Software+Supply+Chain+with+TUF+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=CnxODYi-GEE
- YouTube title: Secure Transport for Your Software Supply Chain with TUF - Marina Moore & Trishank Kuppusamy
- Match score: 0.858
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/secure-transport-for-your-software-supply-chain-with-tuf/CnxODYi-GEE.txt
- Transcript chars: 31540
- Keywords: software, metadata, secure, actually, version, supply, packages, called, security, source, change, signed, reposter, marina, securely, signature, snapshot, details

### Resumo baseado na transcript

all right hello everybody I'm Marina Moore I'm a PhD candidate at NYU and I've been a maintainer of the tough project for the past five years or so um and this is my colleague trank hello trishan k ksami um staff security engineer at data dog have been involved with t in various capacities since my research on it at NYU and now using it a data dog to secure some of our own products Marina please yeah and we're going to talk today about um secure transport for this is all currently up to date this is our very fast overview of tough um and hopefully that's enough to get started um we can learn more about some of the details of this as we go the tough project is this one specification

### Excerpt da transcript

all right hello everybody I'm Marina Moore I'm a PhD candidate at NYU and I've been a maintainer of the tough project for the past five years or so um and this is my colleague trank hello trishan k ksami um staff security engineer at data dog have been involved with t in various capacities since my research on it at NYU and now using it a data dog to secure some of our own products Marina please yeah and we're going to talk today about um secure transport for your software supply chain with tough so we'll talk a bit about what tough is and then um some various case studies about how it can be used to um secure transport of different different elements in the software supply chain first of all I'll start with a quick definition of what a uh supply chain is just so that we're all on the same page a software Supply Chain by this definition is a collection of systems devices and people which produce a final software product and there's an example here of kind of the different steps that happen in a software supply chain things from um source code to testing to building to then deployment of of that code and there can be other steps um in the chain as well there have been a number of attacks on Supply chains in recent years unfortunately um just to to motivate the problem here are a few examples everything from dependencies to um repositories themselves to source code um being attacked these are just from the past couple years I won't go into detail about all of them um and at the bottom of this slide I do have a link to the um tag security catalog of supply chain compromises where these came from and which have a lot more detail for folks who are curious um the main point is this is a an area that attackers have discovered and so we want to make sure that we also are protecting it um and today in this talk we're not going to focus on the whole thing we're going to focus really on this last step once since you already have an a image that is built you have a packaged piece of software um how do you then distribute that securely to the person who's going to run it and our threat model for this um for this for this talk is um attackers who can access a couple different pieces of the system they can perform a man in the- Middle attack that on the network which means they can read the traffic alter the traffic between the repository and the user uh they can compromise Keys used design updates so the keys themselves um they can get lost computers can get stolen all
