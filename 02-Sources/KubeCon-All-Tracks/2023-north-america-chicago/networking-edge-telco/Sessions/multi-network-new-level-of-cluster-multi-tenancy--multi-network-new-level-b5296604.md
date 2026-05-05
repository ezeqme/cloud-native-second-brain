---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Networking + Edge + Telco"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Maciej Skrocki", "Google", "Doug Smith", "Red Hat", "Inc."]
sched_url: https://kccncna2023.sched.com/event/1R2m0/multi-network-new-level-of-cluster-multi-tenancy-maciej-skrocki-google-doug-smith-red-hat-inc
youtube_search_url: https://www.youtube.com/results?search_query=Multi-Network%2C+New+Level+of+Cluster+Multi-Tenancy+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Multi-Network, New Level of Cluster Multi-Tenancy - Maciej Skrocki, Google & Doug Smith, Red Hat, Inc.

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Networking + Edge + Telco]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Chicago
- Speakers: Maciej Skrocki, Google, Doug Smith, Red Hat, Inc.
- Schedule: https://kccncna2023.sched.com/event/1R2m0/multi-network-new-level-of-cluster-multi-tenancy-maciej-skrocki-google-doug-smith-red-hat-inc
- Busca YouTube: https://www.youtube.com/results?search_query=Multi-Network%2C+New+Level+of+Cluster+Multi-Tenancy+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Multi-Network, New Level of Cluster Multi-Tenancy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2m0/multi-network-new-level-of-cluster-multi-tenancy-maciej-skrocki-google-doug-smith-red-hat-inc
- YouTube search: https://www.youtube.com/results?search_query=Multi-Network%2C+New+Level+of+Cluster+Multi-Tenancy+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XbDh0ixmQRg
- YouTube title: Multi-Network, New Level of Cluster Multi-Tenancy - Maciej Skrocki, Google & Doug Smith, Red Hat
- Match score: 0.781
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/multi-network-new-level-of-cluster-multi-tenancy/XbDh0ixmQRg.txt
- Transcript chars: 29255
- Keywords: network, networking, implementation, basically, networks, device, introduce, multiple, object, cluster, container, native, actually, resource, create, working, connect, having

### Resumo baseado na transcript

thanks everybody for taking the time to come to our talk about multin Network a new level of cluster multi-tenancy today what we're going to look at is first of all what is kubernetes native multi networking and then we're going to dig into some of the use cases about how you would get multi networking going Ma is going to take you through a user Journey we're going to get down to some of the brass taxs and show you exactly what it looks like when from a user

### Excerpt da transcript

thanks everybody for taking the time to come to our talk about multin Network a new level of cluster multi-tenancy today what we're going to look at is first of all what is kubernetes native multi networking and then we're going to dig into some of the use cases about how you would get multi networking going Ma is going to take you through a user Journey we're going to get down to some of the brass taxs and show you exactly what it looks like when from a user perspective you're setting up multi networking on some pods we're going to talk a little bit about some of the ancillary pieces that are involved in this as well as some of the history behind it like what predates the kubernetes native multi networking and then we are going to invite you to get involved I am Doug Smith I am a redh Hatter um who's an open shift uh engineer and I have been involved in uh multi networking with kubernetes for some time and I'm particularly interested in Telco and performance networking use cases and I'm joined today by Mach hi my name is mach and I am a software engineer at Google working in the GK anos networking team so what exactly is multin networking today if you spin up kubernetes and you spin up a pod and you go and exec into that pod and you do IPA you are going to see a pod with a single network interface outside of the loop back e zero so you see that up on the top and then down at the bottom you see that that pod via eth zero has connectivity to all of the other pods in that Network and that's kind of a kubernetes promise that you get and then you would take and you would limit that um connectivity using network policy but you have to ask yourself what if that single interface just isn't enough so what kubernetes Native multi networking does is at the most basic level allows you to spin up a pod with multiple network interfaces so that you can get connect ity to exactly the places that you want it to go in an isolated or performant fashion and we'll get into all of the different ways you might utilize that and you might ask yourself why is it that we are working on this now yeah we all thinking right now that it's about time to talk about and adding multi networking to kubernetes as a whole as a project it is very stable and uh adopted very well we cross the chasm of adoption and we think that it is the right time to start talking and pick up more complex uh topics uh in uh kubernetes as a whole as a project um that's why we are thinking of um committing time t
