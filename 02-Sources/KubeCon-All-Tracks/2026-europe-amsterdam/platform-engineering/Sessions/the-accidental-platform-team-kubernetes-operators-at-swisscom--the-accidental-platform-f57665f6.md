---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Fabian Schulz", "Jelena Malic", "Swisscom"]
sched_url: https://kccnceu2026.sched.com/event/2CW6q/the-accidental-platform-team-kubernetes-operators-at-swisscom-fabian-schulz-jelena-malic-swisscom
youtube_search_url: https://www.youtube.com/results?search_query=The+Accidental+Platform+Team%3A+Kubernetes+Operators+at+Swisscom+CNCF+KubeCon+2026
slides: []
status: parsed
---

# The Accidental Platform Team: Kubernetes Operators at Swisscom - Fabian Schulz & Jelena Malic, Swisscom

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Fabian Schulz, Jelena Malic, Swisscom
- Schedule: https://kccnceu2026.sched.com/event/2CW6q/the-accidental-platform-team-kubernetes-operators-at-swisscom-fabian-schulz-jelena-malic-swisscom
- Busca YouTube: https://www.youtube.com/results?search_query=The+Accidental+Platform+Team%3A+Kubernetes+Operators+at+Swisscom+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre The Accidental Platform Team: Kubernetes Operators at Swisscom.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW6q/the-accidental-platform-team-kubernetes-operators-at-swisscom-fabian-schulz-jelena-malic-swisscom
- YouTube search: https://www.youtube.com/results?search_query=The+Accidental+Platform+Team%3A+Kubernetes+Operators+at+Swisscom+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=OgE9X1uBfGo
- YouTube title: The Accidental Platform Team: Kubernetes Operators at Swisscom - Fabian Schulz & Jelena Malic
- Match score: 0.899
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/the-accidental-platform-team-kubernetes-operators-at-swisscom/OgE9X1uBfGo.txt
- Transcript chars: 29927
- Keywords: network, platform, course, operators, engineers, actually, basically, knowledge, understand, automation, around, already, wizard, create, swisscom, management, routers, created

### Resumo baseado na transcript

So, welcome to this last afternoon of CubeCon to our talk about how we went from building Kubernetes operators to becoming a platform team. So, in this team we have Yelina here with me who is the product owners of the team and I'm a DevOps engineer writing the Kubernetes operators. If you think about the bigger country like Germany or the Netherlands, it scales. maybe you know this network vizard but I'm topping up this type of wizard because to us it sometimes feels like magic that uh the phone just can connect to the internet over these kubernetes things here. So you can see that it doesn't look so nice all that time is used and also while he is doing these designs he needs to talk to multiple people. I mean he needs to talk to the operating system people to the people operating the Kubernetes distribution and to all the different other network engineers that manage our backbone.

### Excerpt da transcript

Hello. Hello. Hi. So, welcome to this last afternoon of CubeCon to our talk about how we went from building Kubernetes operators to becoming a platform team. So, in this team we have Yelina here with me who is the product owners of the team and I'm a DevOps engineer writing the Kubernetes operators. So, we work for Swisscom. Swisscom is the leading telco in Switzerland and a large IT solutions provider. So our team got created two years ago and the goal was basically bring cloud native to telco and modernize a bit the automation the generation of our networks. So we had to generate networks for the mobile data core. Let's have a look where the mobile data core is. So on the left hand side you can see the phone the user equipment. It connects to the closest antenna. From there the data then gets routed to the mobile data core and then most probably out to the internet. So, let's have a look at this mobile data core. So, this is now the 5G mobile data core. And just as a side note, just because your phone has the 5G icon doesn't mean it's using a 5G mobile data core.

That just means it connects to the antenna using 5G. So, lots of telos still have the 4G core. Now, we have the 5G core. And this one is fully running on Kubernetes. So, you can see here in blue the pods uh and the mobile data core. It's structured in those cloudnative functions. You have different functions. Some are there for the session management, some for the antenna to connect to it, manage your subscriber data, data analytics. There's lots of things. So in one dev environment, we have around 2,000 pods. Of course, for this, we use around 32 big servers for one dev environment. And since we're in telco, we want redundancy. So we have three to four data centers, our own data centers in Switzerland where we operate it. Of course, Switzerland, we have 8 million inhabitants. If you think about the bigger country like Germany or the Netherlands, it scales. So there's quite some needs for the network. So who operate, who creates these networks? It's basically our 5G network engineers. I will call them wizard from here on.

And not this type of wizard. maybe you know this network vizard but I'm topping up this type of wizard because to us it sometimes feels like magic that uh the phone just can connect to the internet over these kubernetes things here. So let's have a look what he needs to do to deploy a new 5G network function. We'll select UPF that's the user plane function that's basically th
