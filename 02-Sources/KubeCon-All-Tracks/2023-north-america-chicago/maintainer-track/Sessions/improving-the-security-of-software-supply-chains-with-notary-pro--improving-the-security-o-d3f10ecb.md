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
themes: ["AI ML", "Security", "Community Governance"]
speakers: ["Toddy Mladenov", "Microsoft", "Milind Gokarn", "Amazon"]
sched_url: https://kccncna2023.sched.com/event/1R2sK/improving-the-security-of-software-supply-chains-with-notary-project-toddy-mladenov-microsoft-milind-gokarn-amazon
youtube_search_url: https://www.youtube.com/results?search_query=Improving+the+Security+of+Software+Supply+Chains+with+Notary+Project+CNCF+KubeCon+2023
slides: []
status: parsed
---

# Improving the Security of Software Supply Chains with Notary Project - Toddy Mladenov, Microsoft & Milind Gokarn, Amazon

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Security]], [[Community Governance]]
- País/cidade: United States / Chicago
- Speakers: Toddy Mladenov, Microsoft, Milind Gokarn, Amazon
- Schedule: https://kccncna2023.sched.com/event/1R2sK/improving-the-security-of-software-supply-chains-with-notary-project-toddy-mladenov-microsoft-milind-gokarn-amazon
- Busca YouTube: https://www.youtube.com/results?search_query=Improving+the+Security+of+Software+Supply+Chains+with+Notary+Project+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre Improving the Security of Software Supply Chains with Notary Project.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sK/improving-the-security-of-software-supply-chains-with-notary-project-toddy-mladenov-microsoft-milind-gokarn-amazon
- YouTube search: https://www.youtube.com/results?search_query=Improving+the+Security+of+Software+Supply+Chains+with+Notary+Project+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Z2mzoO9waDM
- YouTube title: Improving the Security of Software Supply Chains with Notary Project- Toddy Mladenov & Milind Gokarn
- Match score: 0.904
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/improving-the-security-of-software-supply-chains-with-notary-project/Z2mzoO9waDM.txt
- Transcript chars: 20384
- Keywords: signing, actually, notary, images, notation, signatures, registry, signature, control, infrastructure, security, signed, artifacts, allows, another, signer, plugins, attestations

### Resumo baseado na transcript

welcome everyone uh welcome to improving the security of software Supply chains with notary project I'm to malinov I a principal product manager at Microsoft mil I'm a senior engineer at Amazon AWS okay so uh today we'll go kind of through the update of uh notary project what happened over the last six months so we'll start with some overview uh we'll talk a little bit about the uh release of the tooling that uh uh we had we'll talk about the features so folks who are not familiar

### Excerpt da transcript

welcome everyone uh welcome to improving the security of software Supply chains with notary project I'm to malinov I a principal product manager at Microsoft mil I'm a senior engineer at Amazon AWS okay so uh today we'll go kind of through the update of uh notary project what happened over the last six months so we'll start with some overview uh we'll talk a little bit about the uh release of the tooling that uh uh we had we'll talk about the features so folks who are not familiar with notary project can learn a little bit more what they can use it for uh we have a couple of demos and uh we'll talk about our road map at the end you'll have the opportunity to ask any questions uh notary project is a set of specifications and tools intended to improve the security of Supply chains for software uh I would like to talk a little bit about our kind of philosophy and how do we think about the the supply chain as well as how we hear customers are actually approaching the the security so the first thing is smooth transition so when we say smooth transition we understand that everybody wants to go and look at the latest and the greatest but most of uh the customers that we talk with they already say look I have some infrastructure let whether it's infrastructure for managing Keys infrastructure for uh even signing uh some kind of Legacy signing uh approaches we would like to have an easy way without going and deploying a bunch of new things and and setting a bunch of infrastructure to actually move to something more modern but we also don't want to be locked into this Legacy infrastructure we would like to have a path that in the future we can use things like for example manage keys or you may know it as a keyless signing for example something that pint will uh go and demo later on so that is one one of the principles that we try to follow so we provide really smooth transition for for uh our users the next thing is uh signature portability so especially in the container space what we learned is that you sign containers in one place and you may use them in a completely different place uh typical example is like you pull the containers from Docker Hub as a base images that you use to build your application right and whoever pushes the images to docker they need to be able to sign them but after that most probably what you do is you copy these images from Docker Hub into your own registry or you copy them from your own registry into some air gap environment you don't
