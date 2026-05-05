---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands"
event_id: kccnceu2023
year: 2023
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2023-04-17/2023-04-21"
track: "Security + Identity"
themes: ["Security", "Kubernetes Core"]
speakers: ["Daniele de Araujo dos Santos", "Shane Lawrence", "Shopify"]
sched_url: https://kccnceu2023.sched.com/event/1Hyb5/prevent-embarrassing-cluster-takeovers-with-this-one-simple-trick-daniele-de-araujo-dos-santos-shane-lawrence-shopify
youtube_search_url: https://www.youtube.com/results?search_query=Prevent+Embarrassing+Cluster+Takeovers+with+This+One+Simple+Trick%21+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Prevent Embarrassing Cluster Takeovers with This One Simple Trick! - Daniele de Araujo dos Santos & Shane Lawrence, Shopify

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2023 - Amsterdam, Netherlands
- Trilha oficial: [[Security + Identity]]
- Temas: [[Security]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Daniele de Araujo dos Santos, Shane Lawrence, Shopify
- Schedule: https://kccnceu2023.sched.com/event/1Hyb5/prevent-embarrassing-cluster-takeovers-with-this-one-simple-trick-daniele-de-araujo-dos-santos-shane-lawrence-shopify
- Busca YouTube: https://www.youtube.com/results?search_query=Prevent+Embarrassing+Cluster+Takeovers+with+This+One+Simple+Trick%21+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Prevent Embarrassing Cluster Takeovers with This One Simple Trick!.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2023.sched.com/event/1Hyb5/prevent-embarrassing-cluster-takeovers-with-this-one-simple-trick-daniele-de-araujo-dos-santos-shane-lawrence-shopify
- YouTube search: https://www.youtube.com/results?search_query=Prevent+Embarrassing+Cluster+Takeovers+with+This+One+Simple+Trick%21+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=RKhtRMoIvtw
- YouTube title: Prevent Embarrassing Cluster Takeovers with This One Simple Trick! - Daniele Santos & Shane Lawrence
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/prevent-embarrassing-cluster-takeovers-with-this-one-simple-trick/RKhtRMoIvtw.txt
- Transcript chars: 33735
- Keywords: security, running, container, privileges, containers, workloads, attacker, shopify, attack, secure, workload, actually, kubota, default, access, course, developers, github

### Resumo baseado na transcript

uh welcome to my snake oil sales pitch I hope you're excited to have a chance to purchase an easy cure for all of your security woes if you call right now then I'll throw in an instant service mesh just Add Water I want to know who here knows pretty much all of the kubernetes security settings that are on by default and also which ones are needed by all of your applications and please keep your hand up if you've never copied and pasted from one manifest to not easy to get this right every single time at scale and we discovered this uh pretty early on I think in 2017 we saw that we were going to need some automation for this we saw that we were going to need some rigorous

### Excerpt da transcript

uh welcome to my snake oil sales pitch I hope you're excited to have a chance to purchase an easy cure for all of your security woes if you call right now then I'll throw in an instant service mesh just Add Water I want to know who here knows pretty much all of the kubernetes security settings that are on by default and also which ones are needed by all of your applications and please keep your hand up if you've never copied and pasted from one manifest to another uh never made a mistake in a yaml file and nobody except you has access to Creator modify workloads uh it's just me and I'm lying so I have nothing to teach you if you've still got your hand up but for everybody else let's go look for some foot guns um that's me also me I've been breaking systems since I was a kid and my professional experience in Security started in the military doing intrusion detection systems I was a senior consultant for an mssp for a while with these big government and financial sector clients and so it was a huge relief in 2017 when I joined Shopify and got to work on this newfangled kubernetes thing that just about all of my other clients would have been terrified of but kubernetes and I have both come a long way since then and I've learned quite a bit in that time I'm really excited to be here with Danny as well Danny yep thank you Shane um hi I'm Dennis Santos I work at Shopify with chain in the infrasek team I joined back in 2020 and from the time I joined until now the security attack landscape has changed considerably especially with a lot of companies opting for the remote work approach and I've learned the thing to do about kubernetes over these years and how we can Harden our clusters to avoid takeovers I hope by the end of this talk you'll walk away with some ideas on how to mitigate some risks so here's the agenda we're going to start talking about why we should care about misconfiguration and then we're going to talk about cubotit a tool that we use internally and the security principles implement and then we're going to run a little demo where we're gonna show you the simple trick you're going to see if you bought it in action and we're going to run some attack defense scenarios and then we're going to talk about how exactly we used to bought it at Shopify and then we're going to finish by sharing some additional resources well every year Red Hat releases a report which analyzes emerging Trends in container kubernetes and Cloud native security it's called the
