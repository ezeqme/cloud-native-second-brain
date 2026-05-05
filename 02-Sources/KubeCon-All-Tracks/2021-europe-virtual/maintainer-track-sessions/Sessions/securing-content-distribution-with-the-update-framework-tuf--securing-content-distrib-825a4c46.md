---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Community Governance"]
speakers: ["Lukas Puehringer", "NYU", "Tandon School of Engineering", "Joshua Lock", "VMware"]
sched_url: https://kccnceu2021.sched.com/event/iE7h/securing-content-distribution-with-the-update-framework-tuf-lukas-puehringer-nyu-tandon-school-of-engineering-joshua-lock-vmware
youtube_search_url: https://www.youtube.com/results?search_query=Securing+Content+Distribution+with+The+Update+Framework+%28TUF%29+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Securing Content Distribution with The Update Framework (TUF) - Lukas Puehringer, NYU, Tandon School of Engineering & Joshua Lock, VMware

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Lukas Puehringer, NYU, Tandon School of Engineering, Joshua Lock, VMware
- Schedule: https://kccnceu2021.sched.com/event/iE7h/securing-content-distribution-with-the-update-framework-tuf-lukas-puehringer-nyu-tandon-school-of-engineering-joshua-lock-vmware
- Busca YouTube: https://www.youtube.com/results?search_query=Securing+Content+Distribution+with+The+Update+Framework+%28TUF%29+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Securing Content Distribution with The Update Framework (TUF).

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iE7h/securing-content-distribution-with-the-update-framework-tuf-lukas-puehringer-nyu-tandon-school-of-engineering-joshua-lock-vmware
- YouTube search: https://www.youtube.com/results?search_query=Securing+Content+Distribution+with+The+Update+Framework+%28TUF%29+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=7BVVhfCWwDM
- YouTube title: Securing Content Distribution with The Update Framework (TUF) - Lukas Puehringer & Joshua Lock
- Match score: 0.883
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/securing-content-distribution-with-the-update-framework-tuf/7BVVhfCWwDM.txt
- Transcript chars: 21772
- Keywords: content, software, specification, update, implementation, systems, distribution, security, secure, package, attacks, repository, framework, integrity, malicious, internal, responsibilities, python

### Resumo baseado na transcript

hello everyone and welcome to our talk securing content distribution with the update framework my name is lucas puringa i'm maintainer of the software security supply chain projects tough ending toto at new york university's secure system lab my name is joshua locke i am the security lead in vmware's open source technology center where i also maintain tough okay um let's see uh what we're gonna talk about today um so first we will talk very briefly about content distribution what we actually mean by that and what challenges

### Excerpt da transcript

hello everyone and welcome to our talk securing content distribution with the update framework my name is lucas puringa i'm maintainer of the software security supply chain projects tough ending toto at new york university's secure system lab my name is joshua locke i am the security lead in vmware's open source technology center where i also maintain tough okay um let's see uh what we're gonna talk about today um so first we will talk very briefly about content distribution what we actually mean by that and what challenges exist then we'll give a tough primer tough being short for the update framework and talk about the pillar stuff is based on and the principles it it uses and yeah and how it all faces the challenges of content and last but not least we'll talk about how to get involved in the project because this is a maintainer track talk of a of an open source project so we want you to get excited and help us out but first things first um content distribution what content do we mean um basically any digital content that needs to be kept up to date um this can be software primarily it is software but it can also be any sort of metadata legal documents etc um but yeah usually it is software [Music] as such the content distribution is part of the software supply chain and a very crucial part too because it's at the user boundary in this software supply chain graph by software supply chain i mean all the steps that are carried out in order to write software to test it build it package it and to finally ship it out so being at the edge of this graph content distribution needs to be done carefully because whatever gets distributed is what um [Music] should be what the um well let's let's put it differently so um [Music] once software leaves the premises of the software producers there is um they will have a hard time to enforce any quality assurance on the software so it should make sure that the software they intend the user to have is actually the software that they get so that is why this is a crucial part of the supply chain and also a very attractive target for attackers because if the attackers compromise the content distribution they can have a huge impact of millions of users potentially um and this also happens in the real world and joshua will talk a little bit about uh when this happened before sure and just an excellent please lucas oh so um you might think that software secure software updates are a sole problem especially if you like me come f
