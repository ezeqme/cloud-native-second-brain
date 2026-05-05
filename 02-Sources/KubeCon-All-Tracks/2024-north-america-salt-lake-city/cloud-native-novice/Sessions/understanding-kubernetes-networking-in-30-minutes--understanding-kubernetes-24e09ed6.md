---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Novice"
themes: ["Networking", "Kubernetes Core"]
speakers: ["Ricardo Katz", "Broadcom", "James Strong", "Isovalent at Cisco"]
sched_url: https://kccncna2024.sched.com/event/1i7p5/understanding-kubernetes-networking-in-30-minutes-ricardo-katz-broadcom-james-strong-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Understanding+Kubernetes+Networking+in+30+Minutes+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Understanding Kubernetes Networking in 30 Minutes - Ricardo Katz, Broadcom & James Strong, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Novice]]
- Temas: [[Networking]], [[Kubernetes Core]]
- País/cidade: United States / Salt Lake City
- Speakers: Ricardo Katz, Broadcom, James Strong, Isovalent at Cisco
- Schedule: https://kccncna2024.sched.com/event/1i7p5/understanding-kubernetes-networking-in-30-minutes-ricardo-katz-broadcom-james-strong-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Understanding+Kubernetes+Networking+in+30+Minutes+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Understanding Kubernetes Networking in 30 Minutes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7p5/understanding-kubernetes-networking-in-30-minutes-ricardo-katz-broadcom-james-strong-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Understanding+Kubernetes+Networking+in+30+Minutes+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Mj04QOqAaJ8
- YouTube title: Understanding Kubernetes Networking in 30 Minutes - Ricardo Katz & James Strong
- Match score: 0.87
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/understanding-kubernetes-networking-in-30-minutes/Mj04QOqAaJ8.txt
- Transcript chars: 30270
- Keywords: actually, networking, network, container, cluster, external, addresses, running, change, tables, namespace, traffic, ricardo, interfaces, communicate, communication, internal, usually

### Resumo baseado na transcript

everyone thank you for coming today my name is jameses strong we're going to talk about understanding kubernetes networking in 30 minutes or as I like to call a Mario speedrun through kubernetes networking um my name is James strong like I said I've already done that I'm a Solutions architect at ISO valent now which is a part of Cisco I am a maintainer of Ingress and gentic so if you have any questions about that uh ask me in an hour at my next talk um so I I call uh HTTP and backend which is POS it the service name right so with that if I keep creating the service with the same name on different them spaces I have reproducible uh architectures reproducible blueprints right I don't need to keep doing adding on all of my environment uh uh uh variables or my configuration the service IP instead of the uh uh the name right and the way that it happens um okay so I'm going to get the logs and I'm going to show you DNS will go to kubernetes API check what's the service AP and return you back that API okay cool it's not and we're back to the beginning all of our pces are there we've got C DNS proxy cni and uh all of our pods connected um other opponents to consider so some of the things so this is again very basic intro to kubernetes networking something to consider is that all of these pods can talk to every other pod um by default so you would need something like

### Excerpt da transcript

everyone thank you for coming today my name is jameses strong we're going to talk about understanding kubernetes networking in 30 minutes or as I like to call a Mario speedrun through kubernetes networking um my name is James strong like I said I've already done that I'm a Solutions architect at ISO valent now which is a part of Cisco I am a maintainer of Ingress and gentic so if you have any questions about that uh ask me in an hour at my next talk um so I won't be taking those questions I'm also the author of networking kubernetes I have an A CL Guru course on the same thing and um unfortunately uh I could not bring my gimly cosplay here but I do have a full gimly cosplay outfit cool my name is Ricardo I am a software engineer at vmb broadcom uh I have created the cook I don't know if someone still uses that like it's kind of broken those days like Ingress like Ingress in gyx I'm one of the maintainers of Ingress in gyx so everything that I touch usually breaks sorry and I breaks it I approve it yeah and I am a Lego Enthusiast so I I love Legos so today we going to talk about understanding Linux uh kubernetes networking but one of the when I was first learning kubernetes one of the old adages was that you know kubernetes is just Linux and um sorry for any of the windows folks out there we will not be talking about that one and when we say this um I like to bring up this picture I found this is a great one for the talk um for those who don't know this is the data flow of a packet through the kernel so um was setting the bar really low for us so let's strap in so agenda we're going to talk about Linux networking we're going to talk about what a pod is what's uh what part of it is and talk about container networking and how we build those criar abstractions on top of Linux Ricardo you want to go ahead yeah sure so um we are going to start doing some Demos in in a minute but I want you you don't need to take pictures we going to put that on the scum promise there's lots of pictures so yes so uh this is how uh a kubernetes networking actually looks like and we are going to actually start building our networking over this with demos and showing like uh how the routing actually works why we have a CNS and what's Cube proxy and why everyone actually hates Cube proxy I can't say anything sorry yeah so we'll start by talking about Linux networking and what the N networking stack is so the base of every ku's workload is working on a node a node has an Ethernet inte
