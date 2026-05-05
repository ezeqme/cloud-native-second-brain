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
themes: ["AI ML", "Security", "Networking"]
speakers: ["John Zaiss", "Daniel Ruggeri", "Mastercard", "Surya Seetharaman", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1i7p0/microsegment-your-network-like-mastercard-with-adminnetworkpolicy-john-zaiss-daniel-ruggeri-mastercard-surya-seetharaman-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=Microsegment+Your+Network+Like+Mastercard+with+AdminNetworkPolicy+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Microsegment Your Network Like Mastercard with AdminNetworkPolicy - John Zaiss & Daniel Ruggeri, Mastercard & Surya Seetharaman, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Connectivity]]
- Temas: [[AI ML]], [[Security]], [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: John Zaiss, Daniel Ruggeri, Mastercard, Surya Seetharaman, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1i7p0/microsegment-your-network-like-mastercard-with-adminnetworkpolicy-john-zaiss-daniel-ruggeri-mastercard-surya-seetharaman-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=Microsegment+Your+Network+Like+Mastercard+with+AdminNetworkPolicy+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Microsegment Your Network Like Mastercard with AdminNetworkPolicy.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7p0/microsegment-your-network-like-mastercard-with-adminnetworkpolicy-john-zaiss-daniel-ruggeri-mastercard-surya-seetharaman-red-hat
- YouTube search: https://www.youtube.com/results?search_query=Microsegment+Your+Network+Like+Mastercard+with+AdminNetworkPolicy+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ptNWbJS7hiY
- YouTube title: Microsegment Your Network Like Mastercard with AdminNetworkP... J. Zaiss, D. Ruggeri, S. Seetharaman
- Match score: 0.857
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/microsegment-your-network-like-mastercard-with-adminnetworkpolicy/ptNWbJS7hiY.txt
- Transcript chars: 32730
- Keywords: network, policy, policies, tenant, cluster, tenants, microservices, spaces, little, segmentation, platform, default, ingress, application, workloads, mastercard, create, coming

### Resumo baseado na transcript

okay I wanted I always want to get a feel for like who's here so show of hands security is important to me John and Sir don't worry the audience has a pulse okay now uh here's another question and this is the one that's going to separate the normal people from the weird kids like me managing Network policy is fun all right my people we're going to hang out we're going to hang out um yeah so we're going to we're going to talk a little bit about

### Excerpt da transcript

okay I wanted I always want to get a feel for like who's here so show of hands security is important to me John and Sir don't worry the audience has a pulse okay now uh here's another question and this is the one that's going to separate the normal people from the weird kids like me managing Network policy is fun all right my people we're going to hang out we're going to hang out um yeah so we're going to we're going to talk a little bit about that uh and uh you know some of Massac card's Journey on micro segmentation and some of the really cool stuff that John and Sur have worked on uh to get us there so we'll go ahead and hop into the next slide do some quick introductions suria hey everyone I'm Surya I'm an engineer working on the open shift networking team at Red Hat I'm a contributor to the Sig Network Community Upstream especially in the Sig Network policy API working group which is a sub project in Sig Network yeah hi I'm John z um principal engineer at at MasterCard and my primary role is the uh architecture for our on premise kubernetes I've been there 20 plus years and someone once referred to me as a piece of furniture been there so long better in dinosaur uh Hey guys D Jerry uh distinguished engineer at MasterCard huge open source and Boss Fan uh been doing a lot of interesting stuff at MasterCard and the past five years specifically I've been leading a lot of our micr segmentation initiatives and these days I now own the kubernetes platform as well for our enrum deployment so I want to spend just a quick minute to talk about Master Card uh the good news is for those that don't know you don't owe us any money we're not a bank what we do is we interconnect a lot of different banks and why this matters uh we are a network security is very important for our Network right so if you kind of think about what we do we're more like your cell phone provider or your internet service provider than we are necessarily your bank yes we do offer a lot of stuff uh value eded Services uh on top of the network but at the end of the day we're really a network and that's what we're here to talk a little bit about is our micr segmentation Journey so we're not going to cover how to micr segment your network like MasterCard completely because guys there is a lot of stuff out there we have to be concerned with segmenting and separating workloads like bare metal nodes main frames virtual machines and a couple tens of thousands of containers right but we are here to tal
