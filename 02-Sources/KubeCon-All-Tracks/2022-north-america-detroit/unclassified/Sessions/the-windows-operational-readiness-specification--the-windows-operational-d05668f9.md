---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Unclassified"
themes: ["Cloud Native"]
speakers: ["Amim Moises Salum Knabben", "Xinqi Li", "VMware"]
sched_url: https://kccncna2022.sched.com/event/182FM/the-windows-operational-readiness-specification-amim-moises-salum-knabben-xinqi-li-vmware
youtube_search_url: https://www.youtube.com/results?search_query=The+Windows+Operational+Readiness+Specification+CNCF+KubeCon+2022
slides: []
status: parsed
---

# The Windows Operational Readiness Specification - Amim Moises Salum Knabben & Xinqi Li, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Unclassified]]
- Temas: [[Cloud Native]]
- País/cidade: United States / Detroit
- Speakers: Amim Moises Salum Knabben, Xinqi Li, VMware
- Schedule: https://kccncna2022.sched.com/event/182FM/the-windows-operational-readiness-specification-amim-moises-salum-knabben-xinqi-li-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=The+Windows+Operational+Readiness+Specification+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre The Windows Operational Readiness Specification.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182FM/the-windows-operational-readiness-specification-amim-moises-salum-knabben-xinqi-li-vmware
- YouTube search: https://www.youtube.com/results?search_query=The+Windows+Operational+Readiness+Specification+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=V3Us2IYjq8k
- YouTube title: The Windows Operational Readiness Specification - Amim Moises Salum Knabben & Xinqi Li, VMware
- Match score: 0.771
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/the-windows-operational-readiness-specification/V3Us2IYjq8k.txt
- Transcript chars: 16004
- Keywords: windows, cluster, operational, upstream, closer, running, categories, called, conformance, started, version, binary, results, server, inside, readiness, implementation, interested

### Resumo baseado na transcript

I was talking about what is conference test why would we need that and what's the difference between limited performance and windows operational readiness then we are gonna take a deeper look at the kubernetes which defines the windows operational resonance in detail and there is a corresponding implementation of this account which is called Windows operational Readiness as well and uh where the tool aims to provide a convenient way to run the performance to run the windows operational relevance test so we're gonna go through it go through

### Excerpt da transcript

I was talking about what is conference test why would we need that and what's the difference between limited performance and windows operational readiness then we are gonna take a deeper look at the kubernetes which defines the windows operational resonance in detail and there is a corresponding implementation of this account which is called Windows operational Readiness as well and uh where the tool aims to provide a convenient way to run the performance to run the windows operational relevance test so we're gonna go through it go through it and this tool can also be run as a sunflower coffee so a main route has more like how and this project has already been integrated with other Upstream projects as well so I mean we'll tell us a little bit more about the usage of this product and finally this project is still a working progress so we want to bring a framework attention from the community and we will like to see the most our collaboration on this the goal the goal of this talk is to um the golf resort is to introduce the windows the idea of Windows operational Readiness and attract more people like we're very well very well going to Upward and anyone else was interested in this project started their contribution to the uptrend so um the first question here is what is performance test so imagine you as a kubernetes vendor and let's say um you have to ship a product to your customer that helps customers to create kubernetes one certified clusters so how do you verify the project for the cluster created by your product to support all the required apis in Google next 155 that's the protocol connection work can user amount of volume to their cost and also if you imagine yourself as a kubernetes developer how do you know that the feature you are about to add to one to or works well all the works well with all the existing features there and if you are like troubleshoot the cluster how do you know about uh how to systematically figure out what works and what doesn't work so the answers to all the questions here is that if we have a suite kubernetes cluster including the API Machinery apps notes networks storage like just like all the expats then if your cluster can pass the test there and you can confidently say that the cluster is a valid kubernetes cluster um and um so this Suite of test is called conformance test conformance test uh defined by cncf and so if you explore the option kubernetes test conformance folder you will find a yaml file called conforman
