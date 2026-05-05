---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Peter Hunt", "Sohan Kunkerkar", "Red Hat"]
sched_url: https://kccncna2024.sched.com/event/1hoy9/cri-o-features-for-fun-and-profit-peter-hunt-sohan-kunkerkar-red-hat
youtube_search_url: https://www.youtube.com/results?search_query=CRI-O+Features+for+Fun+and+Profit+CNCF+KubeCon+2024
slides: []
status: parsed
---

# CRI-O Features for Fun and Profit - Peter Hunt & Sohan Kunkerkar, Red Hat

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United States / Salt Lake City
- Speakers: Peter Hunt, Sohan Kunkerkar, Red Hat
- Schedule: https://kccncna2024.sched.com/event/1hoy9/cri-o-features-for-fun-and-profit-peter-hunt-sohan-kunkerkar-red-hat
- Busca YouTube: https://www.youtube.com/results?search_query=CRI-O+Features+for+Fun+and+Profit+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre CRI-O Features for Fun and Profit.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1hoy9/cri-o-features-for-fun-and-profit-peter-hunt-sohan-kunkerkar-red-hat
- YouTube search: https://www.youtube.com/results?search_query=CRI-O+Features+for+Fun+and+Profit+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=6-OTdYwhKQQ
- YouTube title: CRI-O Features for Fun and Profit - Peter Hunt & Sohan Kunkerkar, Red Hat
- Match score: 0.733
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cri-o-features-for-fun-and-profit/6-OTdYwhKQQ.txt
- Transcript chars: 23360
- Keywords: container, basically, images, feature, support, containers, actually, change, couple, little, volume, trying, features, source, already, running, verify, policy

### Resumo baseado na transcript

thank you everyone for joining um uh our talk and staying to the end of cubec con I hope everyone's had a really productive and uh exciting cuon um today we're here talking about cryo so if you don't want to listen about cryo then you should leave now I won't be offended my name is Peter hunt I'm a senior software engineer at Red Hat I'm a cryo maintainer and I'm a Sig no chair I with me hey my name is soan ker I work at D and Nam spaces uh and so that because in kubernetes often the name space is the granularity of multitenancy so we added this support so basically there's a path that you write uh Etsy uh containers policy do uh com.

### Excerpt da transcript

thank you everyone for joining um uh our talk and staying to the end of cubec con I hope everyone's had a really productive and uh exciting cuon um today we're here talking about cryo so if you don't want to listen about cryo then you should leave now I won't be offended my name is Peter hunt I'm a senior software engineer at Red Hat I'm a cryo maintainer and I'm a Sig no chair I with me hey my name is soan ker I work at D and I'm a senior software engineer I'm one of the cry maintainers and a sign um member of the Sig node and today we're going to be uh talking about some cryo features maintainer track for cryo um features for Fun and Profit so um to start us off if you're not familiar with cry I'm going to do a really quick introduction the um the sort of what how we Define cryo is a it's a implementation of the kubes container runtime interface um which is compliant with the uh open container initiative um containers manages so what does that mean you can imag it basically occupying the same level of the stack as Doctor used to so the cuet is going to talk directly to cry to do all of its actual container image um pod management um because cryo is uh focused solely on kubernetes as opposed to a more generic container runtime we get to make some like certain decisions about how we design it we get to purpose build for kubernetes we focus on security because we know the only use cases we care about is running containers in production rather than debugging or like you know building your containers um and uh we support all uh oci container images run times and Registries after so now that we've had a little bit of introduction let's get into the fun stuff the features um first up we're going to talk a little bit about some integration that we've recently done with sigstore so for a while uh cryo has had support for verifying signatures for images so basically when the cuet request cryo to pull an image cryo will first verify that it's able to uh you know verify the signature with the registry um and if it's not uh then you know it denies that image is pulled so it's happening right at the source which is you know an advantage um to some of the other um policy uh uh engines that stop you from um pulling images um the uh so it's enforced based both on image pull and container Creation in case uh container is shared an image is shared and we didn't actually do the repo um but currently it used to be node level so basically every single image that was verified
